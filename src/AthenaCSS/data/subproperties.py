# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
import itertools

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV

# Custom Packages
from AthenaCSS.data.support import (
    COLORS_UNION, PERCENT, DEGREE,NUMBERS, PIXEL, ANY, TRANSFORM_SPACING, PERCENT_EMPTY, PERCENT_FULL, DEGREE_EMPTY,
    PIXEL_EMPTY
)
from AthenaCSS.models.declarations.property_sub import CSSSubProp
from AthenaCSS.models.declarations.value_logic import ValueLogic

from AthenaCSS.models.athenalib_imports import * # all data models from AthenaLib but with correct string casting for CSS

# ----------------------------------------------------------------------------------------------------------------------
# - Filters -
# ----------------------------------------------------------------------------------------------------------------------
class Blur(CSSSubProp):
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
class Brightness(CSSSubProp):
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
class Contrast(CSSSubProp):
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
class DropShadow(CSSSubProp):
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
class Grayscale(CSSSubProp):
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
class HueRotate(CSSSubProp):
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
class Invert(CSSSubProp):
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
class Opacity(CSSSubProp):
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
class Saturate(CSSSubProp):
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
class Sepia(CSSSubProp):
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
# Support for declarations
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
class Steps(CSSSubProp):
    name="steps"
    value_logic = ValueLogic(
        value_choice={
            (int,str):(Any, ("end", "start", ""))
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)

# ----------------------------------------------------------------------------------------------------------------------
# - Transform -
# ----------------------------------------------------------------------------------------------------------------------
class Matrix(CSSSubProp):
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
class Matrix3D(CSSSubProp):
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
class Translate(CSSSubProp):
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
class Translate3D(CSSSubProp):
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
class TranslateX(CSSSubProp):
    name="translateX"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateY(CSSSubProp):
    name="translateY"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateZ(CSSSubProp):
    name="translateZ"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Scale(CSSSubProp):
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
class Scale3D(CSSSubProp):
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
class ScaleX(CSSSubProp):
    name="scaleX"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleY(CSSSubProp):
    name="scaleY"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleZ(CSSSubProp):
    name="scaleZ"
    value_logic = ValueLogic(
        value_choice=NUMBERS,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate(CSSSubProp):
    name="rotate"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate3D(CSSSubProp):
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
class RotateX(CSSSubProp):
    name="rotateX"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateY(CSSSubProp):
    name="rotateY"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateZ(CSSSubProp):
    name="rotateZ"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Skew(CSSSubProp):
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
class SkewX(CSSSubProp):
    name="skewX"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class SkewY(CSSSubProp):
    name="skewY"
    value_logic = ValueLogic(
        value_choice=DEGREE,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Perspective(CSSSubProp):
    name="perspective"
    value_logic = ValueLogic(
        value_choice=ANY,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
# Support for declarations
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
# ----------------------------------------------------------------------------------------------------------------------
class LinearGradient(CSSSubProp):
    name="linear-gradient"
    value_logic = ValueLogic(
        value_choice=ANY,
        printer_space=TRANSFORM_SPACING
    )
    def __init__(self, *value):
        super().__init__(value)
    # custom printer to handle the color/percent pairs
    def printer(self) -> str:
        values = []
        for value in self.value:
            match value:
                case (RGB() | RGBA() | HEX() | HEXA() | HSL() | HSV()) , Percent():
                    values.append(f"{type(value[0]).__name__.lower()}{value[0].export()} {str(value[1])}")
                case _:  # catches all
                    values.append(value)

        if isinstance(values[-1], int):
            return f"{self.name}({', '.join(str(v) for v in values[:-1])}){values[-1]}"
        return f"{self.name}({', '.join(str(v) for v in values)})"