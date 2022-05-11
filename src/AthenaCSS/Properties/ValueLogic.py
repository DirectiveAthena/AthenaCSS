# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any, Iterable
import copy

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
INITIALINHERIT = {"initial", "inherit"}

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ValueLogic:
    _value:Any
    _default:None
    _value_choice:dict
    __slots__ = ("_value","_default", "_value_choice")

    def __init__(self, *, default=None,value_choice=None):
        self.value_choice = value_choice if value_choice is not None else dict()
        self.default = default # ALWAYS do this AFTER the setting of value_choice

    def __str__(self):
        return f"{self.default}, {self.value_choice}"

    def __repr__(self) -> str:
        # cane be done because the key of self.value_choice is alwyas a type!
        value_choice = {k.__name__:v for k,v in self.value_choice.items()}
        return f"ValueLogic(default={self.default!r}, value_choice={value_choice})"

    def val_checker(self, value) -> Any:
        # don't need to check if the dict is empty or if there is a "catch all - Any"
        if not self.value_choice \
                or value in INITIALINHERIT \
                or Any in self.value_choice \
                or (value is None and None in self.value_choice):
            pass # passed here, as this immediatly goes to the end of the if statement (aka, return value)

        elif isinstance(value, Iterable) \
                and (val_type := tuple(type(v) for v in value)) in self.value_choice:
            # if it is none, then it can be skipped as anything is allowed then
            if (choice := self.value_choice[val_type]) is not None:
                # we know that the len of val_type and value is the same, no need to check again
                for val, c in zip(value, choice):
                    if isinstance(c, type) and not isinstance(val, c):
                        raise TypeError(f"the partial value {val!r} was not of the defined type of {c}")
                    elif isinstance(c, tuple) and val not in c:
                        raise ValueError(f"the partial value {val!r} was not in the defined choice of {c}")
                    # anything else is basically equivalent to TRUE, so don't check

        elif (val_type := type(value)) in self.value_choice:
            # Only a single value is inserted
            #   so the value of the key value pair could either be a None or a set of possible values
            if (choice := self.value_choice[val_type]) is not Any and value not in choice:
                raise ValueError(f"the value {value!r} was not in the defined choice of {choice}")
        else:
            raise TypeError(f"the value {value!r} was not of an allowed type")


        # ! RETURN VALUE !
        return value

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = self.val_checker(value)

    @value.deleter
    def value(self):
        self._value = copy.copy(self._default)

    # ------------------------------------------------------------------------------------------------------------------
    # - Default -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def default(self):
        return self._default

    @default.setter
    def default(self, value):
        self._default = self.val_checker(value)

    # ------------------------------------------------------------------------------------------------------------------
    # - ValueChoice -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value_choice(self):
        return self._value_choice

    @value_choice.setter
    def value_choice(self, value:dict[type:set|type:None]):
        if not isinstance(value, dict):
            raise TypeError
        # If trhe dict is empty, the for loop won't even do anything, so no need to make an if statement here
        for key, val in value.items():
            if isinstance(key, tuple):
                if not all(isinstance(k, type) for k in key):
                    raise SyntaxError("Not all items in the tuple were types")
            elif isinstance(key, type):
                if key is not Any and not all(isinstance(v, key) for v in val):
                    raise SyntaxError("Not all items in the predefined options were of the allowed type")

        self._value_choice = value

