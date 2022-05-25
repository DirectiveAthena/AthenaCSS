# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
import AthenaColor
from AthenaCSS.Objects.ElementSelection.CSSAttribute import CSSAttribute
from AthenaCSS.Objects.ElementSelection.CSSClass import CSSClass
from AthenaCSS.Objects.ElementSelection.CSSId import CSSId
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection
import AthenaCSS.Library.PropertyLibrary as PropertyLibrary
import AthenaCSS.Library.SubPropertyLibrary as Filters
from AthenaCSS.Objects.Printer.CSSPrinter import CSSPrinter

from AthenaLib.Types.Time import Second,MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Percent

from AthenaColor import RGB

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSPrinting(BulkTests):
    def styling_setup(self):
        # SELECTION of the objects
        with (nested_selection := CSSSelection()) as s_:
            s_.add_following(
                ElementLib.H1,
                ElementLib.P(
                    ElementLib.PseudoFirstLine
                )
            )

        with (selection := CSSSelection()) as s:
            s.add_descendants(
                CSSClass("post"),
                nested_selection
            )

        styling = (
            PropertyLibrary.Color(RGB(255,128,52)),
            PropertyLibrary.BackgroundColor(RGB(0,0,0))
        )

        return selection, styling

    def test_CSSPrinter_OneLine(self):
        selection,styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
            one_line= True
        )
        with printer as p:
            p.add_style(
                selection=selection,
                styling=styling
            )

        self.assertEqual(
            ".post h1+p::first-line{color: rgb(255, 128, 52);background-color: rgb(0, 0, 0);}",
            printer.to_string()
        )

    def test_CSSPrinter_Full(self):
        selection, styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
        )
        with printer as p:
            p.add_style(
                selection=selection,
                styling=styling
            )

        self.assertEqual(
            ".post h1+p::first-line{\n    color: rgb(255, 128, 52);\n    background-color: rgb(0, 0, 0);\n}\n\n",
            printer.to_string()
        )

    def test_CSSPrinter_OneLineComment(self):
        selection, styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
            one_line=True
        )
        with printer as p:
            p.add_comment("This is a comment.\nTo test comment formatting")
            p.add_style(
                selection=selection,
                styling=styling
            )

        self.assertEqual(
            "/*This is a comment. To test comment formatting*/.post h1+p::first-line{color: rgb(255, 128, 52);background-color: rgb(0, 0, 0);}",
            printer.to_string()
        )

    def test_CSSPrinter_FullComment(self):
        selection, styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
        )
        with printer as p:
            p.add_comment("This is a comment.\nTo test comment formatting")
            p.add_style(
                selection=selection,
                styling=styling
            )

        self.assertEqual(
            "/*This is a comment.*/\n/*To test comment formatting*/\n.post h1+p::first-line{\n    color: rgb(255, 128, 52);\n    background-color: rgb(0, 0, 0);\n}\n\n",
            printer.to_string()
        )

    def test_CSSPrinter_FullCommentLines(self):
        selection, styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
        )
        with printer as p:
            p.add_line(),
            p.add_seperation(),
            p.add_comment("This is a comment.\nTo test comment formatting"),
            p.add_seperation(),
            p.add_style(
                selection=selection,
                styling=styling
            )

        self.assertEqual(
f"""
/*{"-"*255}*/
/*This is a comment.*/
/*To test comment formatting*/
/*{"-"*255}*/
.post h1+p::first-line{{
    color: rgb(255, 128, 52);
    background-color: rgb(0, 0, 0);
}}

""",
            printer.to_string()
        )

    def test_CSSPrinter_NoComments(self):
        selection, styling = self.styling_setup()

        # Define the printer and populate with styling
        printer = CSSPrinter(
            indentation=4,
            comments=False
        )
        with printer as p:
            p.add_line(),
            p.add_seperation(),
            p.add_comment("This is a comment.\nTo test comment formatting"),
            p.add_seperation(),
            p.add_style(
                selection=selection,
                styling=styling,
                comment="THIS SHOULD NOT APPEAER"
            )

        self.assertEqual(
r"""
.post h1+p::first-line{
    color: rgb(255, 128, 52);
    background-color: rgb(0, 0, 0);
}

""",
            printer.to_string()
        )