# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy

# Custom Library

# Custom Packages
from AthenaCSS.Properties.ValueLogic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSproperty:
    name:str
    _value:ValueLogic
    _value_logic=None
    __slots__ = ("_value","name")

    def __init__(self, value):
        # make a new instance of the _valyeFactory as all value Logicl is defined there
        self._value = copy.deepcopy(self._value_logic) if self._value_logic is not None else ValueLogic()
        self.value = value

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