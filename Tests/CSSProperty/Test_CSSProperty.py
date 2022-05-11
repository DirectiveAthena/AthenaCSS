# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaCSS.Lib.PropertyLibrary import *
from AthenaLib.Types.Time import Second,MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.AbsoluteLength import Pixel
from AthenaLib.Types.RelativeLength import Percent

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
            (Ac().default,                          "stretch"),
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
            (str(Bp((Percent(1), Percent(1)))),"background-position: 1% 1%"),
            (str(Bp((Pixel(1), Pixel(1)))),"background-position: 1px 1px"),
            (str(Bp((Percent(1), "center"))),"background-position: 1% center"),
            (str(Bp((Pixel(1), "center"))),"background-position: 1px center"),
            (str(Bp("center")),"background-position: center"),
        )
        self.Subtest_Equality(cases)

        casesFail=(
            ((1,1), TypeError),
            ((1,"center"), TypeError),
        )
        self.Subtest_Fail(Bp, casesFail)