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
    def __str__(self) -> str:
        if isinstance(self.parts, str):
            return f"{CLASS_PREFIX}{self.parts}"
        # spread out for a bit better readability
        return ''.join(
            f"{CLASS_PREFIX}{p}"
            for p in itertools.chain((self.defined_name,), self.parts)
            # if parts is empty, then it is simply ignored
            if p is not None
        )