"""Example of argument validation

There is more to see, this is somehow a simple validation.

# References:

https://marshmallow.readthedocs.io/en/stable/quickstart.html#quickstart
“Object serialization and deserialization, lightweight and fluffy.”

Dataclass, validator manual
https://stackoverflow.com/questions/50563546/validating-detailed-types-in-python-dataclasses
Libreria que debe hacer algo parecido a lo de stack overflow
https://pypi.org/project/dataclass-type-validator/

Dataclass: attrs, pydantic
https://pypi.org/project/dataclass-type-validator/
https://jackmckew.dev/dataclasses-vs-attrs-vs-pydantic.html

Libreria de data class type validator
https://github.com/levii/dataclass-type-validator
"""

import base64
import itertools
import importlib
import typing

# pylint disable=too-few-public-methods
import dataclasses

from typing import  Optional, Mapping


print("-------------------------------------------------")
print("--1-- Check that we can assign any value despite type hint")
print("-------------------------------------------------")

@dataclasses.dataclass()
class Conff:
    remote_hosts: typing.Dict
print(Conff("ASD"))

print("-------------------------------------------------")
print("--2-- Validator that only works for native types")
print("-------------------------------------------------")

# This kind of validate function works for native types and custom classes,
# but not those specified by the typing module: eg. typing.Dict
@dataclasses.dataclass(repr=False)
class Conf:
    remote_hosts: dict
    remote_hosts2: typing.Dict

    def validate(self):
        ret = True
        for field_name, field_def in self.__dataclass_fields__.items():
            actual_type = type(getattr(self, field_name))
            if actual_type != field_def.type:
                print(f"\t{field_name}: '{actual_type}' instead of '{field_def.type}'")
                ret = False
        return ret

    def __post_init__(self):
        if not self.validate():
            #raise ValueError('Wrong types')
            print(ValueError('Wrong types'))

    def __repr__(self) -> str:
        classname = self.__class__.__name__
        return (f"{classname}("
                f"remote_hosts={self.remote_hosts!r},"
                f"remote_hosts2={self.remote_hosts2!r})"
        )

print(Conf("ASD", 0))
print(Conf(2.4, 0))
print(Conf({"asd":2}, 0))


print("-------------------------------------------------")
print("--3--")
print("-------------------------------------------------")

import inspect
from contextlib import suppress
from functools import wraps


def enforce_types(callable):
    spec = inspect.getfullargspec(callable)

    def check_types(*args, **kwargs):
        parameters = dict(zip(spec.args, args))
        parameters.update(kwargs)
        for name, value in parameters.items():
            with suppress(KeyError):  # Assume un-annotated parameters can be any type
                type_hint = spec.annotations[name]
                if isinstance(type_hint, typing._SpecialForm):
                    # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
                    continue
                try:
                    actual_type = type_hint.__origin__
                except AttributeError:
                    # In case of non-typing types (such as <class 'int'>, for instance)
                    actual_type = type_hint
                # In Python 3.8 one would replace the try/except with
                # actual_type = typing.get_origin(type_hint) or type_hint
                if isinstance(actual_type, typing._SpecialForm):
                    # case of typing.Union[…] or typing.ClassVar[…]
                    actual_type = type_hint.__args__

                if not isinstance(value, actual_type):
                    raise TypeError('Unexpected type for \'{}\' (expected {} but found {})'.format(name, type_hint, type(value)))

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            check_types(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    if inspect.isclass(callable):
        callable.__init__ = decorate(callable.__init__)
        return callable

    return decorate(callable)


@enforce_types
@dataclasses.dataclass()
class Conf2:
    remote_hosts: dict
    remote_hosts2: typing.Dict


print(Conf2({"asd":2}, {}))
try:
    print(Conf2(2, {}))
except Exception as err:
    print(err)


print("-------------------------------------------------")
print("--4--")
print("-------------------------------------------------")


import pytest
import dataclasses
import typing

def dataclass_type_validator(target, strict: bool = False):
    fields = dataclasses.fields(target)

    errors = {}
    for field in fields:
        field_name = field.name
        expected_type = field.type
        value = getattr(target, field_name)

        err = None
        # Do some validation here.
        # CHeck : https://github.com/levii/dataclass-type-validator/blob/master/dataclass_type_validator/__init__.py
        #err = _validate_types(expected_type=expected_type, value=value, strict=strict)
        print(f"expected_type={expected_type}, value={value}, strict={strict}")

        if err is not None:
            errors[field_name] = err

    if len(errors) > 0:
        raise TypeValidationError('Dataclass Type Validation Error', errors=errors)

@dataclasses.dataclass(frozen=True)
class DataclassTestNumber:
    number: int
    optional_number: typing.Optional[int] = None

    def __post_init__(self):
        dataclass_type_validator(self)


print(DataclassTestNumber(number=1,optional_number=None,))
