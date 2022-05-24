# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSPseudo:
    value:Any
    defined_name:str

    __slots__ = ["value"]

    def __init__(self, value:Any=None):
        self.value = value

    def __str__(self):
        if self.value is None:
            return f"{self.defined_name}"
        return f"{self.defined_name}({self.value})"