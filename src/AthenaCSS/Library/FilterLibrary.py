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
    "blur", "brightness", "contrast", "drop_shadow", "grayscale", "hue_rotate", "invert", "opacity", "saturate","sepia"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Filter(CSSproperty):
    def printer(self) -> str:
        return f"{self.name}({self._value.printer()})"

# ----------------------------------------------------------------------------------------------------------------------
class blur(Filter):
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
class brightness(Filter):
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
class contrast(Filter):
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
class drop_shadow(Filter):
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
class grayscale(Filter):
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
class hue_rotate(Filter):
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
class invert(Filter):
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
class opacity(Filter):
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
class saturate(Filter):
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
class sepia(Filter):
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