import imp
import inspect
import sys
import example

# REF: https://pymotw.com/2/inspect/

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = 'example.py'

# Pass a filename as the only argument, and the return value is a tuple
# including the module base name, the suffix of the file, the mode  that will
# be used for reading the file, and the module type as defined in the imp module
#  It is important to note that the function looks only at the file’s name,
# and does not actually check if the file exists or try to read the file.

print("------------ getmoduleinfo ------------")

try:
    (name, suffix, mode, mtype)  = inspect.getmoduleinfo(filename)
except TypeError:
    print('Could not determine module type of %s' % filename)
else:
    mtype_name = { imp.PY_SOURCE:'source',
                   imp.PY_COMPILED:'compiled',
                   }.get(mtype, mtype)

    mode_description = { 'rb':'(read-binary)',
                         'U':'(universal newline)',
                         }.get(mode, '')

    print('NAME   :', name)
    print('SUFFIX :', suffix)
    print('MODE   :', mode, mode_description)
    print('MTYPE  :', mtype_name)

print("------------ getmembers ------------")


# The arguments to getmembers() are an object to scan (a module, class, or
# instance) and an optional predicate function that is used to filter the objects
# returned. The return value is a list of tuples with 2 values: the name of the
# member, and the type of the member. The inspect module includes several such
# predicate functions with names like ismodule(), isclass(), etc.
# You can provide your own predicate function as well.

for name, data in inspect.getmembers(example):
    if name == '__builtins__':
        continue
    print('%s :' % name, repr(data))


# Output:

"""
------------ getmoduleinfo ------------
NAME   : example
SUFFIX : .py
MODE   : U (universal newline)
MTYPE  : source
------------ getmembers ------------
A : <class 'example.A'>
B : <class 'example.B'>
__doc__ : 'Sample file to serve as the basis for inspect examples.\n'
__file__ : '/home/gamadio/Playground/python-simple-tests/runtime-and-debug/example.pyc'
__name__ : 'example'
__package__ : None
instance_of_a : <example.A object at 0x7f378de86c90>
module_level_function : <function module_level_function at 0x7f378de9ab50>
"""

for name, data in inspect.getmembers(example, inspect.isclass):
    print('%s :' % name, repr(data))
# A : <class 'example.A'>
# B : <class 'example.B'>


################################################################################

# If we do not ignore builtins, we would have also:

"""
__builtins__ : {'bytearray': <type 'bytearray'>,
                'IndexError': <type 'exceptions.IndexError'>,
                'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object.,
                'vars': <built-in function vars>,
                'SyntaxError': <type 'exceptions.SyntaxError'>,
                'unicode': <type 'unicode'>,
                'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, .....
All Rights Reserved.Copyright (c) 2000 BeOpen.com. All Rights Reserved.,
    'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>,
    'dict': <type 'dict'>,
    'input': <built-in function input>,
    'oct': <built-in function oct>,
    'bin': <built-in function bin>,
    .... and a lot more.
"""
