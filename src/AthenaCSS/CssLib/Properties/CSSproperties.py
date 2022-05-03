# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .Properties import CSSproperty, CSSpropertyShorthand
from AthenaCSS.CssLib.Types import Second, MilliSecond, CubicBezier

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "align_content", "align_items", "align_self",
    "animation_name", "animation_duration","animation_timing_function"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    possibleValues = ('center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'stretch')
    possibleValueTypes=str

    @property
    def defaultValue(self):
        return self.possibleValues[5]

class align_items(CSSproperty):
    possibleValues = ('baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    @property
    def defaultValue(self):
        return self.possibleValues[4]

class align_self(CSSproperty):
    possibleValues = ('auto','baseline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    @property
    def defaultValue(self):
        return self.possibleValues[0]

class animation_name(CSSproperty):
    possibleValueTypes=str

class animation_duration(CSSproperty):
    possibleValueTypes=Second|MilliSecond|int

    def __init__(self,value:Second|MilliSecond|int, *args, **kwargs):
        # this is done to make my life easier, to not constantly use the 'Second' class
        if isinstance(value, int) and value != 0:
            value = Second(value)
        super(animation_duration, self).__init__(value, *args, **kwargs)

    @property
    def defaultValue(self):
        return Second(0)

class animation_timing_function(CSSproperty):
    possibleValues = ('linear', 'ease', 'ease-in', 'ease-out', ' ease-in-out', CubicBezier)
    possibleValueTypes = str|CubicBezier

    @property
    def defaultValue(self):
        return "ease"

class animation_delay(CSSproperty):pass
class animation_iteration_count(CSSproperty):pass
class animation_direction(CSSproperty):pass
class animation_fill_mode(CSSproperty):pass
class animation_play_state(CSSproperty):pass

class animation(CSSpropertyShorthand):
    # Sub properties
    name=animation_name
    duration=animation_duration
    timing_function=animation_timing_function
    delay=animation_delay
    iteration_count=animation_iteration_count
    direction=animation_direction
    fill_mode=animation_fill_mode
    play_state=animation_play_state

    # To make sure the output order is correct:
    printer_order = ["name", "duration","timing", "delay","iteration_count","direction","fill_mode", "play_state"]

    # for correct type hinting and correct argument parsing
    def __init__(
        self,
        name:animation_name,
        duration:animation_duration,
        timing_function:animation_timing_function,
        delay:animation_delay,
        iteration_count:animation_iteration_count,
        direction:animation_direction,
        fill_mode:animation_fill_mode,
        play_state:animation_play_state,
        *args,
        **kwargs,
    ):
        super(animation, self).__init__(
            *args,
            name=name,
            duration=duration,
            timing_function=timing_function,
            delay=delay,
            iteration_count=iteration_count,
            direction=direction,
            fill_mode=fill_mode,
            play_state=play_state,
            **kwargs,
        )



