#  it is possible to ask for a complete specification of the arguments the callable takes,
# including default values. The getargspec() function returns a tuple containing the
# list of positional argument names, the name of any variable positional arguments
# (e.g., *args), the names of any variable named arguments (e.g., **kwds),
# and default values for the arguments. If there are default values, they match
# up with the end of the positional argument list.


import inspect
import example

arg_spec = inspect.getargspec(example.module_level_function)
print 'NAMES   :', arg_spec[0]
print '*       :', arg_spec[1]
print '**      :', arg_spec[2]
print 'defaults:', arg_spec[3]

args_with_defaults = arg_spec[0][-len(arg_spec[3]):]
print 'args & defaults:', zip(args_with_defaults, arg_spec[3])
