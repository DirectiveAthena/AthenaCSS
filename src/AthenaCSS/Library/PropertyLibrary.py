# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library
from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.Url import Url
from AthenaLib.Types.Math import Percent
from AthenaLib.Types.AbsoluteLength import Pixel

# Custom Packages
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic
from AthenaCSS.Objects.Properties.CSSproperty import CSSproperty
from AthenaCSS.Objects.Properties.CSSpropertyShorthand import CSSpropertyShorthand
from AthenaCSS.Library.Support import (COLORS_CHOICE, COLORS_STR, BLENDMODES, BOX)
import AthenaCSS.Library.FilterLibrary as Filters

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "animation_fill_mode", "animation", "animation_direction", "animation_delay", "animation_play_state",
    "animation_duration", "animation_name", "animation_iteration_count", "animation_timing_function", "align_items",
    "align_content", "align_self","backface_visibility", "background_position", "background_image", "backdrop_filter",
    "background_attachment", "background_clip", "background_blend_mode", "background_color", "background_origin"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class accent_color(CSSproperty):
    name="accent-color"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:{"auto", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class align_content(CSSproperty):
    name="align-content"
    value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str: {"center", "fex-start", "flex-end", "space-between", "space-around", "space-evenly", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class align_items(CSSproperty):
    name="align-items"
    value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str: {"baseline","center", "fex-start", "flex-end", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class align_self(CSSproperty):
    name="align-self"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto","baseline","center", "fex-start", "flex-end", "stretch"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class property_all(CSSproperty):
    name="all"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"unset"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class animation_direction(CSSproperty):
    name="animation-direction"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal", "reverse", "alternate", "alternate-reverse"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class animation_fill_mode(CSSproperty):
    name="animation-fill-mode"
    value_logic = ValueLogic(
        value_choice={
            None:None,
            str:{"forwards", "backwards", "both"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class animation_play_state(CSSproperty):
    name="animation-play-state"
    value_logic = ValueLogic(
        default="running",
        value_choice={
            str:{"paused", "running"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
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

    # noinspection PyProtectedMember
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
# ----------------------------------------------------------------------------------------------------------------------
class backdrop_filter (CSSproperty):
    name="backdrop-filter"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Filters.blur:Any,
            Filters.brightness:Any,
            Filters.contrast:Any,
            Filters.drop_shadow:Any,
            Filters.grayscale:Any,
            Filters.hue_rotate:Any,
            Filters.invert:Any,
            Filters.opacity:Any,
            Filters.saturate:Any,
            Filters.sepia:Any,
            Url:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class backface_visibility (CSSproperty):
    name="backface-visibility"
    value_logic = ValueLogic(
        default="visible",
        value_choice={
            str:{"visible", "hidden"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_attachment(CSSproperty):
    name="background-attachment"
    value_logic = ValueLogic(
        default="scroll",
        value_choice={
            str: {"scroll", "fixed", "local"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_blend_mode(CSSproperty):
    name="background-blend-mode"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: BLENDMODES
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_clip(CSSproperty):
    name="background-clip"
    value_logic = ValueLogic(
        default="border-box",
        value_choice={
            str: BOX
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_color(CSSproperty):
    name="background-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_image(CSSproperty):
    name="background-image"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Url:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_origin(CSSproperty):
    name="background-origin"
    value_logic = ValueLogic(
        default="padding-box",
        value_choice={
            str:BOX,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_position(CSSproperty):
    name="background-position"
    value_logic = ValueLogic(
        default=(Percent(0), Percent(0)),
        value_choice={
            str: (str_choices := {"bottom", "top", "left", "center", "right"}),
            (Percent,Percent): (Any, Any),
            (Pixel,Pixel): (Any, Any),
            (Percent,str): (Any, str_choices),
            (Pixel,str): (Any, str_choices),
            (str,str):(str_choices, str_choices),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)