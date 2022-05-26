# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.Decorators.ClassMethods import return_self_classmethod as return_self

# Custom Packages
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Objects.Generator.Content.Rules.Managers.RuleManager import RuleManager

# ----------------------------------------------------------------------------------------------------------------------
# - SupportCode -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ManagerDeclarations(RuleManager):
    def add(self,*properties:PROPERTIES) -> ManagerDeclarations:
        for p in properties:
            self._add_to_content(p)
        return self