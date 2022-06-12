# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.models.declarations.property import CSSProperty

# ----------------------------------------------------------------------------------------------------------------------
# - SubProperty -
# ----------------------------------------------------------------------------------------------------------------------
class CSSSubProp(CSSProperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"