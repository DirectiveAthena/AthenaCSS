# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Union,Any

# Custom Library
from AthenaColor import RGB,RGBA
from AthenaColor.Objects.Color.ColorTupleConversion import rgba_to_hexa, rgb_to_hex

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Base CSS Property Class -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperty:
    _value:Any
    important:bool
    color_output:str
    possibleValues:tuple|None=None
    possibleValueTypes:type|tuple[type]|Union[type]=type

    def __init__(self, value:object=None,*,important:bool=False, color_output:str="rgb"):
        # value is property to have more functionality over the setter of a value
        #   think properties which cannout have a negative value
        self.value = value
        self.important = important
        if color_output not in ("rgb","hex"):
            raise ValueError
        self.color_output = color_output

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
            raise TypeError(f"{value=} was not the same type as {type(self).__name__} -> {self.possibleValueTypes=}")
        elif self.possibleValues is not None:
            # to allow for ValueTypes to be used as inserted values
            for pv in {*self.possibleValues, 'initial', 'inherit'}:
                if value == pv or (isinstance(pv, type) and isinstance(value, pv)):
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
            case RGB() if self.color_output == "rgb":
                return f"rgb({self.value.r},{self.value.g},{self.value.b})"
            case RGBA() if self.color_output == "rgb":
                return f"rgba({self.value.r},{self.value.g},{self.value.b},{self.value.a})"
            case RGB() if self.color_output == "hex":
                # implemented due to heavy usecase of HEX values in CSS files
                return rgb_to_hex(*self.value.export())
            case RGBA() if self.color_output == "hex":
                # implemented due to heavy usecase of HEX values in CSS files
                return rgba_to_hexa(*self.value.export())
            case _ if hasattr(self.value, "__str__"):
                return str(self.value)
            case _:
                return NotImplemented

    def printer_name(self) -> str:
        return str(type(self).__name__).replace('_', '-')

    def print(self) -> str:
        if self.important:
            return f"{self.printer_name()}: {self.printer_value()} !important"
        return f"{self.printer_name()}: {self.printer_value()}"


class CSSpropertyShorthand:
    printer_order:list=None # to make sure everything is orderd as it should be
    important:bool

    def __init__(self,*args,important:bool=False, **values):
        # currently *args is not used

        # Inherited classes must have the named attributes set to the type of the to be made attribute
        for k,v in values.items():
            # relies on the fact that Shorthand Properties have their correct attributes set to the mapping CSSproperties
            if isinstance(v, self.__getattribute__(k)):
                self.__setattr__(k, v)
            elif k in self.printer_order:
                self.__setattr__(k, self.__getattribute__(k)(v))
            else:
                raise ValueError
        self.important = important

    def printer_value(self) -> str:
        if self.printer_order is None:
            return " ".join(*(
                str(p.printer_value())
                for p in dir(self)
                if isinstance(p, CSSproperty)
            ))
        elif isinstance(self.printer_order, list | tuple):
            return " ".join(
                str(self.__getattribute__(p).printer_value())
                for p in self.printer_order
                if isinstance(self.__getattribute__(p), CSSproperty)
            )
        # else:
        raise TypeError(self.printer_order)

    def printer_name(self) -> str:
        return str(type(self).__name__).replace('_', '-')

    def print(self) -> str:
        if self.important:
            return f"{self.printer_name()}: {self.printer_value()} !important"
        return f"{self.printer_name()}: {self.printer_value()}"
