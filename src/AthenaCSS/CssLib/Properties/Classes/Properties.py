# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

from typing import Union,Any

# Custom Library
from AthenaColor import RGB,RGBA
from AthenaColor.Objects.Color.ColorTupleConversion import rgba_to_hexa, rgb_to_hex

from AthenaLib.Types.ValueType import ValueType

# Custom Packages
from .CSSproperty import CSSproperty
# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSpropertySingle(CSSproperty):
    possibleValues:tuple|None|tuple[object|type]=None
    possibleValuesTupleLen:int=0
    possibleValueTypes:type|tuple[type]|Union[type]=type

    def value_validator(self, value):
        # Faster if statements provided by twitch viewer: mateoox600
        if not isinstance(value, self.possibleValueTypes):
            raise TypeError(f"{value=} was not the same type as {type(self).__name__} -> {self.possibleValueTypes=}")
        elif self.possibleValues is not None:
            # to allow for ValueTypes to be used as inserted values
            for pv in {*self.possibleValues, 'initial', 'inherit'}:
                if value == pv or (isinstance(pv, type) and isinstance(value, pv)):
                    break
            else:
                raise ValueError(f"{value=} not in {self.possibleValues=}")

        # EVENTUALLY ACTUALLY RETURN THE VALUE!
        return value

class CSSpropertyMulti(CSSproperty):
    possibleValues:tuple|None|tuple[object|type]=None
    possibleValuesTupleLen:int=0
    possibleValueTypes:type|tuple[type]|Union[type]=type

    def value_validator(self, value):
        if isinstance(self.possibleValues, itertools.product):
            if not isinstance(value, tuple):
                raise ValueError(f"{value=} was not a specified tuple")
            elif len(value) != self.possibleValuesTupleLen:
                raise ValueError(f"{value=} was not of the allowed length of {self.possibleValuesTupleLen}")
            # Value was a tuple,and the length matched the allowed length, which means we can start parsing for object types
            for pv in self.possibleValues:
                counter = 0
                for i, v in enumerate(pv):
                    value_ = value[i]
                    if (isinstance(v, str) and value_ == v) or (isinstance(v, ValueType) and isinstance(value_, v)):
                        # print("STRING VALUE FOUND")
                        counter += 1
                if counter == self.possibleValuesTupleLen:
                    break
                break
            else:
                if value not in ('initial', 'inherit'):
                    raise ValueError(f"{value=} not in {self.possibleValues=}")
        # EVENTUALLY ACTUALLY RETURN THE VALUE!
        return value


