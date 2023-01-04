
# https://realpython.com/python-descriptors/#python-descriptors-in-properties

class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

# When it’s accessed to .__set__() a specific value, it raises an AttributeError exception, 
# which is the recommended way to implement read-only descriptors.

### Same code with decorators

class Foo():
    @property
    def attribute1(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    @attribute1.setter
    def attribute1(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

### That in fact it is:
class Foo():
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42

    def setter(self, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")

    attribute1 = property(getter, setter)

# property(fget=None, fset=None, fdel=None, doc=None) -> object
# property() returns a property object that implements the descriptor protocol. 
# It uses the parameters fget, fset and fdel for the actual implementation of the three methods of the protocol.
