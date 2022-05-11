# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from BulkTests import BulkTests
from AthenaCSS.Properties.CSSproperty_Lib import *

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSProperty(BulkTests):

    # noinspection PyUnreachableCode
    def test_PropertySetup(self):
        # Define a CSSProperty Class with a defined name

        Ac = align_content()
        cases = (
            #left                                   #right
            (Ac._value_logic.default,               "stretch"),
            (align_content._value_logic.default,    "stretch"),
            (Ac.default,                            "stretch"),
        )

        self.Subtest_Equality(cases)

        # Define a default value
        self.fail()

        # Define the Value range
        self.fail()

        # Define a value
        self.fail()

        # Print the value
        self.fail()