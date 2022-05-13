# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Properties.CSSproperty import CSSproperty
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Other(CSSproperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"

# ----------------------------------------------------------------------------------------------------------------------
class Steps(Other):
    name="steps"
    value_logic = ValueLogic(
        value_choice={
            (int,str):(Any, {"end", "start", ""})
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)