# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

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
    def __init__(self, *parts, defined_name=None):
        self.defined_name = defined_name
        self.parts= list(
            itertools.chain.from_iterable((ID_PREFIX, x) for x in parts) # thanks to twidi
        )