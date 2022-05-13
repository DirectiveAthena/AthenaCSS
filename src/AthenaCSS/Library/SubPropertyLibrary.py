# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
import itertools

# Custom Library
from AthenaLib.Types.Math import Percent, Degree
from AthenaLib.Types.AbsoluteLength import Pixel

# Custom Packages
from AthenaCSS.Objects.Properties.CSSproperty import CSSproperty
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic
from AthenaCSS.Library.Support import COLORS_UNION

# ----------------------------------------------------------------------------------------------------------------------
# - Filter -
# ----------------------------------------------------------------------------------------------------------------------
class Filter(CSSproperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"

# ----------------------------------------------------------------------------------------------------------------------
class Blur(Filter):
    name="blur"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            Pixel:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Brightness(Filter):
    name="brightness"
    value_logic = ValueLogic(
        default=Percent(100),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Contrast(Filter):
    name="contrast"
    value_logic = ValueLogic(
        default=Percent(100),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class DropShadow(Filter):
    name="drop-shadow"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            #h-shadow,  v-shadow,   blur,   spread, color
            (Pixel,     Pixel,      Pixel,  Pixel,  COLORS_UNION):(Any,Any,Any,Any,Any),
            None:None
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Grayscale(Filter):
    name="grayscale"
    value_logic = ValueLogic(
        default=Percent(0),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class HueRotate(Filter):
    name="hue-rotate"
    value_logic = ValueLogic(
        default=Degree(0),
        value_choice={
            Degree:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Invert(Filter):
    name="invert"
    value_logic = ValueLogic(
        default=Percent(0),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Opacity(Filter):
    name="opacity"
    value_logic = ValueLogic(
        default=Percent(100),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Saturate(Filter):
    name="saturate"
    value_logic = ValueLogic(
        default=Percent(100),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)

    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"
# ----------------------------------------------------------------------------------------------------------------------
class Sepia(Filter):
    name="sepia"
    value_logic = ValueLogic(
        default=Percent(0),
        value_choice={
            Percent:Any,
        },
    )
    def __init__(self, value=value_logic.default):
        if isinstance(value, (int, float)):
            value = type(self.value_logic.default)(value)
        super().__init__(value)

# ----------------------------------------------------------------------------------------------------------------------
# - Steps -
# ----------------------------------------------------------------------------------------------------------------------
class Other(CSSproperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"

# ----------------------------------------------------------------------------------------------------------------------
class Steps(Other):
    name="steps"
    value_logic = ValueLogic(
        value_choice={
            (int,str):(Any, {"end", "start", ""})
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)

# ----------------------------------------------------------------------------------------------------------------------
# Support for Properties
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
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Transform(CSSproperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"

# ----------------------------------------------------------------------------------------------------------------------
class Matrix(Transform):
    name="matrix"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=6
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Matrix3D(Transform):
    name="matrix3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=16
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Translate(Transform):
    name="translate"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=2
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Translate3D(Transform):
    name="translate3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateX(Transform):
    name="translateX"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateY(Transform):
    name="translateY"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class TranslateZ(Transform):
    name="translateZ"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Scale(Transform):
    name="scale"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=2
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Scale3D(Transform):
    name="scale3d"
    value_logic = ValueLogic(
        value_choice={
            **{number: Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleX(Transform):
    name="scaleX"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleY(Transform):
    name="scaleY"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class ScaleZ(Transform):
    name="scaleZ"
    value_logic = ValueLogic(
        value_choice={
            int:Any,
            float:Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate(Transform):
    name="rotate"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Rotate3D(Transform):
    name="rotate3d"
    value_logic = ValueLogic(
        value_choice={
            **{(*number,Degree): Any for number in itertools.product(
                (int, float),
                repeat=3
            )}
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateX(Transform):
    name="rotateX"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateY(Transform):
    name="rotateY"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class RotateZ(Transform):
    name="rotateZ"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Skew(Transform):
    name="skew"
    value_logic = ValueLogic(
        value_choice={
            (Degree, Degree): Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class SkewX(Transform):
    name="skewX"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class SkewY(Transform):
    name="skewY"
    value_logic = ValueLogic(
        value_choice={
            Degree: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class Perspective(Transform):
    name="perspective"
    value_logic = ValueLogic(
        value_choice={
            Any: Any
        },
        printer_space=", "
    )
    def __init__(self, value):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
# Support for Properties
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