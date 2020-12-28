
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def foo(table):
    p = Point(11, y=22)
    table["asd"] = p

table = {}

foo(table)

print(table)
print(table["asd"].x)

##########
print("----------------------")

File_Mapping = namedtuple('File_Mapping', ['unencrypted_file', 'json_report'])

def file_correspondence_registry(table_object, encrypted_path, unencrypted_path=None, json_report_path=None):
    """
    Keep track of which .ext encrypted file is associated with unencrypted file and json report.
    """
    val = table_object.setdefault(encrypted_path, File_Mapping(unencrypted_file=None, json_report=None))
    if unencrypted_path:
        table_object[encrypted_path] = val._replace(unencrypted_file=unencrypted_path)
    if json_report_path:
        table_object[encrypted_path] = val._replace(json_report=json_report_path)


table = {}

path="PD/name.ext"
file_correspondence_registry(table, "PD/name.ext", unencrypted_path="IN/name.ext")
file_correspondence_registry(table, "PD/name.ext", json_report_path="OUT/name.ext")

print(table)
print(table[path].json_report)

##############################
print("----------------------")

def foo2(table):
    Point2 = namedtuple('Point', ['x', 'y'])
    p = Point2(111, y=222)
    table["asd"] = p

table = {}
foo2(table)
print(table)
print(table["asd"].x)


##############################
print("----------------------")

def foo3():
    Point3 = namedtuple('Point', ['x', 'y'])
    p = Point3(111, y=222)
    return[p]

for point in foo3():
    print(point.x, point.y)


#{'asd': Point(x=11, y=22)}
#11
#----------------------
#{'PD/name.ext': File_Mapping(unencrypted_file='IN/name.ext', json_report='OUT/name.ext')}
#OUT/name.ext
#----------------------
#{'asd': Point(x=111, y=222)}
#111
#----------------------
#(111, 222)

