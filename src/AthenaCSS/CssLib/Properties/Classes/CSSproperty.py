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

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperty:
    _value:Any
    important:bool
    color_output:str
    _color_output_choice = ("rgb","hex") # possible color outputs

    def __init__(
            self,
            value:object=None,
            *, # The following is keyword only
            important:bool=False,
            color_output:str="rgb"
        ):
        # value is property to have more functionality over the setter of a value
        #   think properties which cannout have a negative value
        self.value = value
        self.important = important
        self.color_output = color_output

    # ------------------------------------------------------------------------------------------------------------------
    # - Properties -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def important(self):
        return self._important
    @important.setter
    def important(self, value:bool):
        if not isinstance(value, bool):
            raise TypeError
        self._important = value

    @property
    def color_output(self):
        return self._color_output
    @color_output.setter
    def color_output(self, value:str):
        if not isinstance(value, str):
            raise TypeError
        elif not value in self._color_output_choice:
            raise ValueError
        self._color_output = value

    # ------------------------------------------------------------------------------------------------------------------
    # - True Value related -
    # ------------------------------------------------------------------------------------------------------------------
    def value_presetter(self, value):
        return value

    def value_validator(self, value):
        return value

    @property
    def defaultValue(self) -> object|None:
        return None

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if value is None:
            self._value = self.defaultValue
        else:
            self._value = self.value_validator(self.value_presetter(value))

    @value.deleter
    def value(self):
        del self._value
        self._value = None

    # ------------------------------------------------------------------------------------------------------------------
    # - Printing to str -
    # ------------------------------------------------------------------------------------------------------------------
    def printer_name(self) -> str:
        return str(type(self).__name__).replace('_', '-')

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
                return self.printer_value_other()

    def printer_value_other(self) -> str:
        return NotImplemented

    def print(self) -> str:
                        # name                      # value
        printable = [   self.printer_name(), ":",   self.printer_value()]

        if self.important: # when the setting is enabled, the line should end with "!important"
            printable.append("!important")

        # return the full string, spaced out
        return " ".join(printable)

    # ------------------------------------------------------------------------------------------------------------------
    # - Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return self.print()
    def __repr__(self):
        return f"{type(self).__name__}(value={self.value})"
