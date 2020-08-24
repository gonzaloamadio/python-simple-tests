
 # ref : https://stackoverflow.com/questions/27996448/python-encoding-decoding-problems

def unicodetoascii(text):

    uni2ascii = {
            ord('\xe2\x80\x99'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9d'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9e'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x9f'.decode('utf-8')): ord('"'),
            ord('\xc3\xa9'.decode('utf-8')): ord('e'),
            ord('\xe2\x80\x9c'.decode('utf-8')): ord('"'),
            ord('\xe2\x80\x93'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x92'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x94'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x98'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\x9b'.decode('utf-8')): ord("'"),

            ord('\xe2\x80\x90'.decode('utf-8')): ord('-'),
            ord('\xe2\x80\x91'.decode('utf-8')): ord('-'),

            ord('\xe2\x80\xb2'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb3'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb4'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb5'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb6'.decode('utf-8')): ord("'"),
            ord('\xe2\x80\xb7'.decode('utf-8')): ord("'"),

            ord('\xe2\x81\xba'.decode('utf-8')): ord("+"),
            ord('\xe2\x81\xbb'.decode('utf-8')): ord("-"),
            ord('\xe2\x81\xbc'.decode('utf-8')): ord("="),
            ord('\xe2\x81\xbd'.decode('utf-8')): ord("("),
            ord('\xe2\x81\xbe'.decode('utf-8')): ord(")"),
            ord('\xc2\xb7'.decode('utf-8')): ord(")"),
            }

    return text.decode('utf-8').translate(uni2ascii).encode('ascii')

print unicodetoascii("be embedded in other programs. We recommend to review the value of the profile parameters \xe2\x80\x98sapgui/user_scripting\xe2\x80\x99 and")

def unicodetoascii2(text):

    TEXT = (text.
    		replace('\\xe2\\x80\\x99', "'").
            replace('\\xc3\\xa9', 'e').
            replace('\\xe2\\x80\\x90', '-').
            replace('\\xe2\\x80\\x91', '-').
            replace('\\xe2\\x80\\x92', '-').
            replace('\\xe2\\x80\\x93', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x94', '-').
            replace('\\xe2\\x80\\x98', "'").
            replace('\\xe2\\x80\\x9b', "'").
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9c', '"').
            replace('\\xe2\\x80\\x9d', '"').
            replace('\\xe2\\x80\\x9e', '"').
            replace('\\xe2\\x80\\x9f', '"').
            replace('\\xe2\\x80\\xa6', '...').
            replace('\\xe2\\x80\\xb2', "'").
            replace('\\xe2\\x80\\xb3', "'").
            replace('\\xe2\\x80\\xb4', "'").
            replace('\\xe2\\x80\\xb5', "'").
            replace('\\xe2\\x80\\xb6', "'").
            replace('\\xe2\\x80\\xb7', "'").
            replace('\\xe2\\x81\\xba', "+").
            replace('\\xe2\\x81\\xbb', "-").
            replace('\\xe2\\x81\\xbc', "=").
            replace('\\xe2\\x81\\xbd', "(").
            replace('\\xe2\\x81\\xbe', ")")

                 )
    return TEXT

print unicodetoascii2("be embedded in other programs.  We recommend to review the value of the profile parameters \xe2\x80\x98sapgui/user_scripting\xe2\x80\x99 and")


"""The 'problem' with the last two approaches, is that it is not exhaustive.

Alternatives:
    1) Make it exhaustive according to this table : : https://www.utf8-chartable.de/unicode-utf8-table.pl?start=8192&number=128&utf8=string-literal
    2) Ignore not ascii characters
"""

# Python 2 REF: https://docs.python.org/2/howto/unicode.htm
# unicode, encode, decode

## Encoding
#
# https://stackoverflow.com/questions/15321138/removing-unicode-u2026-like-characters-in-a-string-in-python2-7?noredirect=1&lq=1
# Python 2.x
s = 'This is some \\u03c0 text that has to be cleaned\\u2026! it\\u0027s annoying!'
print(s.decode('unicode_escape').encode('ascii','ignore'))
print(unicode(s, errors='ignore').encode("ascii"))
#This is some  text that has to be cleaned! it's annoying!

# >>> s = 'This is some \\u03c0 text that has to be cleaned\\u2026! it\\u0027s annoying!'
# >>> s.decode('unicode_escape')
# u"This is some \u03c0 text that has to be cleaned\u2026! it's annoying!"
# >>> "be embedded in other programs.  We recommend to review the value of the profile parameters \xe2\x80\x98sapgui/user_scripting\xe2\x80\x99 and".decode('unicode_escape')
# u'be embedded in other programs.  We recommend to review the value of the profile parameters \xe2\x80\x98sapgui/user_scripting\xe2\x80\x99 and'
# >>> 'be embedded in other programs.  We recommend to review the value of the profile parameters \\xe2\\x80\\x98sapgui/user_scripting\\xe2\\x80\\x99 and'.decode('unicode_escape')
# u'be embedded in other programs.  We recommend to review the value of the profile parameters \xe2\x80\x98sapgui/user_scripting\xe2\x80\x99 and'


# Python 3.x
s = 'This is some \u03c0 text that has to be cleaned\u2026! it\u0027s annoying!'
print(s.encode('ascii', 'ignore'))
# b"This is some  text that has to be cleaned! it's annoying!"

## Printable
#
# REF: https://stackoverflow.com/questions/8689795/how-can-i-remove-non-ascii-characters-but-leave-periods-and-spaces-using-python?noredirect=1&lq=1
s = "some\x00string. with\x15 funny characters"
import string
# printable characters are: asccii, puntcutation
printable = set(string.printable)
print(filter(lambda x: x in printable, s))
#'somestring. with funny characters'

## Regex
#
# REF: https://stackoverflow.com/questions/40872126/python-replace-non-ascii-character-in-string/40872225
a = "hi »"
import re
print(re.sub(r'[^\x00-\x7f]',r'', 'hi »'))
#'hi '
