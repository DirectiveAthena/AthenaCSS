# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
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
class CSSpropertyValue:
    _value:Any
    _default:None
    _value_choice:dict[type:tuple|type:None]
    __slots__ = ("_value","_default", "_value_choice")

    def __init__(self, *, default=None,value_choice=None):
        self.default = default
        self.value_choice = value_choice if value_choice is not None else dict()

    def __str__(self):
        return f"{self.default}, {self.value_choice}"

    def __repr__(self) -> str:
        # cane be done because the key of self.value_choice is alwyas a type!
        value_choice = {k.__name__:v for k,v in self.value_choice.items()}
        return f"CSSpropertyValue(default={self.default!r}, value_choice={value_choice})"

    def __copy__(self) -> CSSpropertyValue:
        return CSSpropertyValue(default=self.default, value_choice=self.value_choice)


    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value:object):
        # todo maybe don't do a return here
        if value in INITIALINHERIT:
            self._value = value
            return

        try:
            if self.value_choice and (isinstance((choice:= self.value_choice[type(value)]), tuple) and value not in choice):
                raise ValueError
            # don't need to check anything else:
            #   If self.value_choice is empty dictionary -> Anything is allowed, ergo no need for a check
            #   If choice is anything else than a tuple -> Out of convention, the key will be a type, and the value will be None
            #       This means the type is recognized, but doesn't have a set value
            #   If choice was a tuple, and value was in choice -> everything is fine

        except KeyError:
            raise TypeError
        self._value = value


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
        self._default = value

    @default.deleter
    def default(self):
        self._default = None

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
            if not isinstance(key, type) or not (isinstance(key, tuple) and all(isinstance(k, type) for k in key)):
                raise ValueError("Key must be a type or tuple of types")
            elif not isinstance(val, set) and val is not None:
                raise ValueError("Value must be a set or None")
            elif key is str and val is not None:
                value[key] = value[key].update(INITIALINHERIT)
        self._value_choice = value

    @value_choice.deleter
    def value_choice(self):
        self._value_choice = dict()

