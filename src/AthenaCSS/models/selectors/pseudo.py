# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
from dataclasses import dataclass, field

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
@dataclass(slots=True, unsafe_hash=True)
class CSSPseudo:
    """
    A special class to be inherited from by all Pseudo CSS selectors.
    This is done because these type selectors can have an extra value tied to them.
    """
    value:Any=None
    defined_name:str=field(kw_only=True, default=None)

    def __str__(self) -> str:
        if self.value is None:
            return f"{self.defined_name}"
        return f"{self.defined_name}({self.value})"

    # noinspection PyArgumentList
    def __call__(self, value:Any=None):
        return self.__class__(value, defined_name=self.defined_name)