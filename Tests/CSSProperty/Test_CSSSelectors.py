# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
from AthenaCSS.Objects.Selectors.CSSSelector import CSSSelector as Selector

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSSelectors(BulkTests):
    def test_Class1(self):
        self.assertEqual(
            ".test1",
            str(ElementLib.Class("test1"))
        )

    def test_Class2(self):
        self.assertEqual(
            ".test2.test1",
            str(ElementLib.Class("test2", "test1"))
        )

    def test_Class_After(self):
        self.assertEqual(
            ".test2+.name2",
            str(ElementLib.Class("test2").after(ElementLib.Class("name2")))
        )

    def test_Class_Descendant(self):
        self.assertEqual(
            ".clasname1 #idname1",
            str(ElementLib.Class("clasname1").descendant(ElementLib.Id("idname1")))
        )

    def test_Class_Combine1(self):
        selction = Selector(
            ElementLib.Class("clasname1"),
            ElementLib.Id("idname1")
        )
        self.assertEqual(
            ".clasname1,#idname1",
            str(selction)
        )

    def test_Class_Combine2(self):
        selection = Selector(
            ElementLib.Div(ElementLib.Class("clasname1")),
            ElementLib.Id("idname1")
        )

        self.assertEqual(
            "div.clasname1,#idname1",
            str(
                selection
            )
        )

    def test_Class_Complicated1(self):
        element = ElementLib.Div(ElementLib.Class("classname1"))
        elemnt_2 = ElementLib.Id("idname1").descendant(
                ElementLib.Id("idname2")
        )

        selection = Selector(
            element,
            elemnt_2,
            ElementLib.Id("idname3").descendant(
                ElementLib.Id("idname4")
            ),
        )
        self.assertEqual(
            "div.classname1,#idname1 #idname2,#idname3 #idname4",
            str(selection)
        )

        self.assertEqual(
            "div.classname1",
            str(element)
        )

    def test_Div(self):
        self.assertEqual(
            "div",
            str(ElementLib.Div())
        )



    def test_Class_Complicated3(self):
        class_name = ElementLib.Class("name")
        div = ElementLib.Div(class_name)
        paragraph1 = ElementLib.P().child(ElementLib.Div()).child(div)
        paragraph2 = ElementLib.P().child(div)

        selection = Selector(
            class_name,
            paragraph1,
            paragraph2,
        )

        self.assertEqual(
            ".name,p>div>div.name,p>div.name",
            str(selection)
        )

    def test_Attribute1(self):
        self.assertEqual(
            "div[attr_name]",
            str(ElementLib.Div(ElementLib.Attribute("attr_name")))
        )

    def test_Attribute2(self):
        self.assertEqual(
            "div[attr_name][attr_2]",
            str(
                ElementLib.Div(
                    ElementLib.Attribute("attr_name"),
                    ElementLib.Attribute("attr_2")
                )
            )
        )

    def test_Attribute3(self):
        self.assertEqual(
            'div[attr_name][attr_2="something"]',
            str(
                ElementLib.Div(
                    ElementLib.Attribute("attr_name"),
                    ElementLib.Attribute.equals("attr_2", "something")
                )
            )
        )

    def test_Attribute4(self):
        self.assertEqual(
            'div[attr_name][attr_2~="something"]',
            str(
                ElementLib.Div(
                    ElementLib.Attribute("attr_name"),
                    ElementLib.Attribute.contains_word("attr_2", "something")
                )
            )
        )

    def test_DoubleColon(self):
        self.assertEqual(
            'a:active',
            str(
                ElementLib.A(
                    ElementLib.colon_Active(),
                )
            )
        )