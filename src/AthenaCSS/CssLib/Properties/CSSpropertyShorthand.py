# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .Properties import CSSpropertyShorthand
from AthenaCSS.CssLib.Properties.CSSproperties import *

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "animation",
]


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
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
    printer_order = ["name", "duration","timing_function", "delay","iteration_count","direction","fill_mode", "play_state"]

    # for correct type hinting and correct argument parsing
    def __init__(
        self,
        name:           animation_name.possibleValueTypes,
        duration:       animation_duration.possibleValueTypes,
        timing_function:animation_timing_function.possibleValueTypes,
        delay:          animation_delay.possibleValueTypes,
        iteration_count:animation_iteration_count.possibleValueTypes,
        direction:      animation_direction.possibleValueTypes,
        fill_mode:      animation_fill_mode.possibleValueTypes,
        play_state:     animation_play_state.possibleValueTypes,
        *args,
        **kwargs,
    ):
        super(animation, self).__init__(
            *args,
            name=           name,
            duration=       duration,
            timing_function=timing_function,
            delay=          delay,
            iteration_count=iteration_count,
            direction=      direction,
            fill_mode=      fill_mode,
            play_state=     play_state,
            **kwargs,
        )