from dateutil import parser, rrule
import pytz

"""
>>> parser.parse("20200320T025959Z")
datetime.datetime(2020, 3, 20, 2, 59, 59, tzinfo=tzutc())
"""


def parse_rrule(rrule_dic):
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
    ordinal_suffix = lambda n :{ 1: "st", 2: "nd", 3: "rd" }.get(n if (n < 20) else (n % 10), 'th')
    weekdays_name_map = {'MO':'MONDAY','TU':'TUESDAT','WE':'WEDNESDAT','TH':'THURSDAY',
                    'FR':'FRIDAY','SA':'SATURDAY','SU':'SUNDAY',}

    freq = rrule_dic.get("FREQ",None)
    interval = rrule_dic.get("INTERVAL",None)
    until = rrule_dic.get("UNTIL",None)
    bymonthday = rrule_dic.get("BYMONTHDAY",None)
    byday = rrule_dic.get("BYDAY",None)
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
            ret += ordinal_suffix(bymonthday)
        else:
            ret += ordinal_suffix(int(''.join(filter(str.isdigit, byday))))
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
        ret += ','.join([weekdays_name_map.get(x) for x in byday.split(",")])
        ret += " AT"
    else:
        ret = "SCHEDULE NOT RECOGNIZED"
    return ret

def create_string(rrule,exec_interval,exec_datetime,rule_timezone):
    """
    Toma datos como estos:
    root_value = {
    "execution_interval": "Now" || "One Time" || "Repeat"
    "recurrence_rule": "" || "FREQ=MONTHLY;INTERVAL=1;UNTIL=20200320T025959Z;BYMONTHDAY=5"
    "first_execution_datetime": "2020-03-05 20:00:00",
    }
    """
    ei_intervals = {"not_scheduled": "Now", "run_one_time": "One Time", "scheduled": "Repeat"}
    top_str = center_str = bottom_str = ""
    # From start date, split date and time
    start_datetime = pytz.utc.localize(parser.parse(exec_datetime)).astimezone(pytz.timezone(rule_timezone))
    start_date = start_datetime.strftime("%m/%d/%Y")
    start_hour = start_datetime.strftime("%I:%M %p") # '08:00 PM'

    # --- Job not scheduled, i.e. run now and that is all, we show nothing --- #

    if exec_interval == ei_intervals["not_scheduled"]:
        return ""

    # ----- Job is scheduled to run only one time in a specific date ----- #

    if exec_interval == ei_intervals["run_one_time"]:
        top_str = start_date
        center_str = start_hour
        bottom_str = "DOES NOT REPEAT"
        return top_str + " " + center_str + " " + bottom_str

    # ----- If it is scheduled and should be repeated ----- #

    # Store values of the recurrence_rule rule in a dict
    rrule_values = {'FREQ': None, 'INTERVAL':None, 'UNTIL':None, 'BYMONTHDAY':None, 'BYDAY':None}
    for r in rrule.split(';'):
        key,val = r.split("=",1)
        rrule_values[key] = val

    center_str = start_hour
    until = rrule_values["UNTIL"] and parser.parse(rrule_values["UNTIL"]).strftime("%m/%d/%Y")
    bottom_str = "ENDS ON "+until if until  else "NEVER ENDS"

    top_str = parse_rrule(rrule_values)

    return top_str + " " + center_str + " " + bottom_str



x = create_string("FREQ=WEEKLY;INTERVAL=1;UNTIL=20200320T025959Z;BYDAY=WE,TH","Repeat","2020-03-05 20:00:00","America/Buenos_Aires")
print(x)
