"""
inspect includes functions for inspecting the runtime environment while a program
is running. Most of these functions work with the call stack, and operate
on “call frames”. Each frame record in the stack is a 6 element tuple containing
the frame object, the filename where the code exists, the line number in that
file for the current line being run, the function name being called, a list of
lines of context from the source file, and the index into that list of the current
line. Typically such information is used to build tracebacks when exceptions
are raised. It can also be useful when debugging programs, since the stack frames
can be interrogated to discover the argument values passed into the functions.

currentframe() returns the frame at the top of the stack (for the current
function). getargvalues() returns a tuple with argument names, the names
of the variable arguments, and a dictionary with local values from the frame.
By combining them, we can see the arguments to functions and local variables
at different points in the call stack.
"""



import inspect

def recurse(limit):
    local_variable = '.' * limit
    print limit, inspect.getargvalues(inspect.currentframe())
    if limit <= 0:
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    recurse(3)


"""
Using stack(), it is also possible to access all of the stack frames from the
current frame to the first caller. This example is similar to the one above,
except it waits until reaching the end of the recursion to print the stack information.
"""

import inspect

def recurse(limit):
    local_variable = '.' * limit
    if limit <= 0:
        for frame, filename, line_num, func, source_code, source_index in inspect.stack():
            print '%s[%d]\n  -> %s' % (filename, line_num, source_code[source_index].strip())
            print inspect.getargvalues(frame)
            print
        return
    recurse(limit - 1)
    return

if __name__ == '__main__':
    recurse(3)
