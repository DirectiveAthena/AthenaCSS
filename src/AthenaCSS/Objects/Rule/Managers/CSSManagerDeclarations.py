# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Objects.Rule.Managers.CSSRuleManager import CSSRuleManager

# ----------------------------------------------------------------------------------------------------------------------
# - SupportCode -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSManagerDeclarations(CSSRuleManager):
    def add(self,*properties:PROPERTIES):
        for p in properties:
            self._add_to_content(
                p
            )