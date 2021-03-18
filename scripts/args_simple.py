"""
The intent of the program above is to modify the case of the Python command line arguments. Three options are available:

-c to capitalize the arguments
-u to convert the arguments to uppercase
-l to convert the argument to lowercase
"""

"""WHEN TO USE AND NOT USE THIS APPROACH
Use:
    For something uncomplicated, the following pattern, which doesn’t enforce ordering and doesn’t handle option-arguments, may be enough

Do Not Use:
    This approach might suffice in many situations, but it would fail in the following cases:
    - If the order is important, and in particular, if options should appear before the arguments
    - If support for option-arguments is needed
    - If some arguments are prefixed with a hyphen (-)

"""

import sys

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-c" in opts:
    print(" ".join(arg.capitalize() for arg in args))
elif "-u" in opts:
    print(" ".join(arg.upper() for arg in args))
elif "-l" in opts:
    print(" ".join(arg.lower() for arg in args))
else:
    raise SystemExit(f"Usage: {sys.argv[0]} (-c | -u | -l) <arguments>...")


# $ python cul.py -c un deux trois
# Un Deux Trois
