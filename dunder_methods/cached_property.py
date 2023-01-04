"""
Making use of descriptors and lookup chain, we can create a lazy property. I.e. 
These are properties whose initial values are not loaded until they’re accessed for the first time. Then, 
they load their initial value and keep that value cached for later reuse.
"""
# slow_properties.py
import time

class DeepThought:
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life())     #  3 seconds
print(my_deep_thought_instance.meaning_of_life())     #  3 seconds
print(my_deep_thought_instance.meaning_of_life())     #  3 seconds


# lazy_properties.py
import time

class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)     # **
        return obj.__dict__[self.name]

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)

# ** En el objeto o instancia, bajo el nombre de la propiedad, guardamos el resultado.

"""
So then, when we access, as under __dict__ there is no key named as the property, it returns it.

It means, in the first execution, my_deep_thought_instance__dict__['meaning_if_life'] does not exists, so it goes 
to the __get__ of the descriptor
That __get__ save the result of the exec in the __dict__ of the instance
In the following acceses, it finds the property in the __dict__ of the instance that has precedence in the lookup chain
and it returns it.

Note that this works because, in this example, you've only used one method .__get__() of the descriptor protocol. 
You've also implemented a non-data descriptor. If you had implemented a data descriptor, 
then the trick would not have worked. Following the lookup chain, it would have had precedence 
over the value stored in __dict__. To test this out, run the following code:
"""