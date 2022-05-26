# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy

# Custom Library

# Custom Packages
from AthenaCSS.Declarations.ValueLogic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSProperty:
    name:str # don't rely on self.__class__.name, because of inheritance
    important:bool
    value_wrapped:bool
    _value:ValueLogic
    value_logic=None
    __slots__ = ("_value","name", "important", "value_wrapped")

    def __init__(self, value, *, important:bool=False, value_wrapped=False):
        # make a new instance of the ValueLogic as all value Logical is defined there
        self._value = copy.deepcopy(self.value_logic) if self.value_logic is not None else ValueLogic()
        self.value = value
        self.important = important
        self.value_wrapped =value_wrapped

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value!r})"

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value.value

    @value.setter
    def value(self, value):
        # Actual setter is defined by the ValueLogic class
        self._value.value = value

    @value.deleter
    def value(self):
        del self._value.value

    # ------------------------------------------------------------------------------------------------------------------
    # - Default Values -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def default(self):
        return self._value.default

    # ------------------------------------------------------------------------------------------------------------------
    # - Generator -
    # ------------------------------------------------------------------------------------------------------------------
    def printer(self) -> str:
        return f"{self.name_printer()}: {self.value_printer()}"

    def name_printer(self) -> str:
        return f"{self.name}"

    def value_printer(self) -> str:
        value = self._value.printer()
        if self.value_wrapped:
            value = f'"{value}"'
        if self.important:
            value += " !important"
        return value

    def __str__(self) -> str:
        return self.printer()

# ----------------------------------------------------------------------------------------------------------------------
# - SubProperty -
# ----------------------------------------------------------------------------------------------------------------------
class SubProp(CSSProperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"