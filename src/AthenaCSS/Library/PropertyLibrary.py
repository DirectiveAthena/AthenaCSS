# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools
from typing import Any, AnyStr

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
    COLORS_CHOICE, COLORS_STR, BLENDMODES, BOX, BORDERSTYLE, BORDERWIDTH,LENGTHS, COLORS_UNION, BREAK_STR, CURSOR,
    FLEX_DIRECTION, FLEX_WRAP
)
from AthenaCSS.Library.FilterLibrary import FILTERS

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "All", "AnitmationName", "Animation", "AnitmationDirection", "AnitmationDelay", "AnitmationDuration",
    "AccentColor", "AlignSelf", "AlignContent", "AlignItems", "AnitmationFillMode", "AnitmationPlayState",
    "AnitmationIterationCount", "AnitmationTimingFunction", "Border", "BorderColor", "BorderStyle", "BorderWidth",
    "Bottom", "BorderBottom", "BorderBottomColor", "BorderBottomStyle", "BorderBottomWidth", "BorderBottomLeftRadius",
    "BackgroundClip","Background", "BackgroundRepeat", "BackgroundOrigin", "BackgroundAttachment", "BackgroundSize",
    "BackgroundColor", "BackgroundPosition", "BackgroundImage", "BorderImage", "BorderImageOutset", "BorderImageRepeat",
    "BorderTopColor", "BorderTop", "BorderRightColor", "BorderTopRightRadius", "BorderRightStyle", "BorderRightWidth",
    "BorderTopStyle", "BorderLeftStyle", "BorderLeftColor", "BorderTopLeftRadius", "BorderTopWidth", "BorderLeft",
    "BorderLeftWidth", "BorderImageWidth", "BorderImageSlice", "BorderImageSource", "BorderRight", "BorderCollapse",
    "BorderBottomRightRadius", "BorderRadius", "BorderSpacing", "BreakAfter", "BreakBefore", "BreakInside",
    "BoxDecorationBreak", "BoxShadow", "BoxSizing", "BackdropFilter", "BackfaceVisibility", "BackgroundBlendMode",
    "Clear", "Color", "CaretColor", "Cursor", "Columns", "ColumnWidth", "ColumnCount", "ColumnRuleWidth", "ColumnGap",
    "Content", "ColumnRule", "ColumnFill", "ColumnSpan", "ColumnRuleColor", "ColormRuleStyle", "ClipPath", "CaptionSide",
    "CounterReset", "CounterIncrement", "Display", "Direction", "EmptyCells", "FlexDirection", "FlexFlow", "FlexGrow",
    "Float", "FlexWrap", "FlexShrink", "FlexBasis", "Filter"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AccentColor(CSSproperty):
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
class AlignContent(CSSproperty):
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
class AlignItems(CSSproperty):
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
class AlignSelf(CSSproperty):
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
class All(CSSproperty):
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
class AnitmationName(CSSproperty):
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
class AnitmationDuration(CSSproperty):
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
class AnitmationTimingFunction(CSSproperty):
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
class AnitmationDelay(CSSproperty):
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
class AnitmationIterationCount(CSSproperty):
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
class AnitmationDirection(CSSproperty):
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
class AnitmationFillMode(CSSproperty):
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
class AnitmationPlayState(CSSproperty):
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
class Animation(CSSpropertyShorthand):
    name: AnitmationName
    duration: AnitmationDuration
    timing_function: AnitmationTimingFunction
    delay:AnitmationDelay
    iteration_count: AnitmationIterationCount
    direction: AnitmationDirection
    fill_mode: AnitmationFillMode
    play_state: AnitmationPlayState
    __slots__ = [
        "name", "duration", "timing_function", "delay", "iteration_count", "direction", "fill_mode", "play_state"
    ]
    def __init__(
            self,
            name=AnitmationName.value_logic.default,
            duration=AnitmationDuration.value_logic.default,
            timing_function=AnitmationTimingFunction.value_logic.default,
            delay=AnitmationDelay.value_logic.default,
            iteration_count=AnitmationIterationCount.value_logic.default,
            direction=AnitmationDirection.value_logic.default,
            fill_mode=AnitmationFillMode.value_logic.default,
            play_state=AnitmationPlayState.value_logic.default
    ):
        self.name = AnitmationName(name)
        self.duration = AnitmationDuration(duration)
        self.timing_function = AnitmationTimingFunction(timing_function)
        self.delay = AnitmationDelay(delay)
        self.iteration_count = AnitmationIterationCount(iteration_count)
        self.direction = AnitmationDirection(direction)
        self.fill_mode = AnitmationFillMode(fill_mode)
        self.play_state = AnitmationPlayState(play_state)

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
class BackdropFilter(CSSproperty):
    name="backdrop-filter"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **FILTERS,
            Url:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackfaceVisibility(CSSproperty):
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
class BackgroundAttachment(CSSproperty):
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
class BackgroundBlendMode(CSSproperty):
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
class BackgroundClip(CSSproperty):
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
class BackgroundColor(CSSproperty):
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
class BackgroundImage(CSSproperty):
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
class BackgroundOrigin(CSSproperty):
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
class BackgroundPosition(CSSproperty):
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
class BackgroundRepeat(CSSproperty):
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
class BackgroundSize(CSSproperty):
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
class Background(CSSpropertyShorthand):
    color: BackgroundColor
    image: BackgroundImage
    position:BackgroundPosition
    size:BackgroundSize
    repeat:BackgroundRepeat
    origin:BackgroundOrigin
    clip:BackgroundClip
    attachment:BackgroundAttachment
    __slots__ = [
        "color", "image", "position", "size", "repeat", "origin", "clip", "attachment"
    ]
    def __init__(
            self,
            color=BackgroundColor.value_logic.default,
            image=BackgroundImage.value_logic.default,
            position=BackgroundPosition.value_logic.default,
            size=BackgroundSize.value_logic.default,
            repeat=BackgroundRepeat.value_logic.default,
            origin=BackgroundOrigin.value_logic.default,
            clip=BackgroundClip.value_logic.default,
            attachment=BackgroundAttachment.value_logic.default,
    ):
        self.color = BackgroundColor(color)
        self.image = BackgroundImage(image)
        self.position = BackgroundPosition(position)
        self.size = BackgroundSize(size)
        self.repeat = BackgroundRepeat(repeat)
        self.origin = BackgroundOrigin(origin)
        self.clip = BackgroundClip(clip)
        self.attachment = BackgroundAttachment(attachment)

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
class BorderBottomColor(CSSproperty):
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
class BorderBottomLeftRadius(CSSproperty):
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
class BorderBottomRightRadius(CSSproperty):
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
class BorderBottomStyle(CSSproperty):
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
class BorderBottomWidth(CSSproperty):
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
class BorderBottom(CSSpropertyShorthand):
    width:BorderBottomWidth
    style:BorderBottomStyle
    color:BorderBottomColor
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=BorderBottomWidth.value_logic.default,
            style=BorderBottomStyle.value_logic.default,
            color=BorderBottomColor.value_logic.default,
    ):
        self.width = BorderBottomWidth(width)
        self.style = BorderBottomStyle(style)
        self.color = BorderBottomColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-bottom: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class BorderTopColor(CSSproperty):
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
class BorderTopLeftRadius(CSSproperty):
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
class BorderTopRightRadius(CSSproperty):
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
class BorderTopStyle(CSSproperty):
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
class BorderTopWidth(CSSproperty):
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
class BorderTop(CSSpropertyShorthand):
    width:BorderTopWidth
    style:BorderTopStyle
    color:BorderTopColor
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=BorderTopWidth.value_logic.default,
            style=BorderTopStyle.value_logic.default,
            color=BorderTopColor.value_logic.default,
    ):
        self.width = BorderTopWidth(width)
        self.style = BorderTopStyle(style)
        self.color = BorderTopColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-top: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class BorderLeftColor(CSSproperty):
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
class BorderLeftStyle(CSSproperty):
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
class BorderLeftWidth(CSSproperty):
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
class BorderLeft(CSSpropertyShorthand):
    width:BorderLeftWidth
    style:BorderLeftStyle
    color:BorderLeftColor
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=BorderLeftWidth.value_logic.default,
            style=BorderLeftStyle.value_logic.default,
            color=BorderLeftColor.value_logic.default,
    ):
        self.width = BorderLeftWidth(width)
        self.style = BorderLeftStyle(style)
        self.color = BorderLeftColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-left: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class BorderRightColor(CSSproperty):
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
class BorderRightStyle(CSSproperty):
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
class BorderRightWidth(CSSproperty):
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
class BorderRight(CSSpropertyShorthand):
    width:BorderRightWidth
    style:BorderRightStyle
    color:BorderRightColor
    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width=BorderRightWidth.value_logic.default,
            style=BorderRightStyle.value_logic.default,
            color=BorderRightColor.value_logic.default,
    ):
        self.width = BorderRightWidth(width)
        self.style = BorderRightStyle(style)
        self.color = BorderRightColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.color._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border-right: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class BorderCollapse(CSSproperty):
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
class BorderColor(CSSproperty):
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
class BorderImageOutset(CSSproperty):
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
class BorderImageRepeat(CSSproperty):
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
class BorderImageSlice(CSSproperty):
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
class BorderImageSource(CSSproperty):
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
class BorderImageWidth(CSSproperty):
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
class BorderImage(CSSpropertyShorthand):
    source: BorderImageSource
    slice:  BorderImageSlice
    width:  BorderImageWidth
    outset: BorderImageOutset
    repeat: BorderImageRepeat

    __slots__ = [
        "source", "slice", "width", "outset", "repeat"
    ]
    def __init__(
            self,
            source=BorderImageSource.value_logic.default,
            slice_=BorderImageSlice.value_logic.default,
            width=BorderImageWidth.value_logic.default,
            outset=BorderImageOutset.value_logic.default,
            repeat=BorderImageRepeat.value_logic.default,
    ):
        self.source = BorderImageSource(source)
        self.slice  = BorderImageSlice(slice_)
        self.width  = BorderImageWidth(width)
        self.outset = BorderImageOutset(outset)
        self.repeat = BorderImageRepeat(repeat)
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
class BorderRadius(CSSproperty):
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
class BorderSpacing(CSSproperty):
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
class BorderStyle(CSSproperty):
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
class BorderWidth(CSSproperty):
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
class Border(CSSpropertyShorthand):
    width:  BorderWidth
    style:  BorderStyle
    color:  BorderColor

    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width= BorderWidth.value_logic.default,
            style= BorderStyle.value_logic.default,
            color= BorderColor.value_logic.default,
    ):
        self.width = BorderWidth(width)
        self.style = BorderStyle(style)
        self.color = BorderColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.width._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"border: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Bottom(CSSproperty):
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
class BoxDecorationBreak(CSSproperty):
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
class BoxShadow(CSSproperty):
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
class BoxSizing(CSSproperty):
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
class BreakAfter(CSSproperty):
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
class BreakBefore(CSSproperty):
    name="break-before"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BreakInside(CSSproperty):
    name="break-inside"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CaptionSide(CSSproperty):
    name="caption-side"
    value_logic = ValueLogic(
        default="top",
        value_choice={
            str: {"top", "bottom"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CaretColor(CSSproperty):
    name="caret-color"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto", *COLORS_STR},
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Clear(CSSproperty):
    name="clear"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"left", "right", "both"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ClipPath(CSSproperty):
    name="clip-path"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"border-box","padding-box","content-box", "margin-box", "fill-box", "stroke-box", "view-box"},
            Url:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Color(CSSproperty):
    name="color"
    value_logic = ValueLogic(
        # default=None, # I know this is overrideen by ValueLogic to None, but thevalue cannot exsist
        value_choice={
            str: COLORS_STR,
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnCount(CSSproperty):
    name="column-count"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnFill(CSSproperty):
    name="column-fill"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto", "balance"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnGap(CSSproperty):
    name="column-gap"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal"},
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRuleColor(CSSproperty):
    name="column-rule-color"
    value_logic = ValueLogic(
        # default=None, # I know this is overrideen by ValueLogic to None, but thevalue cannot exsist
        value_choice={
            str: COLORS_STR,
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColormRuleStyle(CSSproperty):
    name="column-rule-style"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str:BORDERSTYLE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRuleWidth(CSSproperty):
    name="column-rule-width"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRule(CSSpropertyShorthand):
    width:  ColumnRuleWidth
    style:  ColormRuleStyle
    color:  ColumnRuleColor

    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width= ColumnRuleWidth.value_logic.default,
            style= ColormRuleStyle.value_logic.default,
            color= ColumnRuleColor.value_logic.default,
    ):
        self.width = ColumnRuleWidth(width)
        self.style = ColormRuleStyle(style)
        self.color = ColumnRuleColor(color)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.width._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"column-rule: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class ColumnSpan(CSSproperty):
    name="column-span"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str:{"all"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnWidth(CSSproperty):
    name="column-width"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:{"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Columns(CSSpropertyShorthand):
    width:  ColumnWidth
    count:  ColumnCount

    __slots__ = [
        "width", "count"
    ]
    def __init__(
            self,
            width= ColumnWidth.value_logic.default,
            count= ColumnCount.value_logic.default,
    ):
        self.width = ColumnWidth(width)
        self.count = ColumnCount(count)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.width._value.printer(),
            self.count._value.printer(),
        ))
        return f"columns: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Content(CSSproperty):
    name="content"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            None:None,
            str:{"normal", "counter", "open-quote", "close-quote", "no-open-quote", "no-close-quote"},
            Url:Any,
            AnyStr:Any # as long as an object has a __str__, this should be fine
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CounterIncrement(CSSproperty):
    name="counter-increment"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            int:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CounterReset(CSSproperty):
    name="counter-reset"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            (None,int):(Any,Any),
            (str,int):(Any,Any),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Cursor(CSSproperty):
    name="cursor"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            None:None,
            (Url, str):(Any, CURSOR),
            str: CURSOR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Direction(CSSproperty):
    name="direction"
    value_logic = ValueLogic(
        default="ltr",
        value_choice={
            str:{"ltr","rtl"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Display(CSSproperty):
    name="direction"
    value_logic = ValueLogic(
        value_choice={
            None:None,
            str:{
                "inline","block","contents","flex","grid","inline-block", "inline-flex", "inline-grid", "inline-table",
                "list-item", "run-in", "table","table-caption", "table-column-group", "table-header-group",
                "table-footer-group", "table-row-group", "table-cell", "table-column", "table-row"
            }
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class EmptyCells(CSSproperty):
    name="empty-cells"
    value_logic = ValueLogic(
        default="show",
        value_choice={
            str:{"show", "hide"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Filter(CSSproperty):
    name="filter"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **FILTERS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexBasis(CSSproperty):
    name="flex-basis"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:{"auto"},
            **LENGTHS,
            Percent:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexDirection(CSSproperty):
    name="flex-direction"
    value_logic = ValueLogic(
        default="row",
        value_choice={
            str:FLEX_DIRECTION,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexFlow(CSSproperty):
    name="flex-flow"
    value_logic = ValueLogic(
        default=("row", "nowrap"),
        value_choice={
            (str,str):(FLEX_DIRECTION,FLEX_WRAP)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexGrow(CSSproperty):
    name="flex-grow"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexShrink(CSSproperty):
    name="flex-shrink"
    value_logic = ValueLogic(
        default=1,
        value_choice={
            int:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexWrap(CSSproperty):
    name="flex-wrap"
    value_logic = ValueLogic(
        default="nowrap",
        value_choice={
            str:FLEX_WRAP
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Flex(CSSpropertyShorthand):
    grow:   FlexGrow
    shrink: FlexShrink
    basis:  FlexBasis

    __slots__ = [
        "grow", "shrink", "basis"
    ]
    def __init__(
            self,
            grow=FlexGrow.value_logic.default,
            shrink=FlexShrink.value_logic.default,
            basis=FlexBasis.value_logic.default,
    ):
        self.grow =  FlexGrow(grow)
        self.shrink = FlexShrink(shrink)
        self.basis = FlexBasis(basis)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.grow._value.printer(),
            self.shrink._value.printer(),
            self.basis._value.printer(),
        ))
        return f"columns: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Float(CSSproperty):
    name="flex-wrap"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"left", "right"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)