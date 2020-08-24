


" · We recommend to review the value of the"

"""
if we execute this file with python2, we will obtain the following error:

└──> python2 non-ascii-in-file-err.py
  File "non-ascii-in-file-err.py", line 5
SyntaxError: Non-ASCII character '\xc2' in file non-ascii-in-file-err.py on line 5, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

This is because of the first character in the string, the dot in the middle of the line. -->  ·

With python3, we do not have this error, utf-8 is the default encodign

SOLUTION:
    write this as the first line of the file:

# -*- coding: utf-8 -*-

"""

