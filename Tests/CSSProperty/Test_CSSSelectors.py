# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
from AthenaCSS.Objects.ElementSelection.CSSAttribute import CSSAttribute
from AthenaCSS.Objects.ElementSelection.CSSClass import CSSClass
from AthenaCSS.Objects.ElementSelection.CSSId import CSSId
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSSelectors(BulkTests):
    def test_CSSSelection0(self):
        div = ElementLib.Div(CSSClass("name"))
        selection = CSSSelection()
        with selection as s:
            s.add(div)

        self.assertEqual(
            "div.name",
            str(selection)
        )

    def test_CSSSelection1(self):
        with (nested_selection := CSSSelection()) as s_:
            s_.add_following(
                ElementLib.H1(),
                ElementLib.P(ElementLib.PseudoFirstLine())
            )

        with (selection := CSSSelection()) as s:
            s.add_descendants(
                CSSClass("post"),
                nested_selection
            )

        self.assertEqual(
            ".post h1+p::first-line",
            str(selection)
        )

    def test_CSSSelection2(self):
        with (selection := CSSSelection()) as s:
            s.add_childeren(
                ElementLib.Div(CSSClass("post")),
                ElementLib.P(ElementLib.PseudoFirstChild(),ElementLib.PseudoFirstLine())
            )

        self.assertEqual(
            "div.post>p:first-child::first-line",
            str(selection)
        )