

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

