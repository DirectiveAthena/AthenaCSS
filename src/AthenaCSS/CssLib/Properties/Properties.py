# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Union

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Base CSS Property Class -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperty:
    value:object
    possibleValues:tuple|None=None
    possibleValueTypes:type|tuple[type]|Union[type]=object

    def __init__(self, value:object=None):
        # Faster if statements provided by twitch viewer: mateoox600
        if value is None:
            value = self.defaultValue
        elif  self.possibleValues is not None \
        and value not in {*self.possibleValues, 'initial', 'inherit'}:
            raise ValueError(f"{value=} not in {self.possibleValues=}")

        if not isinstance(value,self.possibleValueTypes):
            raise TypeError(f"{value=} was not the same type as {self.possibleValueTypes=}")
        self.value = value

    @property
    def defaultValue(self) -> object|None:
        return None

    def value_printer(self) -> str:
        match self.value:
            case str(v) | v if hasattr(v, "__str__"):
                return v
            case None:
                return "none"
            case int(v) | float(v):
                return str(v)
            case _:
                return NotImplemented

    def print(self) -> str:
        return f"{str(type(self).__name__).replace('_','-')}: {self.value_printer()}"

class CSSpropertyShorthand:
    def __init__(self, **values):
        # Inherited classes must have the named attributes set to the type of the to be made attribute
        for k,v in values.items():
            self.__setattr__(k, self.__getattribute__(k)(v))

    def print(self) -> str:
        return " ".join(*(p.value_printer for p in dir(self) if isinstance(p, CSSproperty)))
