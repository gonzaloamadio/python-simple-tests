import re
import string
import random

MAX_NAME_LENGTH=63
RAND_NUMBER_LENGTH=15


def _sanitize_subdomain_name(input, length=None):
    """
    Sanitize input string to be used as name replacing ' ', '.', '_' by '-' and removing every char but '-', and word
    chars '\w' # noqa: W605

    According to the pertinent internet recommendations (RFC3986 section 2.2, which in turn refers to:
    RFC1034 section 3.5 and RFC1123 section 2.1), a subdomain must meet several requirements:
    - Each subdomain part must have a length no greater than 63.
    - Each subdomain part must begin and end with an alpha-numeric (i.e. letters [A-Za-z] or digits [0-9]).
    - Each subdomain part may contain hyphens (dashes), but may not begin or end with a hyphen.

    :param input: string to be sanitized.
    :param length: truncate the resulting string to the provided length. Defaults to not truncate.
    :return: string
    """
    s = input.strip().replace(' ', '-')
    s = '{}'.format(s[1:] if s.startswith('-') else s)
    s = '{}'.format(s[:-1] if s.endswith('-') else s)
    s = s.replace('.', '-')
    s = s.replace('_', '-')
    s = re.sub(r'(?u)[^-\w]', '', s)
    return s[:length]


def get_valid_subdomain(input, length=MAX_NAME_LENGTH):
    """
    Return the given string converted to a string that can be used for a clean
    subdomain name. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot. Finally file name is trimmed to a max of length characters.

    :param input: string to be converted
    :param length: truncate the resulting string to the provided length. Default MAX_NAME_LENGTH
    :return: string
    """
    return _sanitize_subdomain_name(input, length=length)


def generate_subdomain(name=None):
    # In the case the name is almost max allowed subdomain length, cut it to add randomness anyway
    name = (name and name[:MAX_NAME_LENGTH-RAND_NUMBER_LENGTH]) or ""
    random_digits = get_rand_digits()
    return get_valid_subdomain(f"{name}-{random_digits}")


def get_rand_digits(length=RAND_NUMBER_LENGTH):
    return ''.join(random.choice(string.digits) for x in range(length))


print(generate_subdomain())
print(generate_subdomain("abc"))
print(generate_subdomain("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
print(generate_subdomain("bbbbbbbbbbbbbbbb"))
print(generate_subdomain("-bbbbbbbbbbbbbbbb-"))
print(generate_subdomain("bbbbbbbbb bbbbbbb"))
print(generate_subdomain("bbbbb.bb$%&)bbbbbbbbb"))


