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
    _value:CSSpropertyValue
    _valueFactory=None
    __slots__ = ("_value",)

    def __init__(self, value):
        self._value = copy.deepcopy(self._valueFactory) if self._valueFactory is not None else CSSpropertyValue()
        self.value = value

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value.value

    @value.setter
    def value(self, value):
        self._value.value = value

    @value.deleter
    def value(self):
        del self._value.value

    # ------------------------------------------------------------------------------------------------------------------
    # - Possible Values -
    # ------------------------------------------------------------------------------------------------------------------
