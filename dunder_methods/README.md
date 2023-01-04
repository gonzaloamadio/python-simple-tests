# Descriptor
https://towardsdatascience.com/python-descriptors-and-how-to-use-them-5167d506af84
https://realpython.com/python-descriptors/


A descriptor is an object that:
* 		implements the Descriptor Protocol and
* 		is assigned to an attribute.

## Types of descriptors

There are two types: data descriptor, non-data descriptor

1) 		data descriptor: defines `__get__` and `__set__` or `__delete__`
```
__get__(self, instance, owner=None) -> value
__set__(self, instance, value) -> None
__delete__(self, instance) -> value
__set_name__(self, owner, name)
```

- self is the instance of the descriptor you’re writing.
- obj (instance) is the instance of the object your descriptor is attached to.
- type (owner) is the type of the object the descriptor is attached to.

- accessing the attribute doing obj.attribute calls the __get__ method,
- setting a value doing obj.attribute = new_value calls the __set__ method,
- deleting the attribute doing del obj.attribute calls the __delete__ method,

2) 		non-data descriptor: only defines `__get__`.

An example of a non-data descriptor is Python methods. Why? Well, Python functions are objects that implement __get__ and methods are functions that are assigned to attributes which makes them non-data descriptors!


## Descriptors are shared

https://realpython.com/python-descriptors/#how-to-use-python-descriptors-properly

Another important thing to know is that Python descriptors are instantiated just once per class. That means that every single instance of a class containing a descriptor shares that descriptor instance. This is something that you might not expect and can lead to a classic pitfall, like this:

```
# descriptors2.py
class OneDigitNumericValue():
    def __init__(self):
        self.value = 0
    def __get__(self, obj, type=None) -> object:
        return self.value
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value) != value:
            raise AttributeError("The value is invalid")
        self.value = value

class Foo():
    number = OneDigitNumericValue()

my_foo_object = Foo()
my_second_foo_object = Foo()

my_foo_object.number = 3
print(my_foo_object.number)
print(my_second_foo_object.number)

my_third_foo_object = Foo()
print(my_third_foo_object.number)

$ python descriptors2.py
3
3
3
```

## Lookup chain

When you access an attribute using `obj.attribute` syntax, Python (Aca vemos la presedencia de descriptors sobre non-data descriptors en el proceso de lookup)
* 		first looks for a data descriptor named attribute,
* 		if it doesn’t find any, it then checks in `obj.__dict__` for an attribute key,
* 		failing that, it then checks for a non-data descriptor.


So, what happens when you access the attribute of an object with dot notation? How does the interpreter know what you really need? Well, here’s where a concept called the lookup chain comes in:

1) First, you’ll get the result returned from the __get__ method of the data descriptor named after the attribute you’re looking for.
2) If that fails, then you’ll get the value of your object’s __dict__ for the key named after the attribute you’re looking for.
3) If that fails, then you’ll get the result returned from the __get__ method of the non-data descriptor named after the attribute you’re looking for.
4) If that fails, then you’ll get the value of your object type’s __dict__ for the key named after the attribute you’re looking for.
5) If that fails, then you’ll get the value of your object parent type’s __dict__ for the key named after the attribute you’re looking for.
6) If that fails, then the previous step is repeated for all the parent’s types in the method resolution order of your object.
7) If everything else has failed, then you’ll get an AttributeError exception.

Now you can see why it’s important to know if a descriptor is a data descriptor or a non-data descriptor? They’re on different levels of the lookup chain, and you’ll see later on that this difference in behavior can be very convenient.