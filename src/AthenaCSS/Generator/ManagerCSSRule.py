# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import NamedTuple

# Custom Library

# Custom Packages
from AthenaCSS.Library.Support import SELECTORGROUP_TYPES

from AthenaCSS.Declarations.CSSProperty import CSSProperty
from AthenaCSS.Declarations.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Selectors import (CSSId, CSSElement, CSSClass, CSSPseudo, CSSAttribute)

# ----------------------------------------------------------------------------------------------------------------------
# - SupportCode -
# ----------------------------------------------------------------------------------------------------------------------
Declarations = CSSProperty|CSSPropertyShorthand
SELECTORS = CSSId|CSSElement|CSSClass|CSSPseudo|CSSAttribute

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True,slots=True)
class ManagerSelectors:
    content: list = field(init=False, default_factory=list)
    # Subclass placed inside the ManagerSelectors as it is only meant to be accessed by the actuall Manager
    class SelectorGroup(NamedTuple):
        selectors: tuple[SELECTORS]
        group_type: SELECTORGROUP_TYPES

    # ------------------------------------------------------------------------------------------------------------------
    # - Types of content additions -
    # ------------------------------------------------------------------------------------------------------------------
    def add(self, *selectors:SELECTORS) -> ManagerSelectors:
        # reason for splitting the selectors up into their own groups
        #   is to make formatting in the to_string section more streamlined and consitent
        #   with either one "add" or multiple "add" sections

        for element in selectors:
            self.content.append(
                self.SelectorGroup(
                    selectors=(element,),
                    group_type=SELECTORGROUP_TYPES.combination
                )
            )
        return self

    def add_descendants(self, *selectors:SELECTORS) -> ManagerSelectors:
        self.content.append(
            self.SelectorGroup(
                selectors=selectors,
                group_type=SELECTORGROUP_TYPES.descendant
            )
        )
        return self

    def add_following(self, *selectors:SELECTORS) -> ManagerSelectors:
        self.content.append(
            self.SelectorGroup(
                selectors=selectors,
                group_type=SELECTORGROUP_TYPES.following
            )
        )
        return self

    def add_family(self, *selectors:SELECTORS) -> ManagerSelectors:
        self.content.append(
            self.SelectorGroup(
                selectors=selectors,
                group_type=SELECTORGROUP_TYPES.family
            )
        )
        return self

    def add_preceding(self, *selectors:SELECTORS) -> ManagerSelectors:
        self.content.append(
            self.SelectorGroup(
                selectors=selectors,
                group_type=SELECTORGROUP_TYPES.preceding
            )
        )
        return self
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True,slots=True)
class ManagerDeclarations:
    content: list = field(init=False, default_factory=list)
    # ------------------------------------------------------------------------------------------------------------------
    # - Types of content additions -
    # ------------------------------------------------------------------------------------------------------------------
    def add(self,*declarations:Declarations) -> ManagerDeclarations:
        for d in declarations:
            if not isinstance(d, Declarations):
                raise TypeError
            self.content.append(d)
        return self
