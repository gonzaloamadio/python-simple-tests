"""
Using descriptors makes sense when you have multiple attributes with similar behavior.
For example class Person with attributes that can not be negative
We can put lots of `if` inside `__init__` , but....
"""

# Data descriptor
class BoundedNumber:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if self.min_val > value or value > self.max_val:
            msg = '{} takes values between {} and {}'.format(
                self.name, 
                self.min_val, 
                self.max_val,
            )
            raise ValueError(msg)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]
    
class Person:
    age = BoundedNumber(1, 120)
    weight = BoundedNumber(1, 250)
    height = BoundedNumber(1, 230)

    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
"""Notice how in the __set__ method we store the value in the instance (current object)
and not in the descriptor, i.e. self. All Person objects will share the same descriptor
so it doesn't make sense to store the values there.

If we store it in self, then all field would have same value
"""