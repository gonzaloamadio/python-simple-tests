# YOU WONT BE DOING THIS, USE ARGPARSE OR DOCOPT

"""
Print integers from <first> to <last>, in steps of <increment>.

Usage:
  python seq.py --help
  python seq.py [-s SEPARATOR] <last>
  python seq.py [-s SEPARATOR] <first> <last>
  python seq.py [-s SEPARATOR] <first> <increment> <last>

Mandatory arguments to long options are mandatory for short options too.
  -s, --separator=STRING use STRING to separate numbers (default: \n)
      --help             display this help and exit

If <first> or <increment> are omitted, they default to 1. When <first> is
larger than <last>, <increment>, if not set, defaults to -1.
The sequence of numbers ends when the sum of the current number and
<increment> reaches the limit imposed by <last>.
"""

"""WHEN TO USE AND NOT USE THIS APPROACH

Use:
    You can use a regular expression to enforce a certain order, specific options and option-arguments, or even the type of arguments.
"""

""" NOTE:
If this is not too complex, we can implement a custom parser:

def parse(args: List[str]) -> Tuple[str, List[int]]:
    arguments = collections.deque(args)
    separator = "\n"
    operands: List[int] = []
    while arguments:
        arg = arguments.popleft()
        if not operands:
            if arg == "--help":
                print(USAGE)
                sys.exit(0)
            if arg in ("-s", "--separator"):
                separator = arguments.popleft()
                continue
        try:
            operands.append(int(arg))
        except ValueError:
            raise SystemExit(USAGE)
        if len(operands) > 3:
            raise SystemExit(USAGE)

    return separator, operands

"""
import re

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)

"""
1) A help option, in short (-h) or long format (--help), captured as a named group called HELP
2) A separator option, -s or --separator, taking an optional argument, and captured as named group called SEP
3) Up to three integer operands, respectively captured as OP1, OP2, and OP3

For clarity, the pattern args_pattern above uses the flag re.VERBOSE on line 11.
This allows you to spread the regular expression over a few lines to enhance readability.
The pattern validates the following:

1) Argument order: Options and arguments are expected to be laid out in a given order. For example, options are expected before the arguments.
2) Option values**: Only --help, -s, or --separator are expected as options.
3) Argument mutual exclusivity: The option --help isn’t compatible with other options or arguments.
4) Argument type: Operands are expected to be positive or negative integers.
"""

from typing import List, Dict
import re
import sys

USAGE = (
    f"Usage: {sys.argv[0]} [-s <separator>] [first [increment]] last"
)

args_pattern = re.compile(
    r"""
    ^
    (
        (--(?P<HELP>help).*)|
        ((?:-s|--separator)\s(?P<SEP>.*?)\s)?
        ((?P<OP1>-?\d+))(\s(?P<OP2>-?\d+))?(\s(?P<OP3>-?\d+))?
    )
    $
""",
    re.VERBOSE,
)

# Given the pattern args_pattern above, you can extract the Python command line arguments with the following function:
"""
The dictionary includes the names of each group as keys and their respective values.
For example, if the arg_line value is --help, then the dictionary is {'HELP': 'help'}.
If arg_line is -s T 10, then the dictionary becomes {'SEP': 'T', 'OP1': '10'}.
You can expand the code block below to see an implementation of seq with regular expressions.
"""
def parse(arg_line: str) -> Dict[str, str]:
    args: Dict[str, str] = {}
    if match_object := args_pattern.match(arg_line):
        args = {k: v for k, v in match_object.groupdict().items()
                if v is not None}
    return args

def seq(operands: List[int], sep: str = "\n") -> str:
    first, increment, last = 1, 1, 1
    if len(operands) == 1:
        last = operands[0]
    if len(operands) == 2:
        first, last = operands
        if first > last:
            increment = -1
    if len(operands) == 3:
        first, increment, last = operands
    last = last + 1 if increment > 0 else last - 1
    return sep.join(str(i) for i in range(first, last, increment))

def main() -> None:
# For the regular expression to be able to handle these things, it needs to see all Python command
# line arguments in one string. You can collect them using str.join():
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit(USAGE)
    if args.get("HELP"):
        print(USAGE)
        return
    operands = [int(v) for k, v in args.items() if k.startswith("OP")]
    sep = args.get("SEP", "\n")
    print(seq(operands, sep))

if __name__ == "__main__":
    main()


# └──> python3.8 args_regex.py 3
# 1
# 2
# 3

