# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom data
import AthenaCSS
from AthenaCSS import *

# Custom Packages
from BulkTests import BulkTests
from AthenaCSS.models.athenalib_imports import * # all data models from AthenaLib but with correct string casting for CSS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSProperty(BulkTests):
    def test_AlignContent(self):
        # Define a CSSProperty Class with a defined name

        Ac = Property.AlignContent
        cases = (
            #left                                   #right
            (Ac().value_logic.default,              "stretch"),
            (Ac.value_logic.default,      "stretch"),
            (repr(Ac()),                            "AlignContent(value='stretch')"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationName(self):
        # Define a CSSProperty Class with a defined name

        An = Property.AnimationName
        cases = (
            #left                                   #right
            (str(An()),                             "animation-name: none"),
            (str(An("help")),                       "animation-name: help"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationDuration(self):
        # Define a CSSProperty Class with a defined name

        An = Property.AnimationDuration
        cases = (
            #left                                   #right
            (str(An()),                             "animation-duration: 0s"),
            (str(An(Second(1))),                    "animation-duration: 1s"),
            (str(An(MilliSecond(1))),               "animation-duration: 1ms"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationTimingFunction(self):
        # Define a CSSProperty Class with a defined name

        An = Property.AnimationTimingFunction
        cases = (
            #left                                   #right
            (str(An()),                             "animation-timing-function: ease"),
            (str(An("linear")),                     "animation-timing-function: linear"),
            (str(An("ease-out")),                   "animation-timing-function: ease-out"),
            (str(An(CubicBezier(1,1,1,1))),         "animation-timing-function: cubic-bezier(1, 1, 1, 1)"),
        )
        self.Subtest_Equality(cases)

    def test_Animation(self):
        # Define a CSSProperty Class with a defined name

        Ani = Property.Animation
        cases = (
            #left                                   #right
            (str(Ani()),                            "animation: none 0s ease 0s 1 normal none running"),
        )
        self.Subtest_Equality(cases)

    def test_BackfaceVisibility(self):
        # Define a CSSProperty Class with a defined name

        Bv = Property.BackfaceVisibility
        cases = (
            #left                                   #right
            (str(Bv()),                             "backface-visibility: visible"),
            (str(Bv("hidden")),                     "backface-visibility: hidden"),
        )
        self.Subtest_Equality(cases)

    def test_BackgroundPosition(self):
        # Define a CSSProperty Class with a defined name

        Bp = Property.BackgroundPosition
        cases = (
            #left                                   #right
            (str(Bp()),                             "background-position: 0% 0%"),
            (str(Bp((Percent(1), Percent(1)))),     "background-position: 1% 1%"),
            (str(Bp((Pixel(1), Pixel(1)))),         "background-position: 1px 1px"),
            (str(Bp((Percent(1), "center"))),       "background-position: 1% center"),
            (str(Bp((Pixel(1), "center"))),         "background-position: 1px center"),
            (str(Bp("center")),                     "background-position: center"),
        )
        self.Subtest_Equality(cases)

        casesFail=(
            ((1,1), TypeError),
            ((1,"center"), TypeError),
        )
        self.Subtest_Fail(Bp, casesFail)

    def test_BackdropFilter(self):
        # Define a CSSProperty Class with a defined name

        Bf = Property.BackdropFilter
        cases = (
            #left                                   #right
            (str(Bf()),                             "backdrop-filter: none"),
            (str(Bf(SubProperty.Blur(100))),        "backdrop-filter: blur(100px)"),
            (str(Bf(SubProperty.Brightness(58))),   "backdrop-filter: brightness(58%)"),
            (str(Bf(SubProperty.Contrast(58))),     "backdrop-filter: contrast(58%)"),
            (str(Bf(SubProperty.Grayscale(58))),    "backdrop-filter: grayscale(58%)"),
            (str(Bf(SubProperty.HueRotate(58))),    "backdrop-filter: hue-rotate(58deg)"),
            (str(Bf(SubProperty.Invert(58))),       "backdrop-filter: invert(58%)"),
            (str(Bf(SubProperty.Opacity(58))),      "backdrop-filter: opacity(58%)"),
            (str(Bf(SubProperty.Saturate(58))),     "backdrop-filter: saturate(58%)"),
            (str(Bf(SubProperty.Sepia(58))),        "backdrop-filter: sepia(58%)"),
        )
        self.Subtest_Equality(cases)

    def test_BackgroundSize(self):
        # Define a CSSProperty Class with a defined name

        Bs = Property.BackgroundSize
        cases = (
            #left                                   #right
            (str(Bs()),                             "background-size: auto"),
            (str(Bs((Percent(100), "auto"))),       "background-size: 100% auto"),
            (str(Bs((Pixel(100), "auto"))),         "background-size: 100px auto"),
            (str(Bs((Pixel(100), Pixel(100)))),     "background-size: 100px 100px"),
        )
        self.Subtest_Equality(cases)