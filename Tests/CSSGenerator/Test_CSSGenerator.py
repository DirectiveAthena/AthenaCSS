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
        css_generator = CSSGenerator().add_rule(
            selectors=[CSSElement.H1.classes("something")],
            declarations = {"color": RGB(128, 64, 32)}
        )

        self.assertEqual(
"""h1.something {
    color: rgb(128, 64, 32);
}""",
        css_generator.to_string()
        )
        css_generator.to_console()