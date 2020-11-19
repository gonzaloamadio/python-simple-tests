def first(iterable, default = None, condition = lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    If the `default` argument is given and the iterable is empty,
    or if it has no items matching the condition, the `default` argument
    is returned if it matches the condition.

    The `default` argument being None is the same as it not being given.

    Raises `StopIteration` if no item satisfying the condition is found
    and default is not given or doesn't satisfy the condition.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    >>> first([], default=1)
    1
    >>> first([], default=1, condition=lambda x: x % 2 == 0)
    Traceback (most recent call last):
    ...
    StopIteration
    >>> first([1,3,5], default=1, condition=lambda x: x % 2 == 0)
    Traceback (most recent call last):
    ...
    StopIteration

    NOTE: If we do not want default value to meet condition, this is enough:
        return next((x for x in the_iterable if condition(x)), default)
    """

    try:
        return next(x for x in iterable if condition(x))
    except StopIteration:
        if default is not None and condition(default):
            return default
        else:
            raise

def first2(iterable, condition = lambda x: True):
    """
    Returns the first item in the `iterable` that
    satisfies the `condition`.

    If the condition is not given, returns the first item of
    the iterable.

    Raises `StopIteration` if no item satysfing the condition is found.

    >>> first( (1,2,3), condition=lambda x: x % 2 == 0)
    2
    >>> first(range(3, 100))
    3
    >>> first( () )
    Traceback (most recent call last):
    ...
    StopIteration
    """

    return next(x for x in iterable if condition(x))
