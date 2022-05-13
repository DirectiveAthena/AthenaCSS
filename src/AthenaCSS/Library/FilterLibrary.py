# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library
from AthenaLib.Types.Math import Percent, Degree
from AthenaLib.Types.AbsoluteLength import Pixel

# Custom Packages
from AthenaCSS.Objects.Properties.CSSproperty import CSSproperty
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic
from AthenaCSS.Library.Support import COLORS_UNION

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__ = [
    "Blur", "Brightness", "Contrast", "DropShadow", "Grayscale", "HueRotate", "Invert", "Opacity", "Saturate","Sepia",
    "FILTERS"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
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