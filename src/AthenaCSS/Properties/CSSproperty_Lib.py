# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages
from .ValueLogic import ValueLogic
from .CSSproperty import CSSproperty

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    name="align-content"
    _value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str: {"center", "fex-start", "flex-end", "space-between", "space-around", "stretch"},
        },
    )
    def __init__(self, value=_value_logic.default):
        super(align_content, self).__init__(value)