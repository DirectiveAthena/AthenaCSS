# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages
from .CsspropertyValue import CSSpropertyValue
from .CSSproperty import CSSproperty

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    _valueFactory = CSSpropertyValue(
        default="stretch",
        value_choice={
            str: {"center", "fex-start", "flex-end", "space-between", "space-around", "stretch"},
            (str,int): ("str", (1,2,3))
        },
    )
    def __init__(self, value=_valueFactory.default):
        super(align_content, self).__init__(value)