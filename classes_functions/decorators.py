"""
REF: https://chase-seibert.github.io/blog/2013/12/17/python-decorator-optional-parameter.html

Also check this lib: https://pypi.org/project/decorator/
"""

###############################################################################
#            Basic decorator pattern
###############################################################################

# This one does nothing but prints that it was called.
# Implemented as a function decorator


from functools import wraps
import random


def my_decorator(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        print 'called decorator'
        return func(*args, **kwargs)
    return wrapped


@my_decorator
def function_to_wrap(bits=128):
    return random.getrandbits(bits)


# This is a very simplistic approach with some caveats, check ref link!!
from django.core.cache import cache as _cache
def cache(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        cache_key = [func, args, kwargs]
        result = _cache.get(cache_key)
        if result:
            return result
        result = func(*args, **kwargs)
        _cache.set(cache_key, result)
        return result
    return wrapped

@cache
def function_to_wrap2(bits=128):
    return random.getrandbits(bits)


###############################################################################
#           class decorator
###############################################################################

# Same decorator as a class
class cache(object):

    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)
    def __call__(self, *args, **kwargs):
        cache_key = [self.func, args, kwargs]
        result = _cache.get(cache_key)
        if result:
            return result
        result = self.func(*args, **kwargs)
        _cache.set(cache_key, result)
        return result

@cache
def function_to_wrap3(bits=128):
    return random.getrandbits(bits)


###############################################################################
#           Passing parameters
###############################################################################

# The trick here is to add another layer of indirection and create a function
# that takes parameters and returns your original decorator.

def cache(seconds=None):
    def callable(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            cache_key = [func, args, kwargs]
            result = _cache.get(cache_key)
            if result:
                return result
            result = func(*args, **kwargs)
            _cache.set(cache_key, result, timeout=seconds)
            return result
        return wrapped
    return callable

@cache(seconds=60)
def function_to_wrap4(bits=128):
    return random.getrandbits(bits)

# Same as a class
class cache(object):
    def __init__(self, seconds=None):
        self.seconds = seconds
    def __call__(self, func):
        @wraps(func)
        def callable(*args, **kwargs):
            cache_key = [func, args, kwargs]
            result = _cache.get(cache_key)
            if result:
                return result
            result = func(*args, **kwargs)
            _cache.set(cache_key, result, timeout=self.seconds)
            return result
        return callable


###############################################################################
#           Optional parameters
###############################################################################

# What if I don’t want the seconds argument to be mandatory? With either the
# functional or class based implementations, you will end up using your decorator like so:
# @cache()
# def function_to_wrap(bits=128):
#     return random.getrandbits(bits)
# This is just ugly. It introduces a source of errors (leaving off the ()
# will throw a somewhat mysterious exception:


# Here is a functional decorator that can be used as @cache(seconds=60), or just @cache.
def cache(*args, **kwargs):
    """First, you decide whether your decorator has been called as a callable or not.
    If not, you pull out your optional parameters (and default them if needed).
    Then you dynamically return either your decorator or a callable.
    Admittedly this is pretty ugly, but the resulting API is nice and clear.
    I’ve also failed repeatedly to produce a class based version of this
    """
    func = None
    if len(args) == 1 and __builtins__.callable(args[0]):
        func = args[0]
    if func:
        seconds = 60  # default values
    if not func:
        seconds = kwargs.get('seconds')

    def callable(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            cache_key = [func, args, kwargs]
            result = _cache.get(cache_key)
            if result:
                return result
            result = func(*args, **kwargs)
            _cache.set(cache_key, result, timeout=seconds)
            return result
        return wrapped

    return callable(func) if func else callable


@cache(seconds=60)
def function_to_wrap5(bits=128):
    return random.getrandbits(bits)
@cache
def function_to_wrap6(bits=128):
    return random.getrandbits(bits)


if __name__ == "__main__":
    function_to_wrap()  # prints 'called decorator'
    print function_to_wrap2()  # prints '47141457794590517513826129394479136255'
    print function_to_wrap2()  # prints '47141457794590517513826129394479136255' also (cached)
