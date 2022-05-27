# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSElement"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSElement:
    __slots__ = ["parts", "defined_name"]

    def __init__(self, *parts, defined_name=None):
        self.defined_name = defined_name
        self.parts = list(x for x in (self.defined_name, *parts) if x is not None)

    def __str__(self) -> str:
        return ''.join(str(p) for p in self.parts)

    def __call__(self, *parts):
        return self.__class__(*parts, defined_name=self.defined_name)