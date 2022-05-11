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
            Any: {Second, MilliSecond},
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
class animation(CSSpropertyShorthand):
    name: animation_name
    duration: animation_duration
    timing_function: None
    delay:None
    iteration_count: None
    direction: None
    fill_mode: None
    play_state: None
    def __init__(
            self,
            name=animation_name.value_logic.default,
            duration=animation_duration.value_logic.default,
            # timing_function,
            # delay,iteration_count,
            # direction,
            # fill_mode,
            # play_state
    ):
        self.name = animation_name(name)
        self.duration = animation_duration(duration)
        # self.timing_function = timing_function
        # self.delay = delay
        # self.iteration_count = iteration_count
        # self.direction = direction
        # self.fill_mode = fill_mode
        # self.play_state = play_state

    def printer(self) -> str:
        parts = " ".join((
            self.name._value.printer(),
            self.duration._value.printer(),
        ))
        return f"animation: {parts}"
