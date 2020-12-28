"""
Usage:
  foo bar [--baz] [--num-jobs=<jobs>]
  foo read <input_file> [--verbose]

Options:
  --baz              Do some baz stuff
  --verbose          Be verbose
  --num-jobs=<jobs>  number of jobs [default: 1]

"""

import docopt

opts = docopt.docopt(__doc__)
print(opts)


"""
└──> python docopt-01.py bar --num-jobs=42
{'--baz': False,
 '--num-jobs': '42',
 '--verbose': False,
 '<input_file>': None,
 'bar': True,
 'read': False}

%python doctop-01.py read input.txt
{'--baz': False,
 '--num-jobs': '1',
 '--verbose': False,
 '<input_file>': 'input.txt',
 'bar': False,
 'read': True}
 """

 """------------------- Other things you can do:
REF: https://dmerej.info/blog/post/docopt-v-argparse/

# Exclusive conditions

Usage: my_program (--either-this <and-that> | <or-this>)
"""
