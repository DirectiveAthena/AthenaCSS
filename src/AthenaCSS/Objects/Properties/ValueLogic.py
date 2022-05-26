# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any, Iterable
from types import UnionType
import copy

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV

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
    printer_space:str
    __slots__ = ("_value","_default", "_value_choice", "printer_space")

    def __init__(self, *, default=None,value_choice=None, printer_space=" "):
        self.value_choice = value_choice if value_choice is not None else dict()
        self.default = default # ALWAYS do this FOLLOWING the setting of value_choice
        self.printer_space = printer_space

    def __repr__(self) -> str:
        # cane be done because the key of self.value_choice is alwyas a type!
        value_choice = {k:v for k,v in self.value_choice.items()}
        return f"ValueLogic(default={self.default!r}, value_choice={value_choice})"

    def value_checker(self, value) -> Any:
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
                        raise TypeError(f"the partial value {val} was not of the defined type of {c}")
                    elif isinstance(c, tuple) and val not in c:
                        raise ValueError(f"the partial value {val} was not in the defined choice of {c}")
                    # anything else is basically equivalent to TRUE, so don't check

        elif (val_type := type(value)) in self.value_choice:
            # Only a single value is inserted
            #   so the value of the key value pair could either be a None or a set of possible values
            if (choice := self.value_choice[val_type]) is not Any and value not in choice:
                raise ValueError(f"the value {value} was not in the defined choice of {choice}")

        elif isinstance(value, Iterable) \
                and any(all(isinstance(v, vc) for v in value) for vc in self.value_choice):
            # it is an iterable, but the choices were made up out of parent classes instead of specific classes
            pass #todo, wtf do I do here?
                 #  the if statement contains the check ... so ... what now?

        elif any(isinstance(value, vc) for vc in self.value_choice if not isinstance(vc, tuple)):
            pass #todo, wtf do I do here?
                 #  the if statement contains the check ... so ... what now?

        else:
            raise TypeError(f"the value {value} was not of an allowed type")

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
        self._value = self.value_checker(value)

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
        if value is None and None not in self.value_choice.keys():
            self._default = None
        else:
            self._default = self.value_checker(value)

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
            if val is Any or key in (None,Any):
                continue
            elif isinstance(key, tuple):
                if not all(isinstance(k, type) or isinstance(k,UnionType) for k in key if k is not None):
                    raise SyntaxError(f"Not all items in the tuple were types, in the value:{value}")
            elif isinstance(key, type):
                if not all(isinstance(v, key) for v in val):
                    raise SyntaxError(f"Not all items in the predefined options were of the allowed type, in the value:{value}")
            else:
                raise SyntaxError(f"value_choice did not consist out of a tuple or a type, in the value:{value}")

        self._value_choice = value

    # ------------------------------------------------------------------------------------------------------------------
    # - Generator -
    # ------------------------------------------------------------------------------------------------------------------
    def printer(self) -> str:
        match self.value:
            case None:
                return "none"
            case RGB()|RGBA()|HEX()|HEXA()|HSL()|HSV():
                return f"{type(self.value).__name__.lower()}{self.value.export()}"
            case tuple(value):
                return self.printer_space.join(str(v) for v in value)
            case value: # catches all
                return str(value)

    def __str__(self) -> str:
        return self.printer()
