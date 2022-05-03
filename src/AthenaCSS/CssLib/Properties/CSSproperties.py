# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaColor import RGB,HEX,CMYK,HSL,HSV,RGBA,HEXA
from AthenaColor.Objects.Color.ColorSystem import ColorSystem
from AthenaColor.Objects.Color.ColorObjectConversion import to_RGB,to_RGBA
from AthenaColor.Data.HtmlColors import HtmlColorObjects,HtmlColorTuples

# Custom Packages
from .Properties import CSSproperty
from AthenaCSS.CssLib.Types import Second, MilliSecond, CubicBezier

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "align_content", "align_items", "align_self",
    "animation_name", "animation_duration","animation_timing_function","animation_delay", "animation_iteration_count",
        "animation_direction","animation_fill_mode","animation_play_state",
    "backface_visibility",
    "background_attachment","background_color","background_clip",
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    possibleValues = ('center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[5]

# ----------------------------------------------------------------------------------------------------------------------
class align_items(CSSproperty):
    possibleValues = ('baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[4]

# ----------------------------------------------------------------------------------------------------------------------
class align_self(CSSproperty):
    possibleValues = ('auto','baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class animation_name(CSSproperty):
    possibleValueTypes=str|None
    
    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

# ----------------------------------------------------------------------------------------------------------------------
class animation_duration(CSSproperty):
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
class animation_timing_function(CSSproperty):
    possibleValues = ('linear', 'ease', 'ease-in', 'ease-out', ' ease-in-out', CubicBezier)
    possibleValueTypes = str|CubicBezier|None
    
    def __init__(self,value:str|CubicBezier=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return "ease"

# ----------------------------------------------------------------------------------------------------------------------
class animation_delay(CSSproperty):
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
class animation_iteration_count(CSSproperty):
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
class animation_direction(CSSproperty):
    possibleValues = ("normal","reverse","alternate", "alternate-reverse")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class animation_fill_mode(CSSproperty):
    possibleValues = ("forwards","backwards", "both")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

# ----------------------------------------------------------------------------------------------------------------------
class animation_play_state(CSSproperty):
    possibleValues = ("paused","running")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[1]

# ----------------------------------------------------------------------------------------------------------------------
class backface_visibility(CSSproperty):
    possibleValues = ("visible","hidden")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_attachment(CSSproperty):
    possibleValues = ("scroll","fixed","local")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]

# ----------------------------------------------------------------------------------------------------------------------
class background_color(CSSproperty):
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
class background_clip(CSSproperty):
    possibleValues = ("border-box","padding-box","content-box")
    possibleValueTypes=str|None

    def __init__(self,value:str=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return self.possibleValues[0]
