# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
import itertools

# Custom Library
from AthenaLib.Types.Math import Degree
from AthenaLib.Types.AbsoluteLength import Pixel

# Custom Packages
from AthenaCSS.Library.Support import (
    COLORS_UNION, PERCENT, DEGREE,NUMBERS, PIXEL, ANY, TRANSFORM_SPACING, PERCENT_EMPTY, PERCENT_FULL, DEGREE_EMPTY,
    PIXEL_EMPTY
)
from AthenaCSS.Declarations.CSSProperty import SubProp
from AthenaCSS.Declarations.ValueLogic import ValueLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Filters -
# ----------------------------------------------------------------------------------------------------------------------
class Blur(SubProp):
    name="blur"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice=PIXEL,
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Brightness(SubProp):
    name="brightness"
    value_logic = ValueLogic(
        default=PERCENT_FULL,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Contrast(SubProp):
    name="contrast"
    value_logic = ValueLogic(
        default=PERCENT_FULL,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class DropShadow(SubProp):
    name="drop-shadow"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            #h-shadow,  v-shadow,   blur,   spread, color
            (Pixel,     Pixel,      Pixel,  Pixel,  COLORS_UNION):Any,
            None:None
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Grayscale(SubProp):
    name="grayscale"
    value_logic = ValueLogic(
        default=PERCENT_EMPTY,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class HueRotate(SubProp):
    name="hue-rotate"
    value_logic = ValueLogic(
        default=DEGREE_EMPTY,
        value_choice=DEGREE
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Invert(SubProp):
    name="invert"
    value_logic = ValueLogic(
        default=PERCENT_EMPTY,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Opacity(SubProp):
    name="opacity"
    value_logic = ValueLogic(
        default=PERCENT_FULL,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Saturate(SubProp):
    name="saturate"
    value_logic = ValueLogic(
        default=PERCENT_FULL,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Sepia(SubProp):
    name="sepia"
    value_logic = ValueLogic(
        default=PERCENT_EMPTY,
        value_choice=PERCENT
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)

# ----------------------------------------------------------------------------------------------------------------------
# Support for Declarations
# ----------------------------------------------------------------------------------------------------------------------
FILTERS = {
    Blur: Any,
    Brightness: Any,
    Contrast: Any,
    DropShadow: Any,
    Grayscale: Any,
    HueRotate: Any,
    Invert: Any,
    Opacity: Any,
    Saturate: Any,
    Sepia: Any,
}
# ----------------------------------------------------------------------------------------------------------------------
# - Steps -
# ----------------------------------------------------------------------------------------------------------------------
class Steps(SubProp):
    name="steps"
    value_logic = ValueLogic(
        value_choice={
            (int,str):(Any, {"end", "start", ""})
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)

# ----------------------------------------------------------------------------------------------------------------------
# - Transform -
# ----------------------------------------------------------------------------------------------------------------------
class Matrix(SubProp):
    name="matrix"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=6
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Matrix3D(SubProp):
    name="matrix3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=16
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Translate(SubProp):
    name="translate"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=2
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Translate3D(SubProp):
    name="translate3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateX(SubProp):
    name="translateX"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateY(SubProp):
    name="translateY"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateZ(SubProp):
    name="translateZ"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Scale(SubProp):
    name="scale"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=2
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Scale3D(SubProp):
    name="scale3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleX(SubProp):
    name="scaleX"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleY(SubProp):
    name="scaleY"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleZ(SubProp):
    name="scaleZ"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate(SubProp):
    name="rotate"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate3D(SubProp):
    name="rotate3d"
    value_logic = ValueLogic(
        value_choice={
            **{(*number,Degree): Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateX(SubProp):
    name="rotateX"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateY(SubProp):
    name="rotateY"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateZ(SubProp):
    name="rotateZ"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Skew(SubProp):
    name="skew"
    value_logic = ValueLogic(
        value_choice={
            (Degree, Degree): Any
        },
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class SkewX(SubProp):
    name="skewX"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class SkewY(SubProp):
    name="skewY"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Perspective(SubProp):
    name="perspective"
    value_logic = ValueLogic(
        value_choice=ANY,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
# Support for Declarations
# ----------------------------------------------------------------------------------------------------------------------
TRANSFORMS = {
    Matrix: Any,
    Matrix3D: Any,
    Translate: Any,
    Translate3D: Any,
    TranslateX: Any,
    TranslateY: Any,
    TranslateZ: Any,
    Scale: Any,
    Scale3D: Any,
    ScaleX: Any,
    ScaleY: Any,
    ScaleZ: Any,
    Rotate: Any,
    Rotate3D: Any,
    RotateX: Any,
    RotateY: Any,
    RotateZ: Any,
    Skew: Any,
    SkewX: Any,
    SkewY: Any,
    Perspective: Any,
}