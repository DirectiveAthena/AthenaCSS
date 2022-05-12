# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools
from typing import Any

# Custom Library
from AthenaLib.Types.Time import Second, MilliSecond
from AthenaLib.Types.Bezier import CubicBezier
from AthenaLib.Types.Url import Url
from AthenaLib.Types.Math import Percent
from AthenaLib.Types.AbsoluteLength import Pixel, AbsoluteLength
from AthenaLib.Types.RelativeLength import RelativeLength

# Custom Packages
from AthenaCSS.Objects.Properties.ValueLogic import ValueLogic
from AthenaCSS.Objects.Properties.CSSproperty import CSSproperty
from AthenaCSS.Objects.Properties.CSSpropertyShorthand import CSSpropertyShorthand
from AthenaCSS.Library.Support import (
    COLORS_CHOICE, COLORS_STR, BLENDMODES, BOX, BORDERSTYLE, BORDERWIDTH,LENGTHS, COLORS_UNION, BREAK_STR
)
import AthenaCSS.Library.FilterLibrary as Filters

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "animation_fill_mode", "animation", "animation_direction", "animation_delay", "animation_play_state",
    "animation_duration", "animation_name", "animation_iteration_count", "animation_timing_function", "align_items",
    "align_content", "align_self","backface_visibility", "background_position", "background_image", "backdrop_filter",
    "background_attachment", "background_clip", "background_blend_mode", "background_color", "background_origin",
    "background_repeat", "background_size", "background", "border_bottom_width", "border_left", "border_left_width",
    "border_bottom_left_radius", "border_right", "border_left_color", "border_top_left_radius", "border_top_color",
    "border_left_style", "border_top_style", "border_top_width", "border_right_style", "border_right_width",
    "border_bottom_color", "border_right_color", "border_bottom_style", "border_bottom_right_radius", "border_bottom",
    "border_top_right_radius", "border_top", "accent_color", "property_all","border_collapse","border_color",
    "border_image_repeat", "border_image", "border_image_width", "border_image_outset", "border_image_source",
    "border_image_slice", "border_radius", "border_spacing", "border_style", "border", "border_width", "bottom",
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
    __slots__ = [
        "name", "duration", "timing_function", "delay", "iteration_count", "direction", "fill_mode", "play_state"
    ]
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
# ----------------------------------------------------------------------------------------------------------------------
class background_repeat(CSSproperty):
    name="background-repeat"
    value_logic = ValueLogic(
        default="repeat",
        value_choice={
            str: {"repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background_size(CSSproperty):
    name="background-size"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto", "cover", "contain"},
            (Percent, Percent): Any,
            (Percent, str): (Any, "auto"),
            (AbsoluteLength,str): (Any, "auto"),
            (RelativeLength, str): (Any, "auto"),
            **{length_combo:(Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class background(CSSpropertyShorthand):
    color: background_color
    image: background_image
    position:background_position
    size:background_size
    repeat:background_repeat
    origin:background_origin
    clip:background_clip
    attachment:background_attachment
    __slots__ = [
        "color", "image", "position", "size", "repeat", "origin", "clip", "attachment"
    ]
    def __init__(
            self,
            color=background_color.value_logic.default,
            image=background_image.value_logic.default,
            position=background_position.value_logic.default,
            size=background_size.value_logic.default,
            repeat=background_repeat.value_logic.default,
            origin=background_origin.value_logic.default,
            clip=background_clip.value_logic.default,
            attachment=background_attachment.value_logic.default,
    ):
        self.color = background_color(color)
        self.image = background_image(image)
        self.position = background_position(position)
        self.size = background_size(size)
        self.repeat = background_repeat(repeat)
        self.origin = background_origin(origin)
        self.clip = background_clip(clip)
        self.attachment = background_attachment(attachment)

    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.image._value.printer(),
            self.position._value.printer(),
            self.size._value.printer(),
            self.repeat._value.printer(),
            self.origin._value.printer(),
            self.clip._value.printer(),
            self.attachment._value.printer(),
        ))
        return f"background: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom_color(CSSproperty):
    name="border-bottom-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom_left_radius(CSSproperty):
    name="border-bottom-left-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            Percent:Any,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom_right_radius(CSSproperty):
    name="border-bottom-right-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            Percent:Any,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom_style(CSSproperty):
    name="border-bottom-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: BORDERSTYLE,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom_width(CSSproperty):
    name="border-bottom-style"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_bottom(CSSpropertyShorthand):
    width:border_bottom_width
    style:border_bottom_style
    color:border_bottom_color
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=border_bottom_width.value_logic.default,
            style=border_bottom_style.value_logic.default,
            color=border_bottom_color.value_logic.default,
    ):
        self.width = border_bottom_width(width)
        self.style = border_bottom_style(style)
        self.color = border_bottom_color(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-bottom: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_top_color(CSSproperty):
    name="border-top-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_top_left_radius(CSSproperty):
    name="border-top-left-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            Percent:Any,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_top_right_radius(CSSproperty):
    name="border-top-right-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            Percent:Any,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_top_style(CSSproperty):
    name="border-top-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: BORDERSTYLE,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_top_width(CSSproperty):
    name="border-top-style"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_top(CSSpropertyShorthand):
    width:border_top_width
    style:border_top_style
    color:border_top_color
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=border_top_width.value_logic.default,
            style=border_top_style.value_logic.default,
            color=border_top_color.value_logic.default,
    ):
        self.width = border_top_width(width)
        self.style = border_top_style(style)
        self.color = border_top_color(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-top: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_left_color(CSSproperty):
    name="border-left-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_left_style(CSSproperty):
    name="border-left-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: BORDERSTYLE,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_left_width(CSSproperty):
    name="border-left-style"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_left(CSSpropertyShorthand):
    width:border_left_width
    style:border_left_style
    color:border_left_color
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=border_left_width.value_logic.default,
            style=border_left_style.value_logic.default,
            color=border_left_color.value_logic.default,
    ):
        self.width = border_left_width(width)
        self.style = border_left_style(style)
        self.color = border_left_color(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-left: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_right_color(CSSproperty):
    name="border-right-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_right_style(CSSproperty):
    name="border-right-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: BORDERSTYLE,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_right_width(CSSproperty):
    name="border-right-style"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_right(CSSpropertyShorthand):
    width:border_right_width
    style:border_right_style
    color:border_right_color
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=border_right_width.value_logic.default,
            style=border_right_style.value_logic.default,
            color=border_right_color.value_logic.default,
    ):
        self.width = border_right_width(width)
        self.style = border_right_style(style)
        self.color = border_right_color(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-right: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_collapse(CSSproperty):
    name="border-collapse"
    value_logic = ValueLogic(
        default="seperate",
        value_choice={
            str: {"seperate", "collapse"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_color(CSSproperty):
    name="border-color"
    value_logic = ValueLogic(
        default="transparent",
        value_choice={
            str:{"transparent", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_image_outset(CSSproperty):
    name="border-image-outset"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int:Any,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_image_repeat(CSSproperty):
    name="border-image-repeat"
    value_logic = ValueLogic(
        default="stretch",
        value_choice={
            str:{"stretch", "repeat", "round", "space"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_image_slice(CSSproperty):
    name="border-image-lice"
    value_logic = ValueLogic(
        default=Percent(100),
        value_choice={
            str:{"fill"},
            int:Any,
            Percent:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_image_source(CSSproperty):
    name="border-image-source"
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
class border_image_width(CSSproperty):
    name="border-image-width"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            str: BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_image(CSSpropertyShorthand):
    source: border_image_source
    slice:  border_image_slice
    width:  border_image_width
    outset: border_image_outset
    repeat: border_image_repeat

    __slots__ = [
        "source", "slice", "width", "outset", "repeat"
    ]
    def __init__(
            self,
            source=border_image_source.value_logic.default,
            slice=border_image_slice.value_logic.default,
            width=border_image_width.value_logic.default,
            outset=border_image_outset.value_logic.default,
            repeat=border_image_repeat.value_logic.default,
    ):
        self.source = border_image_source(source)
        self.slice  = border_image_slice(slice)
        self.width  = border_image_width(width)
        self.outset = border_image_outset(outset)
        self.repeat = border_image_repeat(repeat)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.source._value.printer(),
            self.slice._value.printer(),
            self.width._value.printer(),
            self.outset._value.printer(),
            self.repeat._value.printer(),
        ))
        return f"border-right: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class border_radius(CSSproperty):
    name="border-rasius"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            **{length_combo: (Any, Any, Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength,Percent),
                repeat=4
            )},
            **{length_combo: (Any, Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength,Percent),
                repeat=3
            )},
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength,Percent),
                repeat=2
            )},
            **{length: Any for length in (AbsoluteLength, RelativeLength,Percent)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_spacing(CSSproperty):
    name="border-spacing"
    value_logic = ValueLogic(
        default=Pixel(2),
        value_choice={
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength, Percent),
                repeat=2
            )},
            **{length: Any for length in (AbsoluteLength, RelativeLength, Percent)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_style(CSSproperty):
    name="border-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: BORDERSTYLE,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border_width(CSSproperty):
    name="border-width"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            str: BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class border(CSSpropertyShorthand):
    width:  border_width
    style:  border_style
    color:  border_color

    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width= border_width.value_logic.default,
            style= border_style.value_logic.default,
            color= border_color.value_logic.default,
    ):
        self.width = border_width(width)
        self.style = border_style(style)
        self.color = border_color(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.width._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class bottom(CSSproperty):
    name="bottom"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            Percent: Any,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class box_decoration_break(CSSproperty):
    name="box-decoration-break"
    value_logic = ValueLogic(
        default="slice",
        value_choice={
            str: {"slice", "clone"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class box_shadow(CSSproperty):
    name="box-shadow"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            #h-shadow,  v-shadow,   blur,   spread, color
            (Pixel,     Pixel,      Pixel,  Pixel,  COLORS_UNION):(Any,Any,Any,Any,Any),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class box_sizing(CSSproperty):
    name="box-sizing"
    value_logic = ValueLogic(
        default="content-box",
        value_choice={
            str:{"content-box", "border-box"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class break_after(CSSproperty):
    name="break-after"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class break_before(CSSproperty):
    name="break-before"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)