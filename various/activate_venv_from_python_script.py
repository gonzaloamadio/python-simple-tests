#!/home/gamadio/.virtualenvs/py3.7/bin/python

activate_this = "/home/gamadio/.virtualenvs/py3.7/bin/activate_this.py"
with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))

import sys
import pytest
# If we import here something that is not installed in venv, will fail

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Virtualenv test</title>')
print ('</head>')
print ('<body>')
print ('<h3>If you see this, the module import was successful</h3>')
print (sys.version)
print ('</body>')
print ('</html>')

# REF: https://www.a2hosting.com/kb/developer-corner/python/activating-a-python-virtual-environment-from-a-script-file
