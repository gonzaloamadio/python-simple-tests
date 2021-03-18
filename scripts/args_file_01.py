# sha1sum_file.py

import hashlib
import sys

def sha1sum(filename: str) -> str:
    hash = hashlib.sha1()
    with open(filename, mode="rb") as f:
        hash.update(f.read())
    return hash.hexdigest()

for arg in sys.argv[1:]:
    print(f"{sha1sum(arg)}  {arg}")


"""
This will only work fine on linux, if we use exapand arguments, for example:

    $ python main.py main.*
Arguments count: 5
Argument      0: main.py
Argument      1: main.c
Argument      2: main.exe
Argument      3: main.obj
Argument      4: main.py

That wont work on windows.

For cross platform, see args_file_02.py
"""
