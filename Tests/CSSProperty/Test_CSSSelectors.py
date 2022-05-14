# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSProperty(BulkTests):
    def test_structure(self):
        self.fail()
        
        class1 = Selector.Class("test1")
        class2 = Selector.Class("test2")

        selection1 = Selection(class1, class2)
        self.assertEqual(str(selection1), ".test1, .test2")

        selection2 = Selection(class1, class2, sep="")
        self.assertEqual(str(selection2), ".test1.test2")

        selection3 = Selection(class1, class2, sep=" ")
        self.assertEqual(str(selection3), ".test1 .test2")

        selection4 = Selection(class1, class2, sep=">")
        self.assertEqual(str(selection4), ".test1>.test2")

        selection4 = Selection(class1, class2, sep="+")
        self.assertEqual(str(selection4), ".test1+.test2")

        selection4 = Selection(class1, class2, sep="~")
        self.assertEqual(str(selection4), ".test1~.test2")

        attribute1 = Selector.Attribute("attr1")
        self.assertEqual(str(attribute1), "[attr1]")

        attribute2 = Selector.Attribute("attr2", "something")
        self.assertEqual(str(attribute2), '[attr2="something"]')

        attribute3 = Selector.Attribute("attr2", "something", contain=True)
        self.assertEqual(str(attribute3), '[attr2~="something"]')

        selection5 = Selection(class1, attribute2, sep="~")
        self.assertEqual(str(selection5), '.test1~[attr2="something"]')

        selection6 = Selection(selection3, selection5, sep=", ")
        self.assertEqual(str(selection6), '.test1 .test2, .test1~[attr2="something"]')
