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
    FLEX_DIRECTION, FLEX_WRAP, FONT_FAMILIES
)
from AthenaCSS.Library.FilterLibrary import FILTERS

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "All", "AnimationName", "Animation", "AnimationDirection", "AnimationDelay", "AnimationDuration",
    "AccentColor", "AlignSelf", "AlignContent", "AlignItems", "AnimationFillMode", "AnimationPlayState",
    "AnimationIterationCount", "AnimationTimingFunction", "Border", "BorderColor", "BorderStyle", "BorderWidth",
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
    "Float", "FlexWrap", "FlexShrink", "FlexBasis", "Filter", "Flex", "FontFamily", "FontSize", "FontWeigth",
    "FontStyle", "Font", "FontVariant", "FontKerning", "FontStretch", "FontVariantCaps", "FontFeatureSetting",
    "FontSizeAdjust", "Gap", "GridColumnEnd", "GridColumnStart", "GridColumn", "GridColumnGap", "GridAutoColumns",
    "GridAutoFlow", "GridAutoRows", "Grid", "GridRowStart", "GridRowEnd", "GridRowGap", "GridTemplateRows",
    "GridTemplateColumns", "GridTemplateAreas", "GridTemplate", "GridArea", "GridGap", "GridRow", "ImageRendering",
    "LetterSpacing", "Height", "LineHeight", "HangingPunctuation", "Hyphens", "Isolation", "JustifyContent", "Left",
    "ListStyleImage", "ListStylePosition", "ListStyle", "ListStyleType", "MarginLeft","MarginRight", "MarginBottom",
    "MarginTop", "Margin", "MaskRepeat", "MaskOrigin", "MaskMode", "MaskSize", "MaskImage", "MaskPosition"
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
class AnimationName(CSSproperty):
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
class AnimationDuration(CSSproperty):
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
class AnimationTimingFunction(CSSproperty):
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
class AnimationDelay(CSSproperty):
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
class AnimationIterationCount(CSSproperty):
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
class AnimationDirection(CSSproperty):
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
class AnimationFillMode(CSSproperty):
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
class AnimationPlayState(CSSproperty):
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
    name: AnimationName
    duration: AnimationDuration
    timing_function: AnimationTimingFunction
    delay:AnimationDelay
    iteration_count: AnimationIterationCount
    direction: AnimationDirection
    fill_mode: AnimationFillMode
    play_state: AnimationPlayState
    __slots__ = [
        "name", "duration", "timing_function", "delay", "iteration_count", "direction", "fill_mode", "play_state"
    ]
    def __init__(
            self,
            name=AnimationName.value_logic.default,
            duration=AnimationDuration.value_logic.default,
            timing_function=AnimationTimingFunction.value_logic.default,
            delay=AnimationDelay.value_logic.default,
            iteration_count=AnimationIterationCount.value_logic.default,
            direction=AnimationDirection.value_logic.default,
            fill_mode=AnimationFillMode.value_logic.default,
            play_state=AnimationPlayState.value_logic.default
    ):
        self.name = AnimationName(name)
        self.duration = AnimationDuration(duration)
        self.timing_function = AnimationTimingFunction(timing_function)
        self.delay = AnimationDelay(delay)
        self.iteration_count = AnimationIterationCount(iteration_count)
        self.direction = AnimationDirection(direction)
        self.fill_mode = AnimationFillMode(fill_mode)
        self.play_state = AnimationPlayState(play_state)

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
    name="display"
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
        return f"flex: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Float(CSSproperty):
    name="float"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"left", "right"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontFamily(CSSproperty):
    name="font-family"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: FONT_FAMILIES
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontFeatureSetting(CSSproperty):
    name="font-feature-setting"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str:{"normal"},
            (str, str): (Any,{"on","off"}),
            (str, int): (Any,{1,0}),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontKerning(CSSproperty):
    name="font-kerning"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str:{"normal", "auto"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontSize(CSSproperty):
    name="font-size"
    value_logic = ValueLogic(
        default="medium",
        value_choice={
            str:{"medium","xx-small","x-small","small","large","x-large","xx-large","smaller","larger"},
            **LENGTHS,
            Percent:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontSizeAdjust(CSSproperty):
    name="font-size-adjust"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            int:Any,
            float:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontStretch(CSSproperty):
    name="font-stretch"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {
                "ultra-condensed","extra-condensed","condensed","semi-condensed","normal","semi-expanded","expanded",
                "extra-expanded","ultra-expanded"
            },
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontStyle(CSSproperty):
    name="font-style"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal", "italic", "oblique"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontVariant(CSSproperty):
    name="font-variant"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal", "small-caps"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontVariantCaps(CSSproperty):
    name="font-variant-caps"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {
                "normal","small-caps","all-small-caps","petite-caps","all-petite-caps","unicase","titling-caps","unset"
            },
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontWeigth(CSSproperty):
    name="font-weigth"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal","bold","bolder","lighter"},
            int: {100,200,300,400,500,600,700,800,900}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Font(CSSpropertyShorthand):
    style: FontStyle
    variant: FontVariant
    weight: FontWeigth
    size: FontSize
    family: FontFamily

    __slots__ = [
        "style","variant","weight","size","family",
    ]
    def __init__(
            self,
            style=FontStyle.value_logic.default,
            variant=FontVariant.value_logic.default,
            weight=FontWeigth.value_logic.default,
            size=FontSize.value_logic.default,
            family=FontFamily.value_logic.default,
    ):
        self.style  =FontStyle(style)
        self.variant=FontVariant(variant)
        self.weight =FontWeigth(weight)
        self.size   =FontSize(size)
        self.family =FontFamily(family)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.style._value.printer(),
            self.variant._value.printer(),
            self.weight._value.printer(),
            self.size._value.printer(),
            self.family._value.printer(),
        ))
        return f"font: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Gap(CSSproperty):
    name="gap"
    value_logic = ValueLogic(
        default=("normal", "normal"),
        value_choice={
            (AbsoluteLength, str): (Any, "normal"),
            (RelativeLength, str): (Any, "normal"),
            (str, AbsoluteLength): ("normal", Any),
            (str, RelativeLength): ("normal", Any),
            (str,str):("normal","normal"),
            **{
                length_product:(Any,Any)
                for length_product in itertools.product(
                    (AbsoluteLength, RelativeLength),
                    repeat=2)
            }
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoColumns(CSSproperty):
    name="grid-auto-columns"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto","max-content","min-content"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoFlow(CSSproperty):
    name="grid-auto-flow"
    value_logic = ValueLogic(
        default="row",
        value_choice={
            str: {"row","column", "dense", "row dense", "column dense"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoRows(CSSproperty):
    name="grid-auto-rows"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto","max-content","min-content"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumnEnd(CSSproperty):
    name="grid-column-end"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            (str, int): ({"span"},Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumnGap(CSSproperty):
    name="grid-column-gap"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumnStart(CSSproperty):
    name="grid-column-start"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            (str, int): ({"span"},Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumn(CSSpropertyShorthand):
    start: GridColumnStart
    end: GridColumnEnd

    __slots__ = [
        "start","end",
    ]
    def __init__(
            self,
            start=GridColumnStart.value_logic.default,
            end=GridColumnEnd.value_logic.default,
    ):
        self.start=GridColumnStart(start)
        self.end=GridColumnEnd(end)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.start._value.printer(),
            self.end._value.printer(),
        ))
        return f"grid-column: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class GridRowEnd(CSSproperty):
    name="grid-row-end"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            (str, int): ({"span"},Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridRowGap(CSSproperty):
    name="grid-row-gap"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridRowStart(CSSproperty):
    name="grid-row-start"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            (str, int): ({"span"},Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridRow(CSSpropertyShorthand):
    start: GridRowStart
    end: GridRowEnd

    __slots__ = [
        "start","end",
    ]
    def __init__(
            self,
            start=GridRowStart.value_logic.default,
            end=GridRowEnd.value_logic.default,
    ):
        self.start=GridRowStart(start)
        self.end=GridRowEnd(end)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.start._value.printer(),
            self.end._value.printer(),
        ))
        return f"grid-row: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class GridGap(CSSpropertyShorthand):
    row_gap: GridRowGap
    column_gap: GridColumnGap

    __slots__ = [
        "row_gap","column_gap",
    ]
    def __init__(
            self,
            start=GridRowGap.value_logic.default,
            end=GridColumnGap.value_logic.default,
    ):
        self.row_gap=GridRowGap(start)
        self.column_gap=GridColumnGap(end)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.row_gap._value.printer(),
            self.column_gap._value.printer(),
        ))
        return f"grid-gap: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplateAreas(CSSproperty):
    name="grid-template-areas"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplateColumns(CSSproperty):
    name="grid-template-columns"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"auto", "max-content", "min-content"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplateRows(CSSproperty):
    name="grid-template-rows"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"auto", "max-content", "min-content"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplate(CSSpropertyShorthand):
    rows: GridTemplateRows
    columns: GridTemplateColumns
    areas: GridTemplateAreas

    __slots__ = [
        "rows","columns","areas"
    ]
    def __init__(
            self,
            rows=GridTemplateRows.value_logic.default,
            columns=GridTemplateColumns.value_logic.default,
            areas=GridTemplateAreas.value_logic.default,
    ):
        self.rows=GridTemplateRows(rows)
        self.columns=GridTemplateColumns(columns)
        self.areas=GridTemplateAreas(areas)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.rows._value.printer(),
            self.columns._value.printer(),
            self.areas._value.printer(),
        ))
        return f"grid-template: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class GridArea(CSSpropertyShorthand):
    row_start: GridRowStart
    column_start: GridColumnStart
    row_end: GridRowEnd
    column_end: GridColumnEnd

    __slots__ = [
        "row_start","column_start","row_end","column_end"
    ]
    def __init__(
            self,
            row_start=GridRowStart.value_logic.default,
            column_start=GridColumnStart.value_logic.default,
            row_end=GridRowEnd.value_logic.default,
            column_end=GridColumnEnd.value_logic.default,
    ):
        self.row_start=GridRowStart(row_start)
        self.column_start=GridColumnStart(column_start)
        self.row_end=GridRowEnd(row_end)
        self.column_end=GridColumnEnd(column_end)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.row_start._value.printer(),
            self.column_start._value.printer(),
            self.row_end._value.printer(),
            self.column_end._value.printer(),
        ))
        return f"grid-area: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Grid(CSSpropertyShorthand):
    template_rows: GridTemplateRows
    template_columns: GridTemplateColumns
    template_areas: GridTemplateAreas
    auto_rows: GridAutoRows
    auto_columns: GridAutoColumns
    auto_flow: GridAutoFlow


    __slots__ = [
        "template_rows","template_columns","template_areas","auto_rows","auto_columns","auto_flow"
    ]
    def __init__(
            self,
            template_rows=GridTemplateRows.value_logic.default,
            template_columns=GridTemplateColumns.value_logic.default,
            template_areas=GridTemplateAreas.value_logic.default,
            auto_rows=GridAutoRows.value_logic.default,
            auto_columns=GridAutoColumns.value_logic.default,
            auto_flow=GridAutoFlow.value_logic.default,
    ):
        self.template_rows=GridTemplateRows(template_rows)
        self.template_columns=GridTemplateColumns(template_columns)
        self.template_areas=GridTemplateAreas(template_areas)
        self.auto_rows=GridAutoRows(auto_rows)
        self.auto_columns=GridAutoColumns(auto_columns)
        self.auto_flow=GridAutoFlow(auto_flow)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.template_rows._value.printer(),
            self.template_columns._value.printer(),
            self.template_areas._value.printer(),
            self.auto_rows._value.printer(),
            self.auto_columns._value.printer(),
            self.auto_flow._value.printer(),
        ))
        return f"grid: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class HangingPunctuation(CSSproperty):
    name="hanging-punctuation"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: {"first","last","allow-end","force-end"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Height(CSSproperty):
    name="height"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Hyphens(CSSproperty):
    name="hyphens"
    value_logic = ValueLogic(
        default="manual",
        value_choice={
            None:None,
            str: {"manual", "auto"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ImageRendering(CSSproperty):
    name="image-rendering"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            None:None,
            str: {"auto","smooth","high-quality","crisp-edges","pixelated"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Isolation(CSSproperty):
    name="isolation"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            None:None,
            str: {"auto","isolate"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class JustifyContent(CSSproperty):
    name="justify-content"
    value_logic = ValueLogic(
        default="flex-start",
        value_choice={
            None:None,
            str: {"flex-start","flex-end","center","space-between","space-around","space-evenly"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Left(CSSproperty):
    name="left"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class LetterSpacing(CSSproperty):
    name="letter-spacing"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class LineHeight(CSSproperty):
    name="line-height"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: {"normal"},
            int: Any,
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyleImage(CSSproperty):
    name="list-style-image"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Url: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStylePosition(CSSproperty):
    name="list-style-position"
    value_logic = ValueLogic(
        default="outside",
        value_choice={
            str: {"inside", "outside"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyleType(CSSproperty):
    name="list-style-position"
    value_logic = ValueLogic(
        default="disc",
        value_choice={
            str: {
                "disc", "armenian", "circle", "cjk-ideographic", "decimal", "decimal-leading-zero", "georgian",
                "hebrew", "hiragana", "hiragana-iroha", "katakana", "katakana-iroha", "lower-alpha", "lower-greek" ,
                "lower-latin", "lower-roman", "square", "upper-alpha", "upper-greek", "upper-latin", "upper-roman"
            }
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyle(CSSpropertyShorthand):
    type: ListStyleType
    position: ListStylePosition
    image: ListStyleImage

    __slots__ = [
        "type","position","image"
    ]
    def __init__(
            self,
            type_=ListStyleType.value_logic.default,
            position=ListStylePosition.value_logic.default,
            image=ListStyleImage.value_logic.default,
    ):
        self.type=ListStyleType(type_)
        self.position=ListStylePosition(position)
        self.image=ListStyleImage(image)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.type._value.printer(),
            self.position._value.printer(),
            self.image._value.printer(),
        ))
        return f"list-style: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class MarginBottom(CSSproperty):
    name="margin-bottom"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginLeft(CSSproperty):
    name="margin-left"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginRight(CSSproperty):
    name="margin-right"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginTop(CSSproperty):
    name="margin-top"
    value_logic = ValueLogic(
        default=Pixel(0),
        value_choice={
            str: {"auto"},
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Margin(CSSpropertyShorthand):
    top: MarginTop
    right: MarginRight
    bottom: MarginBottom
    left: MarginLeft

    __slots__ = [
        "top","right","bottom", "left"
    ]
    def __init__(
            self,
            top=MarginTop.value_logic.default,
            right=MarginRight.value_logic.default,
            bottom=MarginBottom.value_logic.default,
            left=MarginLeft.value_logic.default,
    ):
        self.top=MarginTop(top)
        self.right=MarginRight(right)
        self.bottom=MarginBottom(bottom)
        self.left=MarginLeft(left)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.top._value.printer(),
            self.right._value.printer(),
            self.bottom._value.printer(),
            self.left._value.printer(),
        ))
        return f"margin: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class MaskImage(CSSproperty):
    name="mask-image"
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
class MaskMode(CSSproperty):
    name="mask-mode"
    value_logic = ValueLogic(
        default="match-source",
        value_choice={
            str: {"match-source","luminance","alpha"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskOrigin(CSSproperty):
    name="mask-origin"
    value_logic = ValueLogic(
        default="border-box",
        value_choice={
            str: {"border-box","content-box","padding-box","margin-box","fill-box","stroke-box","view-box"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskPosition(CSSproperty):
    name="mask-position"
    value_logic = ValueLogic(
        default=(Percent(0), Percent(0)),
        value_choice={
            (Percent, Percent):(Any, Any),
            (str,str): ({"left", "right", "center"},{"top", "center", "botoom"}),
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (AbsoluteLength, RelativeLength),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskRepeat(CSSproperty):
    name="mask-repeat"
    value_logic = ValueLogic(
        default="repeat",
        value_choice={
            str: {"repeat","repeat-x","repeat-y","space","round","no-repeat"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskSize(CSSproperty):
    name="mask-size"
    value_logic = ValueLogic(
        default="auto",
        value_choice={
            str: {"auto", "contain", "cover"},
            Percent:Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaxHeight(CSSproperty):
    name="max-height"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Percent:Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaxWidth(CSSproperty):
    name="max-width"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Percent:Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MinHeight(CSSproperty):
    name="min-height"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Percent:Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MinWidth(CSSproperty):
    name="min-width"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            Percent:Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MixBlendMode(CSSproperty):
    name="mix-blend-mode"
    value_logic = ValueLogic(
        default="normal",
        value_choice={
            str: BLENDMODES
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ObjectFit(CSSproperty):
    name="object-fit"
    value_logic = ValueLogic(
        default="fill",
        value_choice={
            None:None,
            str: {"fill", "contain", "cover", "scale-down"}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)