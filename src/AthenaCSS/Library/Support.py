# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV, CMYK

from AthenaLib.Types.AbsoluteLength import AbsoluteLength
from AthenaLib.Types.RelativeLength import RelativeLength

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
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

COLORS_STR = {
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
}

BLENDMODES = {
    "normal", "multiply", "screen", "overlay", "darken", "ligthen", "color-dodge", "saturation", "color", "luminosity"
}

LENGTHS = {AbsoluteLength:Any,RelativeLength:Any,}

BOX = {"border-box","padding-box","content-box"}

BORDERSTYLE = {"hidden", "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"}
BORDERWIDTH = {"medium","thin", "thick"}

BREAK_STR = {
    "auto","all","always","avoid","avoid-column","avoid-page","avoid-region","column","left","page","recto","region",
    "right","verso"
}