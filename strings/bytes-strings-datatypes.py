# https://www.w3resource.com/python/python-bytes.php

>>> y = b'Python bytes'
>>> list(y)
[80, 121, 116, 104, 111, 110, 32, 98, 121, 116, 101, 115]
>>> y = 'Python bytes'
>>> list(y)
['P', 'y', 't', 'h', 'o', 'n', ' ', 'b', 'y', 't', 'e', 's']


# String datataype : https://www.w3resource.com/python/python-string.php
# String formatting : https://www.w3resource.com/python/python-format.php


>>> print(len(“你好”))   # Python 2 - str is bytes
6
>>> print(len(u“你好”))  # Python 2 - Add 'u' for unicode code points
2
>>> print(len(“你好”))   # Python 3 - str is unicode code points
2
# strings is by default made of unicode code points
>>> print(len(“你好”))
2
# Manually encode a string into bytes
>>> print(len(("你好").encode("utf-8")))
6
# You don't need to pass an argument as default encoding is "utf-8"
>>> print(len(("你好").encode()))
6
# Print actual unicode code points instead of characters [Source]
>>> print(("你好").encode("unicode_escape"))
b'\\u4f60\\u597d'
# Print bytes encoded in UTF-8 for this string
>>> print(("你好").encode())
b'\xe4\xbd\xa0\xe5\xa5\xbd'


>>> "résumé".encode("utf-8")
b'r\xc3\xa9sum\xc3\xa9'
>>> "El Niño".encode("utf-8")
b'El Ni\xc3\xb1o'

>>> b"r\xc3\xa9sum\xc3\xa9".decode("utf-8")
'résumé'
>>> b"El Ni\xc3\xb1o".decode("utf-8")
'El Niño'

# The results of str.encode() is a bytes object. Both bytes literals
# (such as b"r\xc3\xa9sum\xc3\xa9") and the representations of bytes permit only ASCII characters.

# This is why, when calling "El Niño".encode("utf-8"), the ASCII-compatible
# "El" is allowed to be represented as it is, but the n with tilde is escaped to
# "\xc3\xb1". That messy-looking sequence represents two bytes, 0xc3 and 0xb1 in hex
