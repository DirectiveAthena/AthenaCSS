# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import NamedTuple

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Elements.CSSId import CSSId
from AthenaCSS.Objects.Elements.CSSElement import CSSElement
from AthenaCSS.Objects.Elements.CSSClass import CSSClass
from AthenaCSS.Objects.Elements.CSSPseudo import CSSPseudo
from AthenaCSS.Objects.Elements.CSSAttribute import CSSAttribute
from AthenaCSS.Objects.Generator.Managers.RuleManager import RuleManager

from AthenaCSS.Library.Support import SELECTORGROUP_TYPES

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
ELEMENTS = CSSId|CSSElement|CSSClass|CSSPseudo|CSSAttribute

class SelectorGroup(NamedTuple):
    elements:tuple[ELEMENTS]
    group_type:SELECTORGROUP_TYPES

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ManagerSelectors(RuleManager):
    def add(self, *elements:ELEMENTS) -> ManagerSelectors:
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.combination
            )
        )
        return self

    def add_descendants(self, *elements:ELEMENTS) -> ManagerSelectors:
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.descendant
            )
        )
        return self

    def add_following(self, *elements:ELEMENTS) -> ManagerSelectors:
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.following
            )
        )
        return self

    def add_family(self, *elements:ELEMENTS) -> ManagerSelectors:
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.family
            )
        )
        return self

    def add_preceding(self, *elements:ELEMENTS) -> ManagerSelectors:
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.preceding
            )
        )
        return self