""" Show an example of how we can map and keep a registry of associated data.

Also do the same with different data structures
"""
from pprint import pprint
ex1 = ("/encrypted/encr1", "/in/unencr1", "/out/json1")
ex2 = ("/encrypted/encr2", "/in/unencr2", "/out/json2")
ex3 = ("/encrypted/encr3", "/in/unencr3", "/out/json3")



print("\n###################### Example with name tuples ######################\n")

from collections import namedtuple

File_Mapping = namedtuple('File_Mapping', ['unencrypted_file', 'json_report'])

def file_correspondence_registry(table_object, encrypted_path, unencrypted_path=None, json_report_path=None):
    """
    Keep track of which encrypted file is associated with unencrypted file and json report.
    """
    val = table_object.setdefault(encrypted_path, File_Mapping(unencrypted_file=None, json_report=None))
    if unencrypted_path:
        # Replace return a new value
        new_val = table_object[encrypted_path]._replace(unencrypted_file=unencrypted_path)
        table_object[encrypted_path] = new_val
    if json_report_path:
        new_value = table_object[encrypted_path]._replace(json_report=json_report_path)
        table_object[encrypted_path] = new_value


table = {}
for obj in [ex1, ex2, ex3]:
    file_correspondence_registry(table, obj[0], obj[1], obj[2])
pprint(table)
print("Unencrypted file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].unencrypted_file)
print("Json report file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].json_report)




print("\n################ Example with recordclass ##############################\n")

# It is not core python, you have to install a library
# https://pypi.org/project/recordclass/

from recordclass import recordclass

File_Mapping = recordclass('File_Mapping', ['unencrypted_file', 'json_report'])

def file_correspondence_registry(table_object, encrypted_path, unencrypted_path=None, json_report_path=None):
    """
    Keep track of which encrypted file is associated with unencrypted file and json report.
    """
    val = table_object.setdefault(encrypted_path, File_Mapping(unencrypted_file=None, json_report=None))
    if unencrypted_path:
        val.unencrypted_file = unencrypted_path
    if json_report_path:
        val.json_report = json_report_path


table = {}
for obj in [ex1, ex2, ex3]:
    file_correspondence_registry(table, obj[0], obj[1], obj[2])
pprint(table)
print("Unencrypted file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].unencrypted_file)
print("Json report file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].json_report)


print("\n################ Example with SimpleNamspace #############################\n")

# https://docs.python.org/3/library/types.html#types.SimpleNamespace
# Python > 3.3

from types import SimpleNamespace

def file_correspondence_registry(table_object, encrypted_path, unencrypted_path=None, json_report_path=None):
    sn = SimpleNamespace(unencrypted_file=None, json_report=None)
    val = table_object.setdefault(encrypted_path, sn)
    if unencrypted_path:
        val.unencrypted_file = unencrypted_path
    if json_report_path:
        val.json_report = json_report_path

table = {}
for obj in [ex1, ex2, ex3]:
    file_correspondence_registry(table, obj[0], obj[1], obj[2])
pprint(table)
print("Unencrypted file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].unencrypted_file)
print("Json report file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].json_report)


print("\n################ Example with Dataclass #############################\n")
# Python > 3.7

from dataclasses import dataclass
@dataclass
class File_Mapping:
    unencrypted_file: str
    json_report: str

def file_correspondence_registry(table_object, encrypted_path, unencrypted_path=None, json_report_path=None):
    val = table_object.setdefault(encrypted_path, File_Mapping(unencrypted_file=None, json_report=None))
    if unencrypted_path:
        val.unencrypted_file = unencrypted_path
    if json_report_path:
        val.json_report = json_report_path

table = {}
for obj in [ex1, ex2, ex3]:
    file_correspondence_registry(table, obj[0], obj[1], obj[2])
pprint(table)
print("Unencrypted file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].unencrypted_file)
print("Json report file corresponding to /encrypted/encr3")
print(table["/encrypted/encr3"].json_report)


"""
python keep_track_associated_files.py

###################### Example with name tuples ######################

{'/encrypted/encr1': File_Mapping(unencrypted_file='/in/unencr1', json_report='/out/json1'),
 '/encrypted/encr2': File_Mapping(unencrypted_file='/in/unencr2', json_report='/out/json2'),
 '/encrypted/encr3': File_Mapping(unencrypted_file='/in/unencr3', json_report='/out/json3')}
Unencrypted file corresponding to /encrypted/encr3
/in/unencr3
Json report file corresponding to /encrypted/encr3
/out/json3

################ Example with recordclass ##############################

{'/encrypted/encr1': File_Mapping(unencrypted_file='/in/unencr1', json_report='/out/json1'),
 '/encrypted/encr2': File_Mapping(unencrypted_file='/in/unencr2', json_report='/out/json2'),
 '/encrypted/encr3': File_Mapping(unencrypted_file='/in/unencr3', json_report='/out/json3')}
Unencrypted file corresponding to /encrypted/encr3
/in/unencr3
Json report file corresponding to /encrypted/encr3
/out/json3

################ Example with SimpleNamspace #############################

{'/encrypted/encr1': namespace(json_report='/out/json1', unencrypted_file='/in/unencr1'),
 '/encrypted/encr2': namespace(json_report='/out/json2', unencrypted_file='/in/unencr2'),
 '/encrypted/encr3': namespace(json_report='/out/json3', unencrypted_file='/in/unencr3')}
Unencrypted file corresponding to /encrypted/encr3
/in/unencr3
Json report file corresponding to /encrypted/encr3
/out/json3

################ Example with Dataclass #############################

{'/encrypted/encr1': File_Mapping(unencrypted_file='/in/unencr1', json_report='/out/json1'),
 '/encrypted/encr2': File_Mapping(unencrypted_file='/in/unencr2', json_report='/out/json2'),
 '/encrypted/encr3': File_Mapping(unencrypted_file='/in/unencr3', json_report='/out/json3')}
Unencrypted file corresponding to /encrypted/encr3
/in/unencr3
Json report file corresponding to /encrypted/encr3
/out/json3
"""
