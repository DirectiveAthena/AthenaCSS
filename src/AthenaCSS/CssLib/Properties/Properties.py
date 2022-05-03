# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Union

# Custom Library

# Custom Packages
from AthenaCSS.CssLib.Types import ValueType

# ----------------------------------------------------------------------------------------------------------------------
# - Base CSS Property Class -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperty:
    _value:object
    important:bool
    possibleValues:tuple|None=None
    possibleValueTypes:type|tuple[type]|Union[type]=type

    def __init__(self, value:object=None,*,important=False):
        # value is property to have more functionality over the setter of a value
        #   think properties which cannout have a negative value
        self.value = value
        self.important = important

    def value_presetter(self, value) -> object:
        return value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        # self.value_setter done to make perties add extra functionality
        value = self.value_presetter(value)

        # Faster if statements provided by twitch viewer: mateoox600
        if value is None:
            value = self.defaultValue
        elif not isinstance(value, self.possibleValueTypes):
            raise TypeError(f"{value=} was not the same type as {self.possibleValueTypes=}")
        elif self.possibleValues is not None:
            # to allow for ValueTypes to be used as inserted values
            for pv in {*self.possibleValues, 'initial', 'inherit'}:
                if value == pv:
                    break
                elif isinstance(pv, type) and isinstance(value, pv):
                    break
            else:
                raise ValueError(f"{value=} not in {self.possibleValues=}")

        # EVENTUALLY ACTUALLY SET THE VALUE!
        self._value = value
    
    @property
    def defaultValue(self) -> object|None:
        return None

    def printer_value(self) -> str:
        match self.value:
            case None:
                return "none"
            case str(v) | v if hasattr(v, "__str__"):
                return v
            case int(v) | float(v):
                return str(v)
            case _:
                return NotImplemented

    def printer_name(self) -> str:
        return str(type(self).__name__).replace('_', '-')

    def print(self) -> str:
        if self.important:
            return f"{self.printer_name()}: {self.printer_value()} !important"
        else:
            return f"{self.printer_name()}: {self.printer_value()}"


class CSSpropertyShorthand:
    printer_order:list=None # to make sure everything is orderd as it should be
    important:bool

    def __init__(self,*args,important:bool=False, **values):
        # Inherited classes must have the named attributes set to the type of the to be made attribute
        for k,v in values.items():
            self.__setattr__(k, self.__getattribute__(k)(v))
        self.important = important

    def print(self) -> str:
        if self.printer_order is None:
            string =  " ".join(
                *(
                    p.printer_value
                    for p in dir(self)
                    if isinstance(p, CSSproperty)
                )
            )
        elif isinstance(self.printer_order, list|tuple):
            string = " ".join(
                self.__getattribute__(p).printer_value
                for p in self.printer_order
                if isinstance(self.__getattribute__(p), CSSproperty)
            )
        else:
            raise TypeError(self.printer_order)

        if self.important:
            return f"{string} !important"
        else:
            return string
