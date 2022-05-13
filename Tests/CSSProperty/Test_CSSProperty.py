# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS.Library.PropertyLibrary import *
import AthenaCSS.Library.FilterLibrary as Filters

from AthenaLib.Types.Time import Second,MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.Math import Percent

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSProperty(BulkTests):

    def test_AlignContent(self):
        # Define a CSSProperty Class with a defined name

        Ac = AlignContent
        cases = (
            #left                                   #right
            (Ac().value_logic.default,              "stretch"),
            (AlignContent.value_logic.default,      "stretch"),
            (repr(Ac()),                            "AlignContent(value='stretch')"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationName(self):
        # Define a CSSProperty Class with a defined name

        An = AnitmationName
        cases = (
            #left                                   #right
            (str(An()),                             "animation-name: none"),
            (str(An("jelp")),                       "animation-name: jelp"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationDuration(self):
        # Define a CSSProperty Class with a defined name

        An = AnitmationDuration
        cases = (
            #left                                   #right
            (str(An()),                             "animation-duration: 0s"),
            (str(An(Second(1))),                    "animation-duration: 1s"),
            (str(An(MilliSecond(1))),               "animation-duration: 1ms"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationTimingFunction(self):
        # Define a CSSProperty Class with a defined name

        An = AnimationTimingFunction
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

        Ani = Animation
        cases = (
            #left                                   #right
            (str(Ani()),                            "animation: none 0s ease 0s 1 normal none running"),
        )
        self.Subtest_Equality(cases)

    def test_BackfaceVisibility(self):
        # Define a CSSProperty Class with a defined name

        Bv = BackfaceVisibility
        cases = (
            #left                                   #right
            (str(Bv()),                             "backface-visibility: visible"),
            (str(Bv("hidden")),                     "backface-visibility: hidden"),
        )
        self.Subtest_Equality(cases)

    def test_BackgroundPosition(self):
        # Define a CSSProperty Class with a defined name

        Bp = BackgroundPosition
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

        Bf = BackdropFilter
        cases = (
            #left                                   #right
            (str(Bf()),                             "backdrop-filter: none"),
            (str(Bf(Filters.Blur(100))),            "backdrop-filter: blur(100px)"),
            (str(Bf(Filters.Brightness(58))),       "backdrop-filter: brightness(58%)"),
            (str(Bf(Filters.Contrast(58))),         "backdrop-filter: contrast(58%)"),
            (str(Bf(Filters.Grayscale(58))),        "backdrop-filter: grayscale(58%)"),
            (str(Bf(Filters.HueRotate(58))),        "backdrop-filter: hue-rotate(58deg)"),
            (str(Bf(Filters.Invert(58))),           "backdrop-filter: invert(58%)"),
            (str(Bf(Filters.Opacity(58))),          "backdrop-filter: opacity(58%)"),
            (str(Bf(Filters.Saturate(58))),         "backdrop-filter: saturate(58%)"),
            (str(Bf(Filters.Sepia(58))),            "backdrop-filter: sepia(58%)"),
        )
        self.Subtest_Equality(cases)

    def test_BackgroundSize(self):
        # Define a CSSProperty Class with a defined name

        Bs = BackgroundSize
        cases = (
            #left                                   #right
            (str(Bs()),                             "background-size: auto"),
            (str(Bs((Percent(100), "auto"))),       "background-size: 100% auto"),
            (str(Bs((Pixel(100), "auto"))),         "background-size: 100px auto"),
            (str(Bs((Pixel(100), Pixel(100)))),     "background-size: 100px 100px"),
        )
        self.Subtest_Equality(cases)