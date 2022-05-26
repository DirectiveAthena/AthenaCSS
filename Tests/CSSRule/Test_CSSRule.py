# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
import AthenaCSS.Library.PropertyLibrary as PropLib
from AthenaCSS.Objects.Elements.CSSAttribute import CSSAttribute
from AthenaCSS.Objects.Elements.CSSClass import CSSClass
from AthenaCSS.Objects.Elements.CSSId import CSSId
from AthenaCSS.Objects.Generator.Content.Rules.CSSRule import CSSRule
from AthenaCSS.Objects.Generator.Content.Rules.Managers.ManagerSelectors import SelectorGroup
from AthenaCSS.Library.Support import SELECTORGROUP_TYPES

from AthenaColor import RGB

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSRules(BulkTests):
    def test_CSSRule0(self):
        with (rule:=CSSRule()) as (selector,_):
            selector.add(
                ElementLib.H1
            )

        self.assertEqual(
            {SelectorGroup(
                elements=(ElementLib.H1,),
                group_type=SELECTORGROUP_TYPES.combination
            )},
            rule.selectors
        )

    def test_CSSRule1(self):
        with (rule := CSSRule()) as (selector, declaration):
            selector.add(
                ElementLib.H1
            )
            declaration.add(
                (fore_color:=PropLib.Color(RGB(128,64,32))),
                (back_color:=PropLib.BackgroundColor(RGB(128,64,32)))
            )

        self.assertEqual(
            {SelectorGroup(
                elements=(ElementLib.H1,),
                group_type=SELECTORGROUP_TYPES.combination
            )},
            rule.selectors
        )

        self.assertEqual(
            {fore_color, back_color},
            rule.declarations
        )


