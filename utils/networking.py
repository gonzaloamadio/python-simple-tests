############ PING
# shebang does not work over all platforms
# ping.py  2016-02-25 Rudolf
# subprocess.call() is preferred to os.system()
# works under Python 2.7 and 3.4
# works under Linux, Mac OS, Windows

def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = platform.system().lower()!="windows"

    # Ping
    return subprocess.call(args, shell=need_sh, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) == 0

# test call
#print(ping("192.168.17.142"))
print(ping("192.168.1.46"))
#output = ping("192.168.17.142")
#print("output is: " + str(output))
