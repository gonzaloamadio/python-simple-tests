

# ####
# Args unpacked
# ####

def foo(a, *args, **kwargs):
  print(a, args, kwargs)

# >>> args = (1,2,3)
# >>> foo(args)
# (1, 2, 3) () {}
# >>> foo(*args)
# 1 (2, 3) {}

# NOTE: This is not the parameters order convention, follow reading
def foo(a, b=None, *args, **kwargs):
  print(a, b, args, kwargs)

# >>> p
# (1, 2, 3)
# >>> foo(p)
# (1, 2, 3) None () {}
# >>> foo(*p)
# 1 2 (3,) {}

# >>> foo(p, b="asd")
# (1, 2, 3) asd () {}

# >>> foo(*p, b="asd")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: foo() got multiple values for argument 'b'

# The convention is: position arguments, *args, keyword arguments, **kwargs
# https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3

def foo2(a1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
  print(a1, arg_2, args, kw_1, kw_2, kwargs)

# >>> foo2(*p)
# 1 2 (3,) shark blobfish {}
# >>> p = (1,2,3,4,5)
# >>> foo2(*p)
# 1 2 (3, 4, 5) shark blobfish {}
# >>> foo2(*p, kw_1="asd")
# 1 2 (3, 4, 5) asd blobfish {}
# >>> p = (1,)
# >>> foo(*p)
# 1 None () {}
# >>> p = (1,)
# >>> foo2(*p)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: foo2() missing 1 required positional argument: 'arg_2'
# >>> foo2(1,2, kw_1="asd", pp="zc")
# 1 2 () asd blobfish {'pp': 'zc'}
# >>> foo2(1,2, kw_1="asd", pp="zc", pp2="pp2")
# 1 2 () asd blobfish {'pp': 'zc', 'pp2': 'pp2'}


# ####
# Modify kwargs and pass it along to another function
# ####

def foo(*args, **kwargs):
  kwargs["asd"] = 2
  foo2(**kwargs)

def foo2(**kwargs):
  print(kwargs)

# >>> foo()
# {'asd': 2}
# >>> foo(var=2)
# {'var': 2, 'asd': 2}

 # REF:
 # http://hangar.runway7.net/python/packing-unpacking-arguments

