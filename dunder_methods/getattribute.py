"""
Unlike __getattr__, this one is called always.
Be careful, how to define : 
https://stackoverflow.com/questions/371753/how-do-i-implement-getattribute-without-an-infinite-recursion-error

Called unconditionally to implement attribute accesses for instances of the class. 
If the class also defines __getattr__(), the latter will not be called unless __getattribute__()
either calls it explicitly or raises an AttributeError. This method should return the (computed) 
attribute value or raise an AttributeError exception. In order to avoid infinite recursion in this method, 
its implementation should always 
call the base class method with the same name to access any attributes it needs, 
for example, object.__getattribute__(self, name).

__getattribute__ is similar to __getattr__, with the important difference that 
__getattribute__ will intercept EVERY attribute lookup, doesn't matter if the attribute exists or not.
"""


class Dummy(object):
    def __getattribute__(self, attr):
        return 'YOU SEE ME?'
    
d = Dummy()
print(d.value)  # "YOU SEE ME?"
d.value = "Python"
print(d.value)  # "YOU SEE ME?"