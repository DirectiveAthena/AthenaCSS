# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Elements.CSSId import CSSId
from AthenaCSS.Objects.Elements.CSSElement import CSSElement
from AthenaCSS.Objects.Elements.CSSClass import CSSClass
from AthenaCSS.Objects.Elements.CSSPseudo import CSSPseudo
from AthenaCSS.Objects.Elements.CSSAttribute import CSSAttribute

from AthenaCSS.Objects.Rule.CSSManagerDeclarations import CSSManagerDeclarations
from AthenaCSS.Objects.Rule.CSSManagerSelectors import CSSManagerSelectors

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSRule"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
ELEMENTS = CSSId|CSSElement|CSSClass|CSSPseudo|CSSAttribute

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSRule:
    _selector_manager:CSSManagerSelectors
    _declaration_manager:CSSManagerDeclarations
    __slots__ = ["_selector_manager", "_declaration_manager"]

    def __init__(self):
        self._selector_manager = CSSManagerSelectors()
        self._declaration_manager = CSSManagerDeclarations()

    def __enter__(self) -> tuple[CSSManagerSelectors,CSSManagerDeclarations]:
        # Create a manager to be used to control the selection structure
        return self._selector_manager, self._declaration_manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass