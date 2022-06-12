# ----------------------------------------------------------------------------------------------------------------------
# - WHY? -
# ----------------------------------------------------------------------------------------------------------------------
#
# Before this file, all string casting was directly implmented into AthenaLib
#   which created some problems when starting with the AthenaGuiLib package
#   as it needed some classes stated below with different string casters.
# This is why I decided to go the route of creating string casters for each seperate thing.
# Maybe in the future, this might be joined together for those classes which have a same string casting,
#   but for now, this file does everything it needs to do.
#
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.models.length_relative import (
ElementFontSize as AthenaLib_ElementFontSize,
ElementFontHeight as AthenaLib_ElementFontHeight,
ZeroCharacterWidth as AthenaLib_ZeroCharacterWidth,
RootElementFontSize as AthenaLib_RootElementFontSize,
ViewportWidthPercent as AthenaLib_ViewportWidthPercent,
ViewportHeightPercent as AthenaLib_ViewportHeightPercent,
ViewportLargerPercent as AthenaLib_ViewportLargerPercent,
ViewportSmallerPercent as AthenaLib_ViewportSmallerPercent
)
from AthenaLib.models.length_absolute import (
    Pixel as AthenaLib_Pixel,
    Pica as AthenaLib_Pica,
    Point as AthenaLib_Point,
    Inch as AthenaLib_Inch,
    Meter as AthenaLib_Meter,
    DeciMeter as AthenaLib_DeciMeter,
    CentiMeter as AthenaLib_CentiMeter,
    MilliMeter as AthenaLib_MilliMeter
)
from AthenaLib.models.degree import Degree as AthenaLib_Degree
from AthenaLib.models.percent import Percent as AthenaLib_Percent
from AthenaLib.models.bezier import CubicBezier as AthenaLib_CubicBezier
from AthenaLib.models.time import (
    MilliSecond as AthenaLib_MilliSecond,
    Second as AthenaLib_Second,
    Minute as AthenaLib_Minute,
    Hour as AthenaLib_Hour
)
from AthenaLib.models.url import Url as AthenaLib_Url

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Pixel","Pica","Point","Inch","Meter","DeciMeter","CentiMeter","MilliMeter",
    "Degree",
    "Percent",
    "CubicBezier",
    "MilliSecond","Second","Minute","Hour",
    "ElementFontSize","ElementFontHeight","ZeroCharacterWidth","RootElementFontSize","ViewportWidthPercent",
        "ViewportHeightPercent","ViewportLargerPercent","ViewportSmallerPercent",
    "Url",
]
# ----------------------------------------------------------------------------------------------------------------------
# - Support code -
# ----------------------------------------------------------------------------------------------------------------------
class NewEmpty:
    # Inheritance based method to create a new instance of a class down below which is "empty", aka a value of zero
    @classmethod
    def new_empty(cls):
        # noinspection PyArgumentList
        return cls(0)

# ----------------------------------------------------------------------------------------------------------------------
# - Math like objects -
# ----------------------------------------------------------------------------------------------------------------------
class Degree(AthenaLib_Degree, NewEmpty):
    def __str__(self):
        return f"{self.value}deg"
class Percent(AthenaLib_Percent, NewEmpty):
    @classmethod
    def new_full(cls):
        return cls(100)

    def __str__(self):
        return f"{self.value}%"
class CubicBezier(AthenaLib_CubicBezier):
    def __str__(self):
        return f"cubic-bezier({self.x1}, {self.y1}, {self.x2}, {self.y2})"
# ----------------------------------------------------------------------------------------------------------------------
# - Time -
# ----------------------------------------------------------------------------------------------------------------------
class MilliSecond(AthenaLib_MilliSecond, NewEmpty):
    def __str__(self):
        return f"{self.value}ms"
class Second(AthenaLib_Second, NewEmpty):
    def __str__(self):
        return f"{self.value}s"
class Minute(AthenaLib_Minute, NewEmpty):
    def __str__(self):
        return f"{self.value}m"
class Hour(AthenaLib_Hour, NewEmpty):
    def __str__(self):
        return f"{self.value}h"
# ----------------------------------------------------------------------------------------------------------------------
# - length -
# ----------------------------------------------------------------------------------------------------------------------
class Pixel(AthenaLib_Pixel, NewEmpty):
    def __str__(self):
        return f"{self.value}px"
class Pica(AthenaLib_Pica, NewEmpty):
    def __str__(self):
        return f"{self.value}pc"
class Point(AthenaLib_Point, NewEmpty):
    def __str__(self):
        return f"{self.value}pt"
class Inch(AthenaLib_Inch, NewEmpty):
    def __str__(self):
        return f"{self.value}in"
class Meter(AthenaLib_Meter, NewEmpty):
    def __str__(self):
        return f"{self.value}m"
class DeciMeter(AthenaLib_DeciMeter, NewEmpty):
    def __str__(self):
        return f"{self.value}dm"
class CentiMeter(AthenaLib_CentiMeter, NewEmpty):
    def __str__(self):
        return f"{self.value}cm"
class MilliMeter(AthenaLib_MilliMeter, NewEmpty):
    def __str__(self):
        return f"{self.value}mm"

class ElementFontSize(AthenaLib_ElementFontSize, NewEmpty):
    def __str__(self):
        return f"{self.value}em"
class ElementFontHeight(AthenaLib_ElementFontHeight, NewEmpty):
    def __str__(self):
        return f"{self.value}eh"
class ZeroCharacterWidth(AthenaLib_ZeroCharacterWidth, NewEmpty):
    def __str__(self):
        return f"{self.value}ch"
class RootElementFontSize(AthenaLib_RootElementFontSize, NewEmpty):
    def __str__(self):
        return f"{self.value}rem"
class ViewportWidthPercent(AthenaLib_ViewportWidthPercent, NewEmpty):
    def __str__(self):
        return f"{self.value}vw"
class ViewportHeightPercent(AthenaLib_ViewportHeightPercent, NewEmpty):
    def __str__(self):
        return f"{self.value}vh"
class ViewportLargerPercent(AthenaLib_ViewportLargerPercent, NewEmpty):
    def __str__(self):
        return f"{self.value}vmax"
class ViewportSmallerPercent(AthenaLib_ViewportSmallerPercent, NewEmpty):
    def __str__(self):
        return f"{self.value}vmin"
# ----------------------------------------------------------------------------------------------------------------------
# - others -
# ----------------------------------------------------------------------------------------------------------------------
class Url(AthenaLib_Url, NewEmpty):
    def __str__(self) -> str:
        return f'url("{self.url}")'