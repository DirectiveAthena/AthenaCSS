# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
from enum import Enum
import itertools

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV, CMYK

from AthenaLib.Types.AbsoluteLength import *
from AthenaLib.Types.RelativeLength import *
from AthenaLib.Types.Math import Percent, Degree
from AthenaLib.Types.Time import Second

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
def locked(fnc):
    def wrapper(self, *args, **kwargs):
        if self._lock:
            raise PermissionError("Manager is locked")
        return fnc(self, *args,**kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Support Variables -
# ----------------------------------------------------------------------------------------------------------------------
COLORS_CHOICE = {
    RGB: Any,
    RGBA: Any,
    HEX: Any,
    HEXA: Any,
    HSL: Any,
    HSV: Any,
    CMYK: Any
}

COLORS_UNION = RGB|RGBA|HEX|HEXA|HSL|HSV|CMYK

COLORS_STR = (
    "black","silver","gray","white","maroon","red","purple","fuchsia","green","lime","olive","yellow","navy","blue",
    "teal","aqua","antiquewhite","aquamarine","azure","beige","bisque","blanchedalmond","blueviolet","brown",
    "burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","aqua",
    "darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen",
    "darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey",
    "darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dimgrey","dodgerblue","firebrick","floralwhite",
    "forestgreen","gainsboro","ghostwhite","gold","goldenrod","greenyellow","grey","honeydew","hotpink","indianred",
    "indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan",
    "lightgoldenrodyellow","lightgray","lightgreen","lightgrey","lightpink","lightsalmon","lightseagreen","lightskyblue",
    "lightslategray","lightslategrey","lightsteelblue","lightyellow","limegreen","linen","magenta","fuchsia",
    "mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen",
    "mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","oldlace",
    "olivedrab","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip",
    "peachpuff","peru","pink","plum","powderblue","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen",
    "seashell","sienna","skyblue","slateblue","slategray","slategrey","snow","springgreen","steelblue","tan","thistle",
    "tomato","turquoise","violet","wheat","whitesmoke","yellowgreen"
)

BLENDMODES = (
    "normal", "multiply", "screen", "overlay", "darken", "ligthen", "color-dodge", "saturation", "color", "luminosity"
)
LENGTHS_TUPLE = (
    Pixel,Pica,Point,Inch,Meter,DeciMeter,CentiMeter,MilliMeter,
    ElementFontSize, ElementFontHeight, ZeroCharacterWidth, RootElementFontSize,
        ViewportWidthPercent, ViewportHeightPercent, ViewportLargerPercent, ViewportSmallerPercent
)

LENGTHS = {length: Any for length in itertools.chain(
    LENGTHS_TUPLE, (Percent,)
)}

BOX = ("border-box","padding-box","content-box")

BORDERSTYLE = ("hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset")
BORDERWIDTH = ("medium","thin", "thick")

BREAK_STR = (
    "auto","all","always","avoid","avoid-column","avoid-page","avoid-region","column","left","page","recto","region",
    "right","verso"
)

CURSOR = (
    "alias","all-scroll","auto","cell","context-menu","col-resize","copy","crosshair","default","e-resize","ew-resize",
    "grab","grabbing","help","move","n-resize","ne-resize","nesw-resize","ns-resize","nw-resize","nwse-resize","no-drop",
    "none","not-allowed","pointer","progress","row-resize","s-resize","se-resize","sw-resize","text","vertical-text",
    "w-resize","wait","zoom-in","zoom-out","initial","inherit"
)

FLEX_DIRECTION = ("row","row-reverse","column","column-reverse")
FLEX_WRAP = ("nowrap","wrap","wrap-reverse")

FONT_FAMILIES = ("calibri",)

PERCENT = {Percent:Any}
DEGREE = {Degree:Any}
NUMBERS = {int:Any, float:Any}
PIXEL = {Pixel:Any}
ANY = {Any:Any}

TRANSFORM_SPACING=", "

PERCENT_EMPTY = Percent(0)
PERCENT_FULL = Percent(100)
DEGREE_EMPTY = Degree(0)
PIXEL_EMPTY = Pixel(0)
SECOND_EMPTY = Second(0)

AUTO = "auto"
NORMAL = "normal"
MEDIUM = "medium"
VISIBLE = "visible"
TRANSPARENT = "transparent"
STRETCH = "stretch"
LEFT = "left"
RIGHT = "right"

POSITION_CHOICES = ("bottom", "top", LEFT, "center", RIGHT)
REPEAT = ("repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round")

CLASS_PREFIX = "."
ID_PREFIX = "#"

class SELECTORGROUP_TYPES(Enum):
    following = "+"
    descendant = " "
    combination = ","
    family = ">"
    preceding = "~"

NEW_LINE = "\n"

INITIALINHERIT = ("initial", "inherit")


