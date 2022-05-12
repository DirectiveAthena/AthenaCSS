# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperty:
    name:str # don't rely on self.__class__.name, because of inheritance
    _value:ValueLogic
    value_logic=None
    __slots__ = ("_value","name")

    def __init__(self, value):
        # make a new instance of the _valyeFactory as all value Logicl is defined there
        self._value = copy.deepcopy(self.value_logic) if self.value_logic is not None else ValueLogic()
        self.value = value

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
    # - Printer -
    # ------------------------------------------------------------------------------------------------------------------
    def printer(self) -> str:
        return f"{self.name}: {self._value.printer()}"

    def __str__(self) -> str:
        return self.printer()