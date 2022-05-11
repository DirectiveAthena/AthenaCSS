# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import copy

# Custom Library

# Custom Packages
from AthenaCSS.Properties.CsspropertyValue import CSSpropertyValue

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSproperty:
    value:CSSpropertyValue
    _valueFactory=None
    def __init__(self):
        self.value = copy.copy(self._valueFactory) if self._valueFactory is not None else CSSpropertyValue()
