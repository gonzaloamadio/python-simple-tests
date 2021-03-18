import re


MAX_FILENAME_LENGTH = 64


def _sanitize_name(input, length=None):
    """
    Sanitize input string to be used as filename replacing ' ' by '_' and removing every char but '-', '.' and word
    chars '\w' # noqa: W605
    :param input: string to be sanitized.
    :param length: truncate the resulting string to the provided length. Defaults to not truncate.
    :return: string
    """
    s = input.strip().replace(' ', '_')
    s = re.sub(r'(?u)[^-\w.]', '', s)
    return s[:length]


def get_valid_name(input, length=MAX_FILENAME_LENGTH):
    """
    Return the given string converted to a string that can be used for a clean
    filename. Remove leading and trailing spaces; convert other spaces to
    underscores; and remove anything that is not an alphanumeric, dash,
    underscore, or dot. Finally file name is trimmed to a max of length characters.
    :param input: string to be converted, it assumes to be a filename with extension.
    :param length: truncate the resulting string to the provided length. Default MAX_FILENAME_LENGTH
    :return: string
    """
    s = _sanitize_name(input)
    try:
        name, ext = s.rsplit('.', 1)
        name = name[:length - len(ext) - 1]
    except ValueError:
        # there is no extension in the filename. Returns it directly trimmed.
        return s[:length]
    return '{}.{}'.format(name, ext)

