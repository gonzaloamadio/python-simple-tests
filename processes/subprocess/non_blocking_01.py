import sys
import time
import subprocess
from subprocess import PIPE, Popen
from threading  import Thread

try:
    from queue import Queue, Empty
except ImportError:
    from Queue import Queue, Empty  # python 2.x

ON_POSIX = 'posix' in sys.builtin_module_names

def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()

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
proc = Popen(parameters, stdout=PIPE, stderr=subprocess.STDOUT, universal_newlines=True, bufsize=1, close_fds=ON_POSIX)

#proc = Popen(['myprogram.exe'], stdout=PIPE, bufsize=1, close_fds=ON_POSIX)
q = Queue()
t = Thread(target=enqueue_output, args=(proc.stdout, q))
t.daemon = True # thread dies with the program
t.start()

# ... do other things here

# read line without blocking
while True:
    time.sleep(4)
    try:  line = q.get_nowait() # or q.get(timeout=.1)
    except Empty:
        print('no output yet')
    else: # got line
        print(f"Tengo linea --> {line}")
        # ... do something with line

############# OUT

#Tengo linea --> POST https://testasd.com/
#no output yet
#no output yet
#no output yet
#no output yet
#no output yet
#Tengo linea --> Failed to connect to 3.223.115.185:443: Connection timed out
#Tengo linea --> Failed to connect to host testasd.com
#Tengo linea --> Failed to open HTTPS connection to testasd.com
#Tengo linea --> Failed to obtain WebVPN cookie
#Tengo linea -->
#Tengo linea -->
#Tengo linea -->

