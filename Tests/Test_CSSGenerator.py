# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom data
from AthenaColor import RGB
from AthenaCSS.models.generator import CSSGenerator
from AthenaLib.HTML.models.css import CSSProperty, CSSComment, CSSRule, CSSSelection, CSSSelectionType
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSGenerators(BulkTests):
    def test_CSSGenerator0(self):
        css_generator = CSSGenerator().add_rule(
            selections=(CSSSelection(HtmlLib.H1(classes="something"))),
            properties=CSSProperty(name="color", value=RGB(128, 64, 32))
        )

        self.assertEqual(
"""h1.something {
    color: rgb(128,64,32);
}""",
        css_generator.to_text()
        )

    def test_CSSGenerator1(self):
        css_generator = CSSGenerator().add_rule(
            selections=(
                CSSSelection(HtmlLib.H1(classes="something")),
                CSSSelection(HtmlLib.H2(classes="something_else")),
                CSSSelection(HtmlLib.H2(classes=("something_else","Something_totaly","different")))
            ),
            properties=CSSProperty(name="color", value=RGB(128, 64, 32))
        ).add_comment(
            "THIS SHOULD BE BETWEEN THE FIRST AND SECOND RULE"
        ).add_rule(
            selections=(
                CSSSelection(HtmlLib.H1(),HtmlLib.H2() ,selector_type=CSSSelectionType.family),
                CSSSelection(HtmlLib.H2(id_str="HelpMe"))
            ),
            properties=(
                CSSProperty(name="color", value=RGB(128, 64, 32)),
                CSSProperty(name="background-color", value=RGB(128, 64, 32)),
                CSSProperty(name="border-color", value="transparent")
            )
        )

        self.assertEqual(
"""h1.something,
h2.something_else,
h2.something_else.Something_totaly.different {
    color: rgb(128,64,32);
}
/* THIS SHOULD BE BETWEEN THE FIRST AND SECOND RULE */
h1>h2,
h2#HelpMe {
    color: rgb(128,64,32);
    background-color: rgb(128,64,32);
    border-color: transparent;
}""",
        css_generator.to_text()
        )