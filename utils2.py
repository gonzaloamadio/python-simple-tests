import pytz
from dateutil import parser, tz


def _parse_scheduled_rrule(rrule_dic):
    """Translate an rrule to a human readable str

        It is an hadoc translation for our subset of rrule possibilities.
        A complete parse is more complex than this.

        INPUT
             {'FREQ':str, 'INTERVAL':str, 'UNTIL':str, 'BYMONTHDAY':str
              'BYDAY':str}

        OUTPUT:
            String with human readable translation
    """

    # return ordinal suffix for a number
    def ordinal_suffix(n):
        return {1: "ST", 2: "ND", 3: "RD"}.get(n if (n < 20) else (n % 10), 'TH')

    weekdays_name_map = {'MO': 'MONDAY', 'TU': 'TUESDAT', 'WE': 'WEDNESDAT', 'TH': 'THURSDAY',
                         'FR': 'FRIDAY', 'SA': 'SATURDAY', 'SU': 'SUNDAY'}
    weekdays_order_map = {'MONDAY': 0, 'TUESDAY': 1, 'WEDNESDAY': 2,
                          'THURSDAY': 3, 'FRIDAY': 4, 'SATURDAY': 5, 'SUNDAY': 6}

    def create_days_list(days):
        """From TH,MO to MONDAY,THURSDAY"""
        days_list = [weekdays_name_map.get(x) for x in days.split(",")]
        slist = sorted(days_list, key=weekdays_order_map.get)
        return ','.join(slist)

    freq = rrule_dic.get("FREQ", None)
    interval = rrule_dic.get("INTERVAL", None)
    bymonthday = rrule_dic.get("BYMONTHDAY", None)
    byday = rrule_dic.get("BYDAY", None)
    ret = "EVERY "

    # --- MONTHLY --- #

    if freq == "MONTHLY":
        ret += interval+" MONTHS ON THE " if int(interval) > 1 else "MONTH ON THE "
        # There are 2 possible values if it is a monthly schedule.
        # On a specific day or the [first|second|third|fourth] day of the monts
        # Examples:
        #   "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200320T025959Z;BYMONTHDAY=5"
        #   "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200327T025959Z;BYDAY=+1FR"
        #   "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200327T025959Z;BYDAY=+3TH"
        if bymonthday:
            ret += bymonthday + ordinal_suffix(int(bymonthday))
        else:
            num_day = ''.join(filter(str.isdigit, byday))
            ret += num_day + ordinal_suffix(int(num_day))
            ret += " "+weekdays_name_map[''.join(filter(str.isalpha, byday))]
        ret += " AT"
    elif freq == "DAILY":
        # In daily schedule, we can just select every X days
        ret += interval+" DAYS AT" if int(interval) > 1 else "DAY AT"
    elif freq == "WEEKLY":
        # On weekly, we can select ever X weeks, and also which days of the week
        # Examples:
        #    "FREQ=WEEKLY;INTERVAL=2;BYDAY=TH,MO",
        #    "FREQ=WEEKLY;INTERVAL=1;UNTIL=20200320T025959Z;BYDAY=WE,TH"
        ret += interval+" WEEKS ON " if int(interval) > 1 else "WEEK ON "
        ret += create_days_list(byday)
        ret += " AT"
    else:
        ret = "SCHEDULE NOT RECOGNIZED"
    return ret


def create_friendly_repr_of_schedule_rule(rrule, exec_interval, exec_datetime, rule_timezone=None):
    """Creates a friendly representation of the schedule rule to show in a job information

    Example values for fields (shaped like this)

    "recurrence_rule": "" || "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200320T025959Z;BYMONTHDAY=5"
    "execution_interval": "Now" || "One Time" || "Repeat"
    "execution_datetime": "2020-03-05 20:00:00",
    "rule_timezone" : "America/Buenos_Aires"
    """
    ei_intervals = {"not_scheduled": "Now", "run_one_time": "One Time", "scheduled": "Repeat"}
    rule = time_str = ends_str = ""
    # From start date, split date and time
    start_datetime = pytz.utc.localize(exec_datetime).astimezone(pytz.timezone(rule_timezone))
    start_date = start_datetime.strftime("%m/%d/%Y")
    start_hour = start_datetime.strftime("%I:%M %p")  # '08:00 PM'
    start_hour = start_hour[0] == "0" and start_hour[1:]  # '8:00 PM'

    # --- Job not scheduled, i.e. run now and that is all, we show nothing --- #

    if exec_interval == ei_intervals["not_scheduled"]:
        return "", "", "", True

    # ----- Job is scheduled to run only one time in a specific date ----- #

    if exec_interval == ei_intervals["run_one_time"]:
        rule = start_date
        time_str = start_hour
        ends_str = "DOES NOT REPEAT"
        return rule, time_str, ends_str, False

    # ----- If it is scheduled and should be repeated ----- #

    # Store values of the recurrence_rule rule in a dict
    rrule_values = {'FREQ': None, 'INTERVAL': None, 'UNTIL': None,
                    'BYMONTHDAY': None, 'BYDAY': None, 'COUNT': None}
    for r in rrule.split(';'):
        key, val = r.split("=", 1)
        rrule_values[key] = val

    time_str = start_hour

    if rrule_values["UNTIL"]:
        until = parser.parse(rrule_values["UNTIL"])
        from_zone = tz.gettz('UTC')
        # from_zone = tz.tzutc()
        to_zone = tz.gettz(rule_timezone) if rule_timezone else tz.tzlocal()
        # localized until
        until = until.replace(tzinfo=from_zone).astimezone(to_zone)
        ends_str = until.strftime("%m/%d/%Y")
    else:
        ends_str = "NEVER ENDS"

    rule = _parse_scheduled_rrule(rrule_values)

    return rule, time_str, ends_str, False

rrule= "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200320T025959Z;BYMONTHDAY=5"
exec_interval = "Repeat"
exec_datetime = parser.parse("2020-03-05 20:00:00")
rule_timezone = "America/Buenos_Aires"
print(create_friendly_repr_of_schedule_rule(rrule, exec_interval, exec_datetime, rule_timezone))

