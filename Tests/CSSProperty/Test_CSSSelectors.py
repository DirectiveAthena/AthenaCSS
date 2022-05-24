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
        selection = CSSSelection(div)

        self.assertEqual(
            "div.name",
            str(selection)
        )
        self.assertEqual(
            "div.name",
            str(div)
        )
    def test_CSSSelection1(self):
        div = ElementLib.Div(CSSClass("name"), CSSId("active"))
        selection = CSSSelection(div)

        self.assertEqual(
            "div.name#active",
            str(selection)
        )
        self.assertEqual(
            "div.name#active",
            str(div)
        )
    def test_CSSSelection2(self):
        div = ElementLib.Div(CSSClass("name"), CSSId("active"), CSSAttribute.equals("pressed", True))
        selection = CSSSelection(div)

        self.assertEqual(
            "div.name#active[pressed=True]",
            str(selection)
        )
        self.assertEqual(
            "div.name#active[pressed=True]",
            str(div)
        )
    def test_CSSSelection3(self):
        div1 = ElementLib.Div(CSSClass("name"))
        div2 = ElementLib.Div(CSSClass("place"))
        selection = CSSSelection(div1).preceding(
            div2
        )

        self.assertEqual(
            "div.name~div.place",
            str(selection)
        )
    def test_CSSSelection4(self):
        div1 = ElementLib.Div(CSSClass("name"))
        div2 = ElementLib.Div(CSSClass("place"))
        selection = CSSSelection().combine(
            div1,
            div2
        )

        self.assertEqual(
            "div.name,div.place",
            str(selection)
        )
