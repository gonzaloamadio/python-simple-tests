import subprocess
from subprocess import PIPE, Popen, TimeoutExpired


server_url = "testasd.com"
#server_url = "ec2-3-223-150-210.compute-1.amazonaws.com"
certificate = "~/Downloads/client.crt"
ca_file = "~/Downloads/ca.crt"
parameters = [
    "openconnect",
    server_url,
    "--certificate",
    certificate,
    "--cafile",
    ca_file,
]

# universal_newlines=True  --> Return as str, not as bytes
proc = Popen(parameters, stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
print("ASd")
# This blocks until finish and return all the output
output, errors = proc.communicate()

import pdb;pdb.set_trace()


################# OUT:

ASd
#              <-- Some time has passed here
--Return--
> /home/gamadio/Playground/python-simple-tests/processes/subprocess/02.py(23)<module>()->None
-> import pdb;pdb.set_trace()
(Pdb) l
 18  	# universal_newlines=True  --> Return as str, not as bytes
 19  	proc = Popen(parameters, stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
 20  	print("ASd")
 21  	output, errors = proc.communicate()
 22
 23  ->	import pdb;pdb.set_trace()
 24
 25
 26  	################# OUT:
 27
 28  	#Line: b'POST https://testasd.com/\n'
(Pdb) output
'POST https://testasd.com/\nFailed to connect to 3.223.115.185:443: Connection timed out\nFailed to connect to host testasd.com\nFailed to open HTTPS connection to testasd.com\nFailed to obtain WebVPN cookie\n'
(Pdb) errors
(Pdb)

