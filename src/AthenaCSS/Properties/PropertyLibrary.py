# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library
from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.Bezier import CubicBezier

# Custom Packages
from .ValueLogic import ValueLogic
from .CSSproperty import CSSproperty
from .CSSpropertyShorthand import CSSpropertyShorthand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    name="align-content"
    value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str: {"center", "fex-start", "flex-end", "space-between", "space-around", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class align_items(CSSproperty):
    name="align-items"
    value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str: {"baseline","center", "fex-start", "flex-end", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class align_self(CSSproperty):
    name="align-self"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto","baseline","center", "fex-start", "flex-end", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_name(CSSproperty):
    name="animation-name"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            str: Any,
            None: None
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_duration(CSSproperty):
    name="animation-duration"
    value_logic = ValueLogic(
        default=Second(0),
        value_choice={
            Second:Any,
            MilliSecond:Any
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_timing_function(CSSproperty):
    name="animation-timing-function"
    value_logic = ValueLogic(
        default="ease",
        value_choice={
            str: {"linear", "ease", "ease-in", "ease-out", "ease-in-out"},
            CubicBezier: Any,
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_delay(CSSproperty):
    name="animation-delay"
    value_logic = ValueLogic(
        default=Second(0),
        value_choice={
            Second:Any,
            MilliSecond:Any
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_iteration_count(CSSproperty):
    name="animation-iteration-count"
    value_logic = ValueLogic(
        default=1,
        value_choice={
            str: {"infinite"},
            int:Any
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_direction(CSSproperty):
    name="animation-direction"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal", "reverse", "alternate", "alternate-reverse"},
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_fill_mode(CSSproperty):
    name="animation-fill-mode"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str:{"forwards", "backwards", "both"}
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation_play_state(CSSproperty):
    name="animation-play-state"
    value_logic = ValueLogic(
        default="running",
        value_choice={
            str:{"paused", "running"}
        },
    )
    def __init__(self, value=value_logic.default):
        super().__init__(value)
# ----------------------------------------------------------------------------------------------------------------------
class animation(CSSpropertyShorthand):
    name: animation_name
    duration: animation_duration
    timing_function: animation_timing_function
    delay:animation_delay
    iteration_count: animation_iteration_count
    direction: animation_direction
    fill_mode: animation_fill_mode
    play_state: animation_play_state
    def __init__(
            self,
            name=animation_name.value_logic.default,
            duration=animation_duration.value_logic.default,
            timing_function=animation_timing_function.value_logic.default,
            delay=animation_delay.value_logic.default,
            iteration_count=animation_iteration_count.value_logic.default,
            direction=animation_direction.value_logic.default,
            fill_mode=animation_fill_mode.value_logic.default,
            play_state=animation_play_state.value_logic.default
    ):
        self.name = animation_name(name)
        self.duration = animation_duration(duration)
        self.timing_function = animation_timing_function(timing_function)
        self.delay = animation_delay(delay)
        self.iteration_count = animation_iteration_count(iteration_count)
        self.direction = animation_direction(direction)
        self.fill_mode = animation_fill_mode(fill_mode)
        self.play_state = animation_play_state(play_state)

    def printer(self) -> str:
        parts = " ".join((
            self.name._value.printer(),
            self.duration._value.printer(),
            self.timing_function._value.printer(),
            self.delay._value.printer(),
            self.iteration_count._value.printer(),
            self.direction._value.printer(),
            self.fill_mode._value.printer(),
            self.play_state._value.printer()
        ))
        return f"animation: {parts}"
