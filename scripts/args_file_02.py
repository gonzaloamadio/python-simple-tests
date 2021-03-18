import sys
import glob
import itertools
from typing import List

def expand_args(args: List[str]) -> List[str]:
    arguments = args[:1]
    glob_args = [glob.glob(arg) for arg in args[1:]]
    arguments += itertools.chain.from_iterable(glob_args)
    return arguments

if __name__ == "__main__":
    args = expand_args(sys.argv)
    print(f"Arguments count: {len(args)}")
    for i, arg in enumerate(args):
        print(f"Argument {i:>6}: {arg}")

"""
Using glob make * flag works on windows too.

Ref: https://realpython.com/python-command-line-arguments/

"""
