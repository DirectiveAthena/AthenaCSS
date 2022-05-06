# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaCSS.CssLib.Properties.CSSproperties import *

from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.Url import Url
from AthenaLib.Types.RelativeLength import *
from AthenaLib.Types.AbsoluteLength import *

from AthenaColor import RGB,RGBA,HEX,HEXA,HSV,HSL,CMYK
from AthenaColor.Data.HtmlColors import HtmlColorObjects,HtmlColorTuples


# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSproperties(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    # - Support Functions -
    # ------------------------------------------------------------------------------------------------------------------
    def SubtestFunction(self, PropertyType, cases, PropertyName):
        for value, result, value_printer in cases:
            with self.subTest(value=value, result=result, value_printer=value_printer):
                self.assertEqual(PropertyType(value).value, result)
                self.assertEqual(PropertyType(value).print(), f"{PropertyName} : {value_printer}")
                self.assertEqual(PropertyType(value, important=True).print(), f"{PropertyName} : {value_printer} !important")

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
            #value                  #result                 #value_printer
            (None,                  "ease",                 "ease"),
            ("linear",              "linear",               "linear"),
            ("ease-out",            "ease-out",             "ease-out"),
            (CubicBezier(1,1,1,1),  CubicBezier(1,1,1,1),   "cubic-bezier(1, 1, 1, 1)"),
            (CubicBezier(2,-5,2,5),  CubicBezier(1,-5,1,5), "cubic-bezier(1.0, -5, 1.0, 5)"),
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

    def test_BackgroundAttachment(self):
        PropertyType = background_attachment
        PropertyName = "background-attachment"
        cases = (
            #value              #result             #value_printer
            (None,              "scroll",           "scroll"),
            ("scroll",          "scroll",           "scroll"),
            ("fixed",           "fixed",            "fixed"),
            ("local",           "local",            "local"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_BackgroundColor(self):
        PropertyType = background_color
        PropertyName = "background-color"
        cases = (
            #value              #result             #value_printer
            (None,              "transparent",      "transparent"),
            (RGB(),             RGB(0,0,0),         "rgb(0,0,0)"),
            (HEX("#ff8800"),    RGB(255,136,0),     "rgb(255,136,0)"),
            (HEXA("#ff880001"), RGBA(255,136,0,1),  "rgba(255,136,0,1)"),
            (RGBA(255,136,0,1), RGBA(255,136,0,1),  "rgba(255,136,0,1)"),
            (HSL(152,.9,.4),    RGB(10,194,108),    "rgb(10,194,108)"),
            (HSV(152,.9,.4),    RGB(10,102,59),     "rgb(10,102,59)"),
            (CMYK(0,.1,.87,.2), RGB(204,184,27),    "rgb(204,184,27)"),
            (CMYK(0,.1,.87,.2), RGB(204,184,27),    "rgb(204,184,27)"),
            ("SandyBrown",      RGB(244,164,96),    "rgb(244,164,96)"),
            ("Azure",           RGB(240,255,255),   "rgb(240,255,255)"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
            ("AzureQQQQQ",      ValueError),
            ("AzureQQQQQ",      ValueError),
            (HtmlColorObjects,  TypeError),
            (HtmlColorTuples,   TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_BackgroundClip(self):
        PropertyType = background_clip
        PropertyName = "background-clip"
        cases = (
            #value              #result             #value_printer
            (None,              "border-box",       "border-box"),
            ("padding-box",     "padding-box",      "padding-box"),
            ("content-box",     "content-box",      "content-box"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            ("RAISES_ERROR",    ValueError),
            ("1",               ValueError),
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_BackgroundImage(self):
        PropertyType = background_image
        PropertyName = "background-image"
        cases = (
            #value                          #result                         #value_printer
            (None,                          None,                           "none"),
            ("image/girlfriend.jpg",        'image/girlfriend.jpg',         'url("image/girlfriend.jpg")'),
            (Url("image/girlfriend.jpg"),   'image/girlfriend.jpg',         'url("image/girlfriend.jpg")'),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            (1,                 TypeError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    def test_BackgroundOrigin(self):
        PropertyType = background_origin
        PropertyName = "background-origin"
        cases = (
            #value              #result             #value_printer
            (None,              "padding-box",      "padding-box"),
            ("border-box",      "border-box",       "border-box"),
            ("content-box",     "content-box",      "content-box"),
        )
        self.SubtestFunction(PropertyType,cases,PropertyName)
        casesFail = (
            #value              #error
            (1,                 TypeError),
            ("RAISES ERROR",    ValueError),
        )
        self.SubtestFunctionFails(PropertyType, casesFail)

    # def test_BackgroundPosition(self):
    #     PropertyType = background_position
    #
    #     PropertyName = "background-position"
    #     cases = (
    #         #value                      #result                     #value_printer
    #         (None,                      (Percent(0),Percent(0)),    "0%, 0%"),
    #         ((Percent(5),Percent(9)),   (Percent(5),Percent(9)),    "5%, 9%"),
    #         ((Pixel(5),Pixel(9)),       (Pixel(5),Pixel(9)),        "5px, 9px"),
    #     )
    #
    #     self.SubtestFunction(PropertyType,cases,PropertyName)
    #     casesFail = (
    #         #value              #error
    #         (1,                 TypeError),
    #         ("RAISES ERROR",    ValueError),
    #     )
    #     self.SubtestFunctionFails(PropertyType, casesFail)
    #
