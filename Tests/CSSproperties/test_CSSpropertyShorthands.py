# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaCSS.CssLib.Properties.CSSpropertyShorthand import *
from AthenaCSS.CssLib.Properties.CSSproperties import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSpropertyShorthands(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - Support Functions -
    # ------------------------------------------------------------------------------------------------------------------
    def SubtestFunction(self, PropertyType, cases, PropertyName):
        for args,kwargs, value_printer in cases:
            with self.subTest(args=args,kwargs=kwargs, value_printer=value_printer):
                self.assertEqual(PropertyType(*args,**kwargs).print(), f"{PropertyName}: {value_printer}")
                self.assertEqual(PropertyType(*args,**kwargs, important=True).print(), f"{PropertyName}: {value_printer} !important")

    def SubtestFunctionFails(self, PropertyType, cases):
        for args,kwargs, error in cases:
            with self.subTest(args=args,kwargs=kwargs):
               with self.assertRaises(error):
                    PropertyType(*args, **kwargs)

    # ------------------------------------------------------------------------------------------------------------------
    # - Tests -
    # ------------------------------------------------------------------------------------------------------------------
    def test_Animation(self):
        PropertyType = animation
        PropertyName = "animation"
        cases = (
            # args                                                                                      #kwargs     #result
            ((None,None,None,None,None,None,None,None),                                                 {},         "none 0s ease 0s 1 normal none running"),
            (("TESTING",-500,"linear",100,"infinite","alternate","backwards","paused"),                 {},         "TESTING 500s linear 100s infinite alternate backwards paused"),
            ((animation_name('TESTING'),-500,"linear",100,"infinite","alternate","backwards","paused"), {},         "TESTING 500s linear 100s infinite alternate backwards paused"),
            ("1",                                                                                       {},         "1 0s ease 0s 1 normal none running"), # missing arguments
            (("1",-500),                                                                                {},         "1 500s ease 0s 1 normal none running"), # missing arguments
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)

        casesFail = (
            # args                                              #kwargs                             #error
            ((None,"None",None,None,None,None,None,None),       {},                                 TypeError), # depending on the underlying properties
            ((None, None, None, None, None, None, None, None),  {"a":"a"},                          AttributeError),
            ((None, None, None, None, None, None, None),        {"a":"a"},                          AttributeError),
            ((None, None, None, None, None, None, None),        {"play_state":animation_name()},    TypeError),
        )
        self.SubtestFunctionFails(PropertyType,casesFail)