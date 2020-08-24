MAX_ELEMENT_NAME_LENGTH = 30
import re

def truncate_and_lower(input, length=MAX_ELEMENT_NAME_LENGTH):
    """
    Truncate input to length and lower case it.
    If input is not string, returns ''.
    :param input: string
    :return: string
    """
    if not isinstance(input, str):
        return ''
    input = re.sub(' +', ' ', input)
    return input[:length].strip().lower()

def create_prefix_name_with_two_elements(str1, str2):
    """

    :param str1:string First element of a report prefix_name
    :param str2:string Second element of a report prefix_name
    :return: A string with length of at most MAX_ELEMENT_NAME_LENGTH, and evenly truncated strings
    """
    half_max_length = MAX_ELEMENT_NAME_LENGTH // 2
    if len(str2) > half_max_length >= len(str1):
        # the last -1 is for the _ in the middle of the name
        str2 = truncate_and_lower(str2, length=MAX_ELEMENT_NAME_LENGTH - len(str1) - 1)
    elif len(str1) > half_max_length >= len(str2):
        str1 = truncate_and_lower(str1, length=MAX_ELEMENT_NAME_LENGTH - len(str2) - 1)
    elif half_max_length < len(str2) and half_max_length < len(str1):
        print("ENTRE")
        str1 = truncate_and_lower(str1, length=MAX_ELEMENT_NAME_LENGTH // 2)
        str2 = truncate_and_lower(str2, length=MAX_ELEMENT_NAME_LENGTH // 2)
    return f"{str1.strip()}_{str2.strip()}"

x = create_prefix_name_with_two_elements("this should  be   lower case eee", 'THIS SHOULD  BE   LOWER CASE EEE')
print(x)
x = create_prefix_name_with_two_elements("this should    be lower case eee", 'THIS SHOULD BE LOWER   CASE EEE')
print(x)
