# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.CssLib.Selectors.Selectors import Selector
from AthenaCSS.CssLib.Properties.Properties import CSSpropertyShorthand,CSSproperty

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSelement:
    properties:list[CSSproperty|CSSpropertyShorthand]
    selectors:list[Selector]

    def __init__(self):
        self.properties = []
        self.selectors = []

    def print(self) -> str:
        selectors = ',\n'.join(s.print() for s in self.selectors)
        properties = ';\n'.join(p.print() for p in self.properties)
        return f"{selectors} {{\n{properties}\n}}"

    def add_selector(self, selector:Selector) -> CSSelement:
        if not isinstance(selector, Selector):
            raise TypeError(f"{selector=} is not a Selector")
        self.selectors.append(selector)
        return self

    def add_property(self, prop:CSSproperty|CSSpropertyShorthand) -> CSSelement:
        if not isinstance(prop, CSSproperty|CSSpropertyShorthand):
            raise TypeError(f"{prop=} is not a CSSproperty or CSSpropertyShorthand")
        self.properties.append(prop)
        return self