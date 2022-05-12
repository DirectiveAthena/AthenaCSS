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

        Ac = align_content
        cases = (
            #left                                   #right
            (Ac().value_logic.default,              "stretch"),
            (align_content.value_logic.default,     "stretch"),
            (repr(Ac()),                            "align_content(value='stretch')"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationName(self):
        # Define a CSSProperty Class with a defined name

        An = animation_name
        cases = (
            #left                                   #right
            (str(An()),                             "animation-name: none"),
            (str(An("jelp")),                       "animation-name: jelp"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationDuration(self):
        # Define a CSSProperty Class with a defined name

        An = animation_duration
        cases = (
            #left                                   #right
            (str(An()),                             "animation-duration: 0s"),
            (str(An(Second(1))),                    "animation-duration: 1s"),
            (str(An(MilliSecond(1))),               "animation-duration: 1ms"),
        )
        self.Subtest_Equality(cases)

    def test_AnimationTimingFunction(self):
        # Define a CSSProperty Class with a defined name

        An = animation_timing_function
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

        Ani = animation
        cases = (
            #left                                   #right
            (str(Ani()),                            "animation: none 0s ease 0s 1 normal none running"),
        )
        self.Subtest_Equality(cases)

    def test_BackfaceVisibility(self):
        # Define a CSSProperty Class with a defined name

        Bv = backface_visibility
        cases = (
            #left                                   #right
            (str(Bv()),                             "backface-visibility: visible"),
            (str(Bv("hidden")),                     "backface-visibility: hidden"),
        )
        self.Subtest_Equality(cases)

    def test_BackgroundPosition(self):
        # Define a CSSProperty Class with a defined name

        Bp = background_position
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

        Bf = backdrop_filter
        cases = (
            #left                                   #right
            (str(Bf()),                             "backdrop-filter: none"),
            (str(Bf(Filters.blur(100))),            "backdrop-filter: blur(100px)"),
            (str(Bf(Filters.brightness(58))),       "backdrop-filter: brightness(58%)"),
            (str(Bf(Filters.contrast(58))),         "backdrop-filter: contrast(58%)"),
            (str(Bf(Filters.grayscale(58))),        "backdrop-filter: grayscale(58%)"),
            (str(Bf(Filters.hue_rotate(58))),       "backdrop-filter: hue-rotate(58deg)"),
            (str(Bf(Filters.invert(58))),           "backdrop-filter: invert(58%)"),
            (str(Bf(Filters.opacity(58))),          "backdrop-filter: opacity(58%)"),
            (str(Bf(Filters.saturate(58))),         "backdrop-filter: saturate(58%)"),
            (str(Bf(Filters.sepia(58))),            "backdrop-filter: sepia(58%)"),
        )
        self.Subtest_Equality(cases)