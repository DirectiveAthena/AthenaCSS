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

    # ----------------------------------------------------------------------------------------------------------------------
    # - Support Functions -
    # ----------------------------------------------------------------------------------------------------------------------
    def SubtestFunction(self, PropertyType, cases, PropertyName):
        for value, result, value_printer in cases:
            with self.subTest(value=value, result=result, value_printer=value_printer):
                self.assertEqual(PropertyType(value).value, result)
                self.assertEqual(PropertyType(value).print(), f"{PropertyName}: {value_printer}")
                self.assertEqual(PropertyType(value, important=True).print(), f"{PropertyName}: {value_printer} !important")

    def SubtestFunctionFails(self, PropertyType, cases):
        for value, error in cases:
            with self.subTest(value=value, error=error):
               with self.assertRaises(error):
                    PropertyType(value)

    # ----------------------------------------------------------------------------------------------------------------------
    # - TESTS -
    # ----------------------------------------------------------------------------------------------------------------------
    def test_AlignContent(self):
        PropertyType = align_content
        PropertyName = "align-content"
        cases = (
            #value          #result         #value_printer
            (None,          "stretch",      "stretch"),
            ("flex-start",  "flex-start",   "flex-start"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AlignItems(self):
        PropertyType = align_items
        PropertyName = "align-items"
        cases = (
            #value          #result     #value_printer
            (None,          "stretch",  "stretch"),
            ("baseline",    "baseline", "baseline"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AlignSelf(self):
        PropertyType = align_self
        PropertyName = "align-self"
        cases = (
            #value              #result     #value_printer
            (None,              "auto",     "auto"),
            ("baseline",        "baseline", "baseline"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationName(self):
        PropertyType = animation_name
        PropertyName = "animation-name"
        cases = (
            #value          #result     #value_printer
            (None,          None,       "none"),
            ("TESTING",     "TESTING",  "TESTING"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationDuration(self):
        PropertyType = animation_duration
        PropertyName = "animation-duration"
        cases = (
            #value              #result         #value_printer
            (None,              Second(0),      "0s"),
            (Second(10),        Second(10),     "10s"),
            (MilliSecond(10),   MilliSecond(10),"10ms"),
            (1,                 Second(1),      "1s"),
            (0,                 Second(0),      "0s"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    TypeError),
            ("1",               TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationTimingFunction(self):
        PropertyType = animation_timing_function
        PropertyName = "animation-timing-function"
        cases = (
            #value              #result         #value_printer
            (None,              "ease",         "ease"),
            ("linear",          "linear",       "linear"),
            ("ease-out",        "ease-out",     "ease-out"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationDelay(self):
        PropertyType = animation_delay
        PropertyName = "animation-delay"
        cases = (
            #value              #result         #value_printer
            (None,              Second(0),      "0s"),
            (Second(10),        Second(10),     "10s"),
            (MilliSecond(10),   MilliSecond(10),"10ms"),
            (-1,                Second(-1),     "-1s"),
            (0,                 0,              "0"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    TypeError),
            ("1",               TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationIterationCount(self):
        PropertyType = animation_iteration_count
        PropertyName = "animation-iteration-count"
        cases = (
            #value              #result             #value_printer
            (None,              1,                  "1"),
            ("infinite",        "infinite",         "infinite"),
            (100,               100,                "100"),
            (-100,              100,                "100"),
            (1,                 1,                  "1"),
            (0,                 0,                  "0"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationDirection(self):
        PropertyType = animation_direction
        PropertyName = "animation-direction"
        cases = (
            #value              #result             #value_printer
            (None,              "normal",           "normal"),
            ("alternate",       "alternate",        "alternate"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationFillMode(self):
        PropertyType = animation_fill_mode
        PropertyName = "animation-fill-mode"
        cases = (
            #value              #result             #value_printer
            (None,              None,               "none"),
            ("backwards",       "backwards",        "backwards"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_AnimationPlayState(self):
        PropertyType = animation_play_state
        PropertyName = "animation-play-state"
        cases = (
            #value              #result             #value_printer
            (None,              "running",          "running"),
            ("running",         "running",          "running"),
            ("paused",          "paused",           "paused"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_Animation(self):
        PropertyType = animation
        PropertyName = "animation"
        cases = (
            (
                (None,None,None,None,None,None,None,None),
                "none 0s ease 0s 1 normal none running"
            ),
            (
                ("TESTING",-500,"linear",100,"infinite","alternate","backwards","paused"),
                "TESTING 500s linear 100s infinite alternate backwards paused"
            ),
            (
                (animation_name('TESTING'),-500,"linear",100,"infinite","alternate","backwards","paused"),
                "TESTING 500s linear 100s infinite alternate backwards paused"
            ),
        )
        for value, value_printer in cases:
            with self.subTest(value=value, value_printer=value_printer):
                self.assertEqual(PropertyType(*value).print(), f"{PropertyName}: {value_printer}")
                self.assertEqual(PropertyType(*value, important=True).print(), f"{PropertyName}: {value_printer} !important")

        casesFail = (
            # args                                              #kwargs                             #error
            ((None,"None",None,None,None,None,None,None),       {},                                 TypeError), # depending on the underlying properties
            ("1",                                               {},                                 TypeError), # missing arguments
            ((None, None, None, None, None, None, None, None),  {"a":"a"},                          AttributeError),
            ((None, None, None, None, None, None, None),        {"play_state":animation_name()},    TypeError),
        )
        for args,kwargs , error in casesFail:
            with self.subTest(args=args, kwargs=kwargs,error=error):
                with self.assertRaises(error):
                    PropertyType(*args, **kwargs)

    def test_BackfaceVisibility(self):
        PropertyType = backface_visibility
        PropertyName = "backface-visibility"
        cases = (
            #value              #result             #value_printer
            (None,              "visible",          "visible"),
            ("visible",         "visible",          "visible"),
            ("hidden",          "hidden",           "hidden"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)