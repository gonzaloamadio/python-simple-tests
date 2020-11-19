''' Demo script experimenting with various features of the
inspect module
'''
# To be run with Python3.3


from inspect_test import MyClass
from inspect_test import myfunc
from inspect_test import mygen

import inspect
from inspect import signature

if __name__=='__main__':

    # demo of inspect.getsource()
    obj = MyClass()

    # Get the source file where this class
    if inspect.isclass(MyClass):
        print(inspect.getsource(MyClass))

    # demo of inspect.getmembers()

    # Get the members
    print('Object Members:: \n')
    for member in inspect.getmembers(obj):
        print(member)


    print('\n\nRandom Expirements \n')

    # experiments with builtins
    functions = [obj.fun1, open, dir, myfunc]
    for func in functions:
        if inspect.isbuiltin(func):
            print('{0:s} is built in'.format(func.__name__))
        else:
            print('{0:s} is not built in'.format(func.__name__))

    print('\n')
    # experiments with signatures
    # Introduced in Python 3.3
    functions = [obj.fun1, inspect.isclass]
    for func in functions:
        sig = signature(func)
        print('Parameters: {0:s}:: {1:s}'.format(func.__name__,str(sig)))

    print('\n')

    # experiments with frames
    myfunc()

    # generator experiments
    generator = mygen()

    # get the current state
    print(inspect.getgeneratorstate(generator))

    count = 0
    for fib in generator:
        # get the current state
        print(inspect.getgeneratorstate(generator))

        #print the number yielded
        print(fib)
        if count >= 10:
            break
        count = count + 1

    print(inspect.getgeneratorstate(generator))
