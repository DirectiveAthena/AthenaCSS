# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools

# Custom Library
from AthenaColor import RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA
from AthenaColor.Objects.Color.ColorSystem import ColorSystem
from AthenaColor.Objects.Color.ColorObjectConversion import to_RGB,to_RGBA
from AthenaColor.Data.HtmlColors import HtmlColorObjects,HtmlColorTuples

from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.Url import Url
from AthenaLib.Types.RelativeLength import *
from AthenaLib.Types.AbsoluteLength import *

# Custom Packages
from .Classes.Properties import CSSpropertySingle,CSSpropertyMulti

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "align_content", "align_items", "align_self",
    "animation_name", "animation_duration","animation_timing_function","animation_delay", "animation_iteration_count",
        "animation_direction","animation_fill_mode","animation_play_state",
    "backface_visibility",
    "background_attachment","background_color","background_clip","background_image","background_origin",
        "background_position"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSpropertySingle):
    possibleValues = ('center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[5]

# ----------------------------------------------------------------------------------------------------------------------
class align_items(CSSpropertySingle):
    possibleValues = ('baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[4]

# ----------------------------------------------------------------------------------------------------------------------
class align_self(CSSpropertySingle):
    possibleValues = ('auto','baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class animation_name(CSSpropertySingle):
    possibleValueTypes=str|None
    
    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

# ----------------------------------------------------------------------------------------------------------------------
class animation_duration(CSSpropertySingle):
    possibleValueTypes=Second|MilliSecond|int|None

    def __init__(self,value:Second|MilliSecond|int=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        if isinstance(value, int):
            return Second(abs(value))
        elif isinstance(value, Second|MilliSecond):
            return abs(value)
        else:
            return value

    @property
    def defaultValue(self):
        return Second(0)

# ----------------------------------------------------------------------------------------------------------------------
class animation_timing_function(CSSpropertySingle):
    possibleValues = ('linear', 'ease', 'ease-in', 'ease-out', ' ease-in-out', CubicBezier)
    possibleValueTypes = str|CubicBezier|None
    
    def __init__(self,value:str|CubicBezier=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return "ease"

# ----------------------------------------------------------------------------------------------------------------------
class animation_delay(CSSpropertySingle):
    possibleValueTypes=Second|MilliSecond|int|None

    def __init__(self,value:Second|MilliSecond|int=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        if isinstance(value, int) and value != 0:
            return Second(value)
        else:
            return value
    @property
    def defaultValue(self):
        return Second(0)

# ----------------------------------------------------------------------------------------------------------------------
class animation_iteration_count(CSSpropertySingle):
    possibleValues = ("infinite",int)
    possibleValueTypes=str|int|None

    def __init__(self,value:str|int=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        if isinstance(value, int):
            return abs(value)
        else:
            return value

    @property
    def defaultValue(self):
        return 1

# ----------------------------------------------------------------------------------------------------------------------
class animation_direction(CSSpropertySingle):
    possibleValues = ("normal","reverse","alternate", "alternate-reverse")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class animation_fill_mode(CSSpropertySingle):
    possibleValues = ("forwards","backwards", "both")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

# ----------------------------------------------------------------------------------------------------------------------
class animation_play_state(CSSpropertySingle):
    possibleValues = ("paused","running")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[1]

# ----------------------------------------------------------------------------------------------------------------------
class backface_visibility(CSSpropertySingle):
    possibleValues = ("visible","hidden")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_attachment(CSSpropertySingle):
    possibleValues = ("scroll","fixed","local")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_clip(CSSpropertySingle):
    possibleValues = ("border-box","padding-box","content-box")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_color(CSSpropertySingle):
    possibleValues = ("transparent",RGB,RGBA,HtmlColorObjects,HtmlColorTuples)
    possibleValueTypes=str|RGB|RGBA|None

    def __init__(self,value:str|RGB|RGBA|HtmlColorObjects|HtmlColorTuples=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        # Named colors:
        if any(c in self.possibleValues for c in (HtmlColorObjects,HtmlColorTuples)) and isinstance(value, str):
            try:
                return getattr(HtmlColorObjects, value)
            except AttributeError:
                pass
        elif isinstance(value, ColorSystem):
            if isinstance(value, RGB|HEX|CMYK|HSL|HSV):
                return to_RGB(value)
            elif isinstance(value, RGBA|HEXA):
                return to_RGBA(value)

        # don't forget to return value
        return value

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_image(CSSpropertySingle):
    possibleValueTypes=str|None|Url

    def __init__(self,value:str|Url=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        if isinstance(value, str):
            return Url(value=value)
        # don't forget to return value
        return value

# ----------------------------------------------------------------------------------------------------------------------
class background_origin(CSSpropertySingle):
    possibleValues = ("border-box","padding-box","content-box")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[1]

# ----------------------------------------------------------------------------------------------------------------------
class background_position(CSSpropertyMulti):
    possibleValues = itertools.product(
        ("bottom", "center", "left", "right", "top", Pixel, Percent)
        , repeat=2
    )
    possibleValuesTupleLen=2
    possibleValueTypes=str|None|tuple|Pixel|Percent

    def __init__(self,value:str|tuple=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    def value_presetter(self, value) -> object:
        return value

    @property
    def defaultValue(self):
        return Percent(0),Percent(0)