from functools import wraps

# Ref: https://www.geeksforgeeks.org/decorators-with-parameters-in-python/

# Decorator with arguments (trick: 3 levels)
def decorator_func(*args2):

    def Inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("outer args")
            for ele in args2:
                print(ele)
            print("inner args")
            for ele in args:
                print(ele)

            func(*args, **kwargs)

        return wrapper
    return Inner


# Not using decorator
@decorator_func(12, 15)
def my_fun(*args):
    for ele in args:
        print(ele)

# Same as:
# decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')

my_fun("Gees", "fsd")

################################################################################

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function'
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print 'Called example function'

# example()
# Calling decorated function
# Called example function
# example.__name__
# 'example'
# example.__doc__
# 'Docstring'
