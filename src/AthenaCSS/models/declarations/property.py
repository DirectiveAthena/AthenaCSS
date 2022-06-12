# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy
from dataclasses import dataclass, field, InitVar
from typing import Any

# Custom Library

# Custom Packages
from AthenaCSS.models.declarations.value_logic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class CSSProperty:
    value:InitVar[Any]
    important:bool=field(kw_only=True, default=False)
    value_wrapped:bool=field(kw_only=True, default=False)
    _value:ValueLogic=field(init=False, repr=False)
    # below should be set for each different property
    value_logic:ValueLogic=field(init=False, repr=False)
    name:str=field(init=False, repr=False)

    def __post_init__(self, value):
        # make a new instance of the ValueLogic as all value Logical is defined there
        self._value = copy.deepcopy(self.value_logic) if self.value_logic is not None else ValueLogic()
        # the above has to be set first, only then can the self.value property be set
        self.value = value

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self) -> ValueLogic.value:
        return self._value.value

    @value.setter
    def value(self, value):
        # Actual setter is defined by the ValueLogic class
        self._value.value = value

    # ------------------------------------------------------------------------------------------------------------------
    # - Default Values -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def default(self):
        return self._value.default

    # ------------------------------------------------------------------------------------------------------------------
    # - generator -
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