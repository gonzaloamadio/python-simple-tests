"""
https://stackoverflow.com/questions/371753/how-do-i-implement-getattribute-without-an-infinite-recursion-error

This method will allow you to “catch” references to attributes that don't exist in your object

Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not an instance attribute nor is it found in the class tree for self). name is the attribute name. This method should return the (computed) attribute value or raise an AttributeError exception.
Note that if the attribute is found through the normal mechanism, __getattr__() is not called.

__getattribute__ is similar to __getattr__, with the important difference that 
__getattribute__ will intercept EVERY attribute lookup, doesn't matter if the attribute exists or not.
"""


class NFA(object):
    '''NFA class, does not break when we access an attribute that is not defined'''
    def __getattr__(self, name):
        return None

class Vehicle(NFA):
    can_fly = False
    number_of_weels = 0

class Car(Vehicle):
    number_of_weels = 4

    def __init__(self, color):
        self.color = color

my_car = Car("red")

print(my_car.color)
print(my_car.number_of_weels)
print(my_car.can_fly)
print(my_car.aa is None)
my_car.a = 2
print(my_car.a is None)

class A:
    context = Car("red")

a = A()
print("a.context.color = {}".format(a.context.color))
print("a.context.asd = {}".format(a.context.asd))

"""
❯ python getattr.py
red                         				# my_car.color
4							# my_car.number_of_weels
False						# my_car.can_fly
True							# my_car.aa is None
False						# my_car.a is None
a.context.color = red
a.context.asd = None
"""

class Dummy(object):
    def __getattr__(self, attr):
        return attr.upper()

d = Dummy()
d.does_not_exist # 'DOES_NOT_EXIST'
d.what_about_this_one  # 'WHAT_ABOUT_THIS_ONE'
# But if the attribute does exist, __getattr__ won’t be invoked:
d.value = "Python"
print(d.value)  # "Python"