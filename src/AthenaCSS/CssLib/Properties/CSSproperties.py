# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .Properties import CSSproperty, CSSpropertyShorthand
from AthenaCSS.CssLib.Types import Second, MilliSecond

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "align_content", "align_items", "align_self"
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
    possibleValues = ('basline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    @property
    def defaultValue(self):
        return self.possibleValues[4]

class align_self(CSSproperty):
    possibleValues = ('auto','basline','center', 'flex-start', 'flex-end', 'stretch')
    possibleValueTypes=str

    @property
    def defaultValue(self):
        return self.possibleValues[0]

class animantion_name(CSSproperty):
    possibleValueTypes=str

class animation_duration(CSSproperty):
    possibleValues=(Second, MilliSecond)

    @property
    def defaultValue(self):
        return Second(0)

class animation_timing_function(CSSproperty):pass
class animation_delay(CSSproperty):pass
class animation_iteration_count(CSSproperty):pass
class animation_direction(CSSproperty):pass
class animation_fill_mode(CSSproperty):pass
class animation_play_state(CSSproperty):pass

class animation(CSSpropertyShorthand):
    name=animantion_name
    duration=animation_duration
    timing_function=animation_timing_function
    delay=animation_delay
    iteration_count=animation_iteration_count
    direction=animation_direction
    fill_mode=animation_fill_mode
    play_state=animation_play_state

    def __init__(self, name,duration,timing_function,delay,iteration_count,direction,fill_mode,play_state):
        super(animation, self).__init__(
            name=name,
            duration=duration,
            timing_function=timing_function,
            delay=delay,
            iteration_count=iteration_count,
            direction=direction,
            fill_mode=fill_mode,
            play_state=play_state
        )



