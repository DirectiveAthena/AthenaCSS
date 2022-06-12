# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

# Custom Library

# Custom Packages
from AthenaCSS.data.support import CLASS_PREFIX
from AthenaCSS.models.selectors.element import CSSElement

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSClass"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSClass(CSSElement):
    def __init__(self, *parts, defined_name=None):
        self.defined_name = defined_name
        self.parts= list(parts)

    def __str__(self) -> str:
        return ''.join(f"{CLASS_PREFIX}{p}" for p in itertools.chain((self.defined_name,), self.parts) if p is not None)