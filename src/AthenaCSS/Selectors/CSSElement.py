# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

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
        self.parts = list(parts)

    def __str__(self) -> str:
        return ''.join(str(p) for p in itertools.chain((self.defined_name,), self.parts) if p is not None)

    def __call__(self, *parts):
        parts_ = []
        for p in parts:
            if type(p) is type(self):
                parts_.extend(p.parts)
            else:
                parts_.append(p)

        return self.__class__(*self.parts, *parts_, defined_name=self.defined_name)