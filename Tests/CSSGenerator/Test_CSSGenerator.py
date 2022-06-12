# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom data
from AthenaColor import RGB
from AthenaCSS import *

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
                    SelectorElement.H1(CSSClass("something")),
                    SelectorElement.H2(CSSClass("something_else")),
                    SelectorElement.H2(CSSClass("something_else"), CSSClass("Something_totaly"), CSSClass("different")),
                )
                declaration.add(
                    Property.Color(RGB(128,64,32)),
                )
            generator.add_rule(
                rule0
            ).add_comment(
                "THIS SHOULD BE BETWEEN THE FIRST AND SECOND RULE"
            )

            with (rule1 := CSSRule()) as (selector, declaration):
                selector.add(
                    SelectorElement.H1
                )
                declaration.add(
                    Property.Color(RGB(128,64,32)),
                )

            generator.add_rule(rule1)

            with (rule2 := CSSRule()) as (selector, declaration):
                selector.add(
                    SelectorElement.H1,
                    SelectorElement.H2(CSSId("Help"))
                )
                declaration.add(
                    Property.Color(RGB(128,64,32)),
                    Property.BackgroundColor(RGB(128,64,32)),
                    Property.BorderColor()
                )

            generator.add_rule(rule2)

        self.assertEqual(
"""h1.something,
h2.something_else,
h2.something_else.Something_totaly.different {
    color: rgb(128, 64, 32);
}
/*THIS SHOULD BE BETWEEN THE FIRST AND SECOND RULE*/
h1 {
    color: rgb(128, 64, 32);
}
h1,
h2#Help {
    color: rgb(128, 64, 32);
    background-color: rgb(128, 64, 32);
    border-color: transparent;
}""",
        css_generator.to_string()
        )
        css_generator.to_console()