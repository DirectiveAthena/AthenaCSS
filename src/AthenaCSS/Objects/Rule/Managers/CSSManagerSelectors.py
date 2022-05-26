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
from AthenaCSS.Objects.Rule.Managers.CSSRuleManager import CSSRuleManager

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
class CSSManagerSelectors(CSSRuleManager):
    def add(self, *elements:ELEMENTS):
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.combination
            )
        )

    def add_descendants(self, *elements:ELEMENTS):
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.descendant
            )
        )

    def add_following(self, *elements:ELEMENTS):
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.following
            )
        )

    def add_family(self, *elements:ELEMENTS):
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.family
            )
        )

    def add_preceding(self, *elements:ELEMENTS):
        self._add_to_content(
            SelectorGroup(
                elements=elements,
                group_type=SELECTORGROUP_TYPES.preceding
            )
        )