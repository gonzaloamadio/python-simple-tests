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
for line in proc.stdout:
    print(f"Line: {line}")
proc.stdout.flush()

import pdb;pdb.set_trace()

out = proc.stdout.readline()
print(f"len de out: {len(out)}")
print(f"Out: {out}")

################# OUT:

#Line: b'POST https://testasd.com/\n'
#Line: b'Failed to connect to 3.223.115.185:443: Connection timed out\n'
#Line: b'Failed to connect to host testasd.com\n'
#Line: b'Failed to open HTTPS connection to testasd.com\n'
#Line: b'Failed to obtain WebVPN cookie\n'
#> /tmp/oc.py(35)<module>()
#-> out = proc.stdout.readline()
#(Pdb) l

