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
from AthenaCSS.Objects.Generator.CSSGenerator import CSSGenerator

from AthenaColor import RGB

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSGenerators(BulkTests):
    def test_CSSGenerator0(self):
        with (css_generator := CSSGenerator()) as generator:
            with (rule0 := CSSRule()) as (selector, declaration):
                selector.add(
                    ElementLib.H1(CSSClass("something")),
                    ElementLib.H2(CSSClass("something_else")),
                )
                declaration.add(
                    PropLib.Color(RGB(128,64,32)),
                )
            generator.add_rule(
                rule0
            ).add_comment(
                "THIS SHOULD BE BETWEEN THE FIRST AND SECOND RULE"
            )

            with (rule1 := CSSRule()) as (selector, declaration):
                selector.add(
                    ElementLib.H1
                )
                declaration.add(
                    PropLib.Color(RGB(128,64,32)),
                )

            generator.add_rule(rule1)

            with (rule2 := CSSRule()) as (selector, declaration):
                selector.add(
                    ElementLib.H1
                )
                declaration.add(
                    PropLib.Color(RGB(128,64,32)),
                    PropLib.BackgroundColor(RGB(128,64,32)),
                    PropLib.BorderColor()
                )

            generator.add_rule(rule2)

        pass