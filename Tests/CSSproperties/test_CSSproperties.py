# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages
from AthenaCSS.CssLib.Properties.CSSproperties import *
from AthenaCSS.CssLib.Types import Second,MilliSecond

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperties_Full(unittest.TestCase):

    def SubtestFunction(self, PropertyType, cases, PropertyName):
        for value, result, value_printer in cases:
            with self.subTest(value=value, result=result, value_printer=value_printer):
                if value is not None:
                    if not isinstance(value, PropertyType.possibleValueTypes):
                        with self.assertRaises(TypeError):
                            PropertyType(value)
                        continue # Continue to next case, else the code below fill fail the test

                    if PropertyType.possibleValues is not None and value not in PropertyType.possibleValues:
                        with self.assertRaises(ValueError):
                            PropertyType(value)
                        continue # Continue to next case, else the code below fill fail the test

                self.assertEqual(PropertyType(value).value, result)
                self.assertEqual(PropertyType(value).print(), f"{PropertyName}: {value_printer}")
                self.assertEqual(PropertyType(value, important=True).print(), f"{PropertyName}: {value_printer} !important")

    def test_AlignContent(self):
        PropertyType = align_content
        PropertyName = "align-content"
        cases = (
            #value          #result         #value_printer
            (None,          "stretch",      "stretch"),
            ("flex-start",  "flex-start",   "flex-start"),
            ("RAISES_ERROR",None,           None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

    def test_AlignItems(self):
        PropertyType = align_items
        PropertyName = "align-items"
        cases = (
            #value          #result     #value_printer
            (None,          "stretch",  "stretch"),
            ("baseline",    "baseline", "baseline"),
            ("RAISES_ERROR",None,       None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

    def test_AlignSelf(self):
        PropertyType = align_self
        PropertyName = "align-self"
        cases = (
            #value          #result     #value_printer
            (None,          "auto",     "auto"),
            ("baseline",    "baseline", "baseline"),
            ("RAISES_ERROR",None,       None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

    def test_AnimationName(self):
        PropertyType = animation_name
        PropertyName = "animation-name"
        cases = (
            #value          #result     #value_printer
            (None,          None,       "none"),
            ("TESTING",     "TESTING",  "TESTING"),
            (1,             None,       None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

    def test_AnimationDuration(self):
        PropertyType = animation_duration
        PropertyName = "animation-duration"
        cases = (
            #value              #result         #value_printer
            (None,              Second(0),      "0s"),
            (Second(10),        Second(10),     "10s"),
            (MilliSecond(10),   MilliSecond(10),"10ms"),
            (1,                 Second(1),      "1s"),
            (0,                 0,              "0"),
            ("1",               None,           None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

    def test_AnimationTimingFunction(self):
        PropertyType = animation_timing_function
        PropertyName = "animation-timing-function"
        cases = (
            #value              #result         #value_printer
            (None,              "ease",         "ease"),
            ("linear",          "linear",       "linear"),
            ("ease-out",        "ease-out",     "ease-out"),
            ("1",               None,           None),# should raise error
            (1,                 None,           None),# should raise error
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)