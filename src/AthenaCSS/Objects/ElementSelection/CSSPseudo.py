# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSPseudo"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSPseudo:
    """
    A special class to be inherited from by all Pseudo CSS selectors.
    This is done because these type selectors can have an extra value tied to them.
    """
    value:Any
    defined_name:str

    __slots__ = ["value", "defined_name"]

    def __init__(self, value:Any=None,*, defined_name:str=None):
        self.value = value
        self.defined_name = defined_name

    def __str__(self):
        if self.value is None:
            return f"{self.defined_name}"
        return f"{self.defined_name}({self.value})"

    def __call__(self, value:Any=None):
        return self.__class__(value, defined_name=self.defined_name)