import inspect
from pprint import pprint

import example

pprint(inspect.getmembers(example.A))

"""
[('__class__', <type 'type'>),
 ('__delattr__', <slot wrapper '__delattr__' of 'object' objects>),
 ('__dict__',
  dict_proxy({'__module__': 'example', 'get_name': <function get_name at 0x7f1bf0153f50>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': 'The A class.', '__init__': <function __init__ at 0x7f1bf0153ed0>})),
 ('__doc__', 'The A class.'),
 ('__format__', <method '__format__' of 'object' objects>),
 ('__getattribute__', <slot wrapper '__getattribute__' of 'object' objects>),
 ('__hash__', <slot wrapper '__hash__' of 'object' objects>),
 ('__init__', <unbound method A.__init__>),
 ('__module__', 'example'),
 ('__new__', <built-in method __new__ of type object at 0x555cbcb32980>),
 ('__reduce__', <method '__reduce__' of 'object' objects>),
 ('__reduce_ex__', <method '__reduce_ex__' of 'object' objects>),
 ('__repr__', <slot wrapper '__repr__' of 'object' objects>),
 ('__setattr__', <slot wrapper '__setattr__' of 'object' objects>),
 ('__sizeof__', <method '__sizeof__' of 'object' objects>),
 ('__str__', <slot wrapper '__str__' of 'object' objects>),
 ('__subclasshook__',
  <built-in method __subclasshook__ of type object at 0x555cbe4e5bb0>),
 ('__weakref__', <attribute '__weakref__' of 'A' objects>),
 ('get_name', <unbound method A.get_name>)]
"""

pprint(inspect.getmembers(example.A, inspect.ismethod))

# [('__init__', <unbound method A.__init__>),
#  ('get_name', <unbound method A.get_name>)]

pprint(inspect.getmembers(example.B, inspect.ismethod))

