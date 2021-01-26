"""
Sometimes we need something extra than just a standard JSON validation. i.e.,
We will see how to validate incoming JSON data by checking all necessary fields present
in JSON file or response and also validate data types of those fields.

Such a scenario includes the following things:

We need the necessary fields present in JSON file
We need data of a JSON filed in a type that we want. For example, we want all numeric fields
in the number format instead of number encoded in a string format like this Marks: "75"
so we can use it directly instead of checking and converting it every time.
We need to use the jsonschema library. This library is useful for validating JSON data.
The library uses the format to make validations based on the given schema. jsonschema
is an implementation of JSON Schema for Python.

Using jsonschema, we can create a schema of our choice, so every time we can validate the
JSON document against this schema, if it passed, we could say that the JSON document is valid.

Follow the below steps:

* First, install jsonschema using pip command. pip install jsonschema
* Define Schema: Describe what kind of JSON you expect
* Convert JSON to Python Object using json.load or json.loads methods.
* Pass resultant JSON to validate() method of a jsonschema. This method will raise an exception
if given json is not what is described in the schema.

Let’s see the example. In this example, I am validating student JSON. The following conditions
must meet to call it as a valid JSON

* The student name and roll number must be present in JSON data.
* Marks and roll number must be in a number format.
"""
import json
import os
import jsonschema
from jsonschema import validate

# Describe what kind of json you expect.
studentSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rollnumber": {"type": "number"},
        "marks": {"type": "number"},
    },
}

def validateJson(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        print(err)
        return False
    return True

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber": "25", "marks": 72}')
# validate it
isValid = validateJson(jsonData, studentSchema)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

# Convert json to python object.
jsonData = json.loads('{"name": "jane doe", "rollnumber": 25, "marks": 72}')
# validate it
isValid = validateJson(jsonData, studentSchema)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")

print("############################################################################")

with_id_schema = {
    "type": "object",
    "properties": {
        "pending": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "exp": {"type": "string"}
                }
            }
        },
    },
}

jsonData = json.loads('{"pending": [{"id": "id_1", "exp": "asd"}, {"id":"id2", "exp": "asd"}]}')

isValid = validateJson(jsonData, with_id_schema)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")


jsonData = json.loads('{"pending": [{"id": 2, "exp": "asd"}, {"id":"id2", "exp": "asd"}]}')
isValid = validateJson(jsonData, with_id_schema)
if isValid:
    print(jsonData)
    print("Given JSON data is Valid")
else:
    print(jsonData)
    print("Given JSON data is InValid")


print("############################################################################")

# id we do not put additionalproperties, that data will be valid
json_schema = {
    "type": "object",
    "properties": {
        "pending_bris": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "expiration_date": {"type": "string"}
                }
            },
            "additionalProperties" : False
        },
    },
    "additionalProperties" : False
}

if os.path.exists("data_ok.txt"):
    with open("data_ok.txt") as json_file:
        data = json.load(json_file)
        if validateJson(data, json_schema):
            print("valid")
        else:
            print("Invalid JSON Data.")
