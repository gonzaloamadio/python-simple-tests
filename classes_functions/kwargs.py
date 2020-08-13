
# Modify kwargs and pass it along to another function
#
def foo(*args, **kwargs):
  kwargs["asd"] = 2
  foo2(**kwargs)

def foo2(**kwargs):
  print(kwargs)

# >>> foo()
# {'asd': 2}
# >>> foo(var=2)
# {'var': 2, 'asd': 2}

