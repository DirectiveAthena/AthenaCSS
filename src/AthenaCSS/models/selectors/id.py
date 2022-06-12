# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools
from dataclasses import dataclass, field
from typing import Any

# Custom Library

# Custom Packages
from AthenaCSS.data.support import ID_PREFIX

from AthenaCSS.models.selectors.element import CSSElement

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSId"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSId(CSSElement):
    def __str__(self) -> str:
        if isinstance(self.parts, str):
            return f"{ID_PREFIX}{self.parts}"
        # spread out for a bit better readability
        return ''.join(
            f"{ID_PREFIX}{p}"
            for p in itertools.chain((self.defined_name,), self.parts)
            # if parts is empty, then it is simply ignored
            if p is not None
        )