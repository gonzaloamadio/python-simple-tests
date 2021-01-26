"""
As we know, the json module provides two methods to parse JSON data using Python.

json.loads(): To parse JSON from String.
json.load() to Parse JSON from a file.

Both methods will throw a ValueError if the string or data you pass can’t
be decoded as JSON. When we receive a JSON response,
we can pass it to the json.loads() method to validate it as per the standard convention
"""
import json

def validateJSON_string(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

InvalidJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com",}"""
isValid = validateJSON_string(InvalidJsonData)
print("Given JSON string is Valid", isValid)

validJsonData = """{"name": "jane doe", "salary": 9000, "email": "jane.doe@pynative.com"}"""
isValid = validateJSON_string(validJsonData)
print("Given JSON string is Valid", isValid)


def validateJSON_file(file_path):
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
    except ValueError as err:
        return False
    return True

isValid = validateJSON_file("data_err.txt")
print("Given JSON string is Valid", isValid)

isValid = validateJSON_file("data_ok.txt")
print("Given JSON string is Valid", isValid)
