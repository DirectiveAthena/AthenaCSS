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
from AthenaLib.Types.AbsoluteLength import Pixel

# Custom Packages
from AthenaCSS.Library.Support import (
    COLORS_CHOICE, COLORS_STR, BLENDMODES, BOX, BORDERSTYLE, BORDERWIDTH,LENGTHS, COLORS_UNION, BREAK_STR, CURSOR,
    FLEX_DIRECTION, FLEX_WRAP, FONT_FAMILIES, PERCENT, ANY, PERCENT_EMPTY, PERCENT_FULL,PIXEL_EMPTY, AUTO, NORMAL,
    SECOND_EMPTY, MEDIUM, VISIBLE, TRANSPARENT, STRETCH, LEFT,RIGHT, POSITION_CHOICES, REPEAT, LENGTHS_TUPLE
)
from AthenaCSS.Library.SubPropertyLibrary import FILTERS, TRANSFORMS, Steps

from AthenaCSS.Declarations.ValueLogic import ValueLogic
from AthenaCSS.Declarations.CSSProperty import CSSProperty
from AthenaCSS.Declarations.CSSPropertyShorthand import CSSPropertyShorthand

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "All","AnimationName","Animation","AnimationDirection","AnimationDelay","AnimationDuration",
    "AccentColor","AlignSelf","AlignContent","AlignItems","AnimationFillMode","AnimationPlayState",
    "AnimationIterationCount","AnimationTimingFunction","Border","BorderColor","BorderStyle","BorderWidth",
    "Bottom","BorderBottom","BorderBottomColor","BorderBottomStyle","BorderBottomWidth","BorderBottomLeftRadius",
    "BackgroundClip","Background","BackgroundRepeat","BackgroundOrigin","BackgroundAttachment","BackgroundSize",
    "BackgroundColor","BackgroundPosition","BackgroundImage","BorderImage","BorderImageOutset","BorderImageRepeat",
    "BorderTopColor","BorderTop","BorderRightColor","BorderTopRightRadius","BorderRightStyle","BorderRightWidth",
    "BorderTopStyle","BorderLeftStyle","BorderLeftColor","BorderTopLeftRadius","BorderTopWidth","BorderLeft",
    "BorderLeftWidth","BorderImageWidth","BorderImageSlice","BorderImageSource","BorderRight","BorderCollapse",
    "BorderBottomRightRadius","BorderRadius","BorderSpacing","BreakAfter","BreakBefore","BreakInside",
    "BoxDecorationBreak","BoxShadow","BoxSizing","BackdropFilter","BackfaceVisibility","BackgroundBlendMode",
    "Clear","Color","CaretColor","Cursor","Columns","ColumnWidth","ColumnCount","ColumnRuleWidth","ColumnGap",
    "Content","ColumnRule","ColumnFill","ColumnSpan","ColumnRuleColor","ColumnRuleStyle","ClipPath","CaptionSide",
    "CounterReset","CounterIncrement","Display","Direction","EmptyCells","FlexDirection","FlexFlow","FlexGrow",
    "Float","FlexWrap","FlexShrink","FlexBasis","Filter","Flex","FontFamily","FontSize","FontWeight",
    "FontStyle","Font","FontVariant","FontKerning","FontStretch","FontVariantCaps","FontFeatureSetting",
    "FontSizeAdjust","Gap","GridColumnEnd","GridColumnStart","GridColumn","GridColumnGap","GridAutoColumns",
    "GridAutoFlow","GridAutoRows","Grid","GridRowStart","GridRowEnd","GridRowGap","GridTemplateRows",
    "GridTemplateColumns","GridTemplateAreas","GridTemplate","GridArea","GridGap","GridRow","ImageRendering",
    "LetterSpacing","Height","LineHeight","HangingPunctuation","Hyphens","Isolation","JustifyContent","Left",
    "ListStyleImage","ListStylePosition","ListStyle","ListStyleType","MarginLeft","MarginRight","MarginBottom",
    "MarginTop","Margin","MaskRepeat","MaskOrigin","MaskMode","MaskSize","MaskImage","MaskPosition",
    "MaxWidth","MinWidth","MixBlendMode","MinHeight","MaxHeight","ObjectFit","OutlineWidth","OutlineColor",
    "OutlineStyle","Outline","Perspective","PerspectiveOrigin","Padding","PaddingTop","PaddingLeft",
    "PaddingRight","PaddingBottom","Position","PointerEvents","PageBreakBefore","PageBreakAfter","PageBreakInside",
    "Quotes","Right","Resize","RowGap","ScrollBehavior","TransitionDelay","TransitionDuration","Transition",
    "TransitionProperty","TransitionTimingFunction","Transform","TextTransform","TransformOrigin","TransformStyle",
    "Top","TextDecorationThickness","TextDecorationStyle","TextDecorationColor","TextDecorationLine",
    "TextDecoration","TextAlign","TextAlignLast","TextIndent","TextShadow","TextJustify","TextOverflow","TabSize",
    "TableLayout","UserSelect","UnicodeBidi","Visibility","VerticalAlign","Order","Orphans","Overflow",
    "OverflowX","OverflowY","OverflowWrap","Opacity","OutlineOffset","ObjectPosition","WordWrap","WordSpacing",
    "WritingMode","Width","Widows","WordBreak","WhiteSpace","ZIndex"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AccentColor(CSSProperty):
    name="accent-color"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AlignContent(CSSProperty):
    name="align-content"
    value_logic = ValueLogic(
        default=STRETCH,
        value_choice={
            str: ("center", "fex-start", "flex-end", "space-between", "space-around", "space-evenly", STRETCH),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AlignItems(CSSProperty):
    name="align-items"
    value_logic = ValueLogic(
        default=STRETCH,
        value_choice={
            str: ("baseline","center", "fex-start", "flex-end", STRETCH),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AlignSelf(CSSProperty):
    name="align-self"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,"baseline","center", "fex-start", "flex-end", STRETCH),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class All(CSSProperty):
    name="all"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: ("unset",),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationName(CSSProperty):
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
class AnimationDuration(CSSProperty):
    name="animation-duration"
    value_logic = ValueLogic(
        default=SECOND_EMPTY,
        value_choice={
            Second:Any,
            MilliSecond:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationTimingFunction(CSSProperty):
    name="animation-timing-function"
    value_logic = ValueLogic(
        default="ease",
        value_choice={
            str: ("linear", "ease", "ease-in", "ease-out", "ease-in-out"),
            CubicBezier: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationDelay(CSSProperty):
    name="animation-delay"
    value_logic = ValueLogic(
        default=SECOND_EMPTY,
        value_choice={
            Second:Any,
            MilliSecond:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationIterationCount(CSSProperty):
    name="animation-iteration-count"
    value_logic = ValueLogic(
        default=1,
        value_choice={
            str: ("infinite",),
            int:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationDirection(CSSProperty):
    name="animation-direction"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL, "reverse", "alternate", "alternate-reverse"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationFillMode(CSSProperty):
    name="animation-fill-mode"
    value_logic = ValueLogic(
        value_choice={
            None:None,
            str:("forwards", "backwards", "both")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class AnimationPlayState(CSSProperty):
    name="animation-play-state"
    value_logic = ValueLogic(
        default="running",
        value_choice={
            str:("paused", "running")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Animation(CSSPropertyShorthand):
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
class BackdropFilter(CSSProperty):
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
class BackfaceVisibility(CSSProperty):
    name="backface-visibility"
    value_logic = ValueLogic(
        default=VISIBLE,
        value_choice={
            str:(VISIBLE, "hidden")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundAttachment(CSSProperty):
    name="background-attachment"
    value_logic = ValueLogic(
        default="scroll",
        value_choice={
            str: ("scroll", "fixed", "local")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundBlendMode(CSSProperty):
    name="background-blend-mode"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: BLENDMODES
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundClip(CSSProperty):
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
class BackgroundColor(CSSProperty):
    name="background-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundImage(CSSProperty):
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
class BackgroundOrigin(CSSProperty):
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
class BackgroundPosition(CSSProperty):
    name="background-position"
    value_logic = ValueLogic(
        default=(PERCENT_EMPTY, PERCENT_EMPTY),
        value_choice={
            str: POSITION_CHOICES,
            (Percent,Percent): (Any, Any),
            (Pixel,Pixel): (Any, Any),
            (Percent,str): (Any, POSITION_CHOICES),
            (Pixel,str): (Any, POSITION_CHOICES),
            (str,str):(POSITION_CHOICES, POSITION_CHOICES),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundRepeat(CSSProperty):
    name="background-repeat"
    value_logic = ValueLogic(
        default="repeat",
        value_choice={
            str: REPEAT,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BackgroundSize(CSSProperty):
    name="background-size"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO, "cover", "contain"),
            (Percent,Percent):Any,
            (Percent,str):(Any, (AUTO,)),
            **{(length,str):(Any, (AUTO,)) for length in LENGTHS_TUPLE},
            **{length_combo:(Any, Any) for length_combo in itertools.product(
                LENGTHS_TUPLE,
                repeat=2
            )},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Background(CSSPropertyShorthand):
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
class BorderBottomColor(CSSProperty):
    name="border-bottom-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderBottomLeftRadius(CSSProperty):
    name="border-bottom-left-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            **PERCENT,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (*LENGTHS_TUPLE, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderBottomRightRadius(CSSProperty):
    name="border-bottom-right-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            **PERCENT,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (*LENGTHS_TUPLE, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderBottomStyle(CSSProperty):
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
class BorderBottomWidth(CSSProperty):
    name="border-bottom-style"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderBottom(CSSPropertyShorthand):
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
class BorderTopColor(CSSProperty):
    name="border-top-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderTopLeftRadius(CSSProperty):
    name="border-top-left-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            **PERCENT,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (*LENGTHS_TUPLE, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderTopRightRadius(CSSProperty):
    name="border-top-right-radius"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: {0},
            **PERCENT,
            **LENGTHS,
            **{length_combo:Any for length_combo in itertools.product(
                (*LENGTHS_TUPLE, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderTopStyle(CSSProperty):
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
class BorderTopWidth(CSSProperty):
    name="border-top-style"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderTop(CSSPropertyShorthand):
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
class BorderLeftColor(CSSProperty):
    name="border-left-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderLeftStyle(CSSProperty):
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
class BorderLeftWidth(CSSProperty):
    name="border-left-style"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderLeft(CSSPropertyShorthand):
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
class BorderRightColor(CSSProperty):
    name="border-right-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderRightStyle(CSSProperty):
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
class BorderRightWidth(CSSProperty):
    name="border-right-style"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            None:None,
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderRight(CSSPropertyShorthand):
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
class BorderCollapse(CSSProperty):
    name="border-collapse"
    value_logic = ValueLogic(
        default="separate",
        value_choice={
            str: {"separate", "collapse"},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderColor(CSSProperty):
    name="border-color"
    value_logic = ValueLogic(
        default=TRANSPARENT,
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderImageOutset(CSSProperty):
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
class BorderImageRepeat(CSSProperty):
    name="border-image-repeat"
    value_logic = ValueLogic(
        default=STRETCH,
        value_choice={
            str:(STRETCH, "repeat", "round", "space")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderImageSlice(CSSProperty):
    name="border-image-lice"
    value_logic = ValueLogic(
        default=PERCENT_FULL,
        value_choice={
            str:("fill",),
            int:Any,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderImageSource(CSSProperty):
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
class BorderImageWidth(CSSProperty):
    name="border-image-width"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            str: BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderImage(CSSPropertyShorthand):
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
class BorderRadius(CSSProperty):
    name="border-radius"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            **{length_combo: (Any, Any, Any, Any) for length_combo in itertools.product(
                (*LENGTHS_TUPLE,Percent),
                repeat=4
            )},
            **{length_combo: (Any, Any, Any) for length_combo in itertools.product(
                (*LENGTHS_TUPLE,Percent),
                repeat=3
            )},
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (*LENGTHS_TUPLE,Percent),
                repeat=2
            )},
            **{length: Any for length in (*LENGTHS_TUPLE,Percent)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderSpacing(CSSProperty):
    name="border-spacing"
    value_logic = ValueLogic(
        default=Pixel(2),
        value_choice={
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (*LENGTHS_TUPLE, Percent),
                repeat=2
            )},
            **{length: Any for length in (*LENGTHS_TUPLE, Percent)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BorderStyle(CSSProperty):
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
class BorderWidth(CSSProperty):
    name="border-width"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            str: BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Border(CSSPropertyShorthand):
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
class Bottom(CSSProperty):
    name="bottom"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            Percent: Any,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BoxDecorationBreak(CSSProperty):
    name="box-decoration-break"
    value_logic = ValueLogic(
        default="slice",
        value_choice={
            str: ("slice", "clone"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BoxShadow(CSSProperty):
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
class BoxSizing(CSSProperty):
    name="box-sizing"
    value_logic = ValueLogic(
        default="content-box",
        value_choice={
            str:("content-box", "border-box")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BreakAfter(CSSProperty):
    name="break-after"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BreakBefore(CSSProperty):
    name="break-before"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class BreakInside(CSSProperty):
    name="break-inside"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:BREAK_STR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CaptionSide(CSSProperty):
    name="caption-side"
    value_logic = ValueLogic(
        default="top",
        value_choice={
            str: ("top", "bottom")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CaretColor(CSSProperty):
    name="caret-color"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Clear(CSSProperty):
    name="clear"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: (LEFT, RIGHT, "both")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ClipPath(CSSProperty):
    name="clip-path"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: ("border-box","padding-box","content-box", "margin-box", "fill-box", "stroke-box", "view-box"),
            Url:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Color(CSSProperty):
    name="color"
    value_logic = ValueLogic(
        # default=None, # I know this is overridden by ValueLogic to None, but the value cannot exist
        value_choice={
            str:(TRANSPARENT, *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnCount(CSSProperty):
    name="column-count"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnFill(CSSProperty):
    name="column-fill"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO, "balance"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnGap(CSSProperty):
    name="column-gap"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,),
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRuleColor(CSSProperty):
    name="column-rule-color"
    value_logic = ValueLogic(
        # default=None, # I know this is overridden by ValueLogic to None, but the value cannot exist
        value_choice={
            str: COLORS_STR,
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRuleStyle(CSSProperty):
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
class ColumnRuleWidth(CSSProperty):
    name="column-rule-width"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            str:BORDERWIDTH,
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnRule(CSSPropertyShorthand):
    width:  ColumnRuleWidth
    style:  ColumnRuleStyle
    color:  ColumnRuleColor

    __slots__ = [
        "width", "style", "color"
    ]
    def __init__(
            self,
            width= ColumnRuleWidth.value_logic.default,
            style= ColumnRuleStyle.value_logic.default,
            color= ColumnRuleColor.value_logic.default,
    ):
        self.width = ColumnRuleWidth(width)
        self.style = ColumnRuleStyle(style)
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
class ColumnSpan(CSSProperty):
    name="column-span"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str:("all",),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ColumnWidth(CSSProperty):
    name="column-width"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Columns(CSSPropertyShorthand):
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
class Content(CSSProperty):
    name="content"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            None:None,
            str:(NORMAL, "counter", "open-quote", "close-quote", "no-open-quote", "no-close-quote"),
            Url:Any,
            AnyStr:Any # as long as an object has a __str__, this should be fine
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class CounterIncrement(CSSProperty):
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
class CounterReset(CSSProperty):
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
class Cursor(CSSProperty):
    name="cursor"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            (Url, str):(Any, CURSOR),
            str: CURSOR
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Direction(CSSProperty):
    name="direction"
    value_logic = ValueLogic(
        default="ltr",
        value_choice={
            str:("ltr","rtl")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Display(CSSProperty):
    name="display"
    value_logic = ValueLogic(
        value_choice={
            None:None,
            str:(
                "inline","block","contents","flex","grid","inline-block", "inline-flex", "inline-grid", "inline-table",
                "list-item", "run-in", "table","table-caption", "table-column-group", "table-header-group",
                "table-footer-group", "table-row-group", "table-cell", "table-column", "table-row"
            )
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class EmptyCells(CSSProperty):
    name="empty-cells"
    value_logic = ValueLogic(
        default="show",
        value_choice={
            str:("show", "hide")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Filter(CSSProperty):
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
class FlexBasis(CSSProperty):
    name="flex-basis"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FlexDirection(CSSProperty):
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
class FlexFlow(CSSProperty):
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
class FlexGrow(CSSProperty):
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
class FlexShrink(CSSProperty):
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
class FlexWrap(CSSProperty):
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
class Flex(CSSPropertyShorthand):
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
class Float(CSSProperty):
    name="float"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: (LEFT, RIGHT)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontFamily(CSSProperty):
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
class FontFeatureSetting(CSSProperty):
    name="font-feature-setting"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str:(NORMAL,),
            (str, str): (Any,("on","off")),
            (str, int): (Any,(1,0)),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontKerning(CSSProperty):
    name="font-kerning"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(NORMAL, AUTO),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontSize(CSSProperty):
    name="font-size"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            str:(MEDIUM,"xx-small","x-small","small","large","x-large","xx-large","smaller","larger"),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontSizeAdjust(CSSProperty):
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
class FontStretch(CSSProperty):
    name="font-stretch"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (
                "ultra-condensed","extra-condensed","condensed","semi-condensed",NORMAL,"semi-expanded","expanded",
                "extra-expanded","ultra-expanded"
            ),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontStyle(CSSProperty):
    name="font-style"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL, "italic", "oblique"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontVariant(CSSProperty):
    name="font-variant"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL, "small-caps"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontVariantCaps(CSSProperty):
    name="font-variant-caps"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (
                NORMAL,"small-caps","all-small-caps","petite-caps","all-petite-caps","unicase","titling-caps","unset"
            ),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class FontWeight(CSSProperty):
    name="font-weight"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,"bold","bolder","lighter"),
            int: (100,200,300,400,500,600,700,800,900)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Font(CSSPropertyShorthand):
    style: FontStyle
    variant: FontVariant
    weight: FontWeight
    size: FontSize
    family: FontFamily

    __slots__ = [
        "style","variant","weight","size","family",
    ]
    def __init__(
            self,
            style=FontStyle.value_logic.default,
            variant=FontVariant.value_logic.default,
            weight=FontWeight.value_logic.default,
            size=FontSize.value_logic.default,
            family=FontFamily.value_logic.default,
    ):
        self.style  =FontStyle(style)
        self.variant=FontVariant(variant)
        self.weight =FontWeight(weight)
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
class Gap(CSSProperty):
    name="gap"
    value_logic = ValueLogic(
        default=(NORMAL, NORMAL),
        value_choice={
            (str,str):(NORMAL,NORMAL),
            **{(length, str): (Any, NORMAL) for length in LENGTHS_TUPLE},
            **{(str, length): (NORMAL, Any) for length in LENGTHS_TUPLE},
            **{length_product:(Any,Any) for length_product in itertools.product(LENGTHS_TUPLE,repeat=2)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoColumns(CSSProperty):
    name="grid-auto-columns"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,"max-content","min-content"),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoFlow(CSSProperty):
    name="grid-auto-flow"
    value_logic = ValueLogic(
        default="row",
        value_choice={
            str: ("row","column", "dense", "row dense", "column dense"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridAutoRows(CSSProperty):
    name="grid-auto-rows"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,"max-content","min-content"),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumnEnd(CSSProperty):
    name="grid-column-end"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            (str, int): (("span",),Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumnGap(CSSProperty):
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
class GridColumnStart(CSSProperty):
    name="grid-column-start"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            (str, int): (("span",),Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridColumn(CSSPropertyShorthand):
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
class GridRowEnd(CSSProperty):
    name="grid-row-end"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            (str, int): (("span",),Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridRowGap(CSSProperty):
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
class GridRowStart(CSSProperty):
    name="grid-row-start"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            (str, int): (("span",),Any),
            int: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridRow(CSSPropertyShorthand):
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
class GridGap(CSSPropertyShorthand):
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
class GridTemplateAreas(CSSProperty):
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
class GridTemplateColumns(CSSProperty):
    name="grid-template-columns"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: (AUTO, "max-content", "min-content"),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplateRows(CSSProperty):
    name="grid-template-rows"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: (AUTO, "max-content", "min-content"),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class GridTemplate(CSSPropertyShorthand):
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
class GridArea(CSSPropertyShorthand):
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
class Grid(CSSPropertyShorthand):
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
class HangingPunctuation(CSSProperty):
    name="hanging-punctuation"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: ("first","last","allow-end","force-end"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Height(CSSProperty):
    name="height"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Hyphens(CSSProperty):
    name="hyphens"
    value_logic = ValueLogic(
        default="manual",
        value_choice={
            None:None,
            str: ("manual", AUTO),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ImageRendering(CSSProperty):
    name="image-rendering"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str: (AUTO,"smooth","high-quality","crisp-edges","pixelated"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Isolation(CSSProperty):
    name="isolation"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str: (AUTO,"isolate"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class JustifyContent(CSSProperty):
    name="justify-content"
    value_logic = ValueLogic(
        default="flex-start",
        value_choice={
            None:None,
            str: ("flex-start","flex-end","center","space-between","space-around","space-evenly"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Left(CSSProperty):
    name=LEFT
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class LetterSpacing(CSSProperty):
    name="letter-spacing"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class LineHeight(CSSProperty):
    name="line-height"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,),
            int: Any,
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyleImage(CSSProperty):
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
class ListStylePosition(CSSProperty):
    name="list-style-position"
    value_logic = ValueLogic(
        default="outside",
        value_choice={
            str: ("inside", "outside")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyleType(CSSProperty):
    name="list-style-position"
    value_logic = ValueLogic(
        default="disc",
        value_choice={
            str: (
                "disc", "armenian", "circle", "cjk-ideographic", "decimal", "decimal-leading-zero", "georgian",
                "hebrew", "hiragana", "hiragana-iroha", "katakana", "katakana-iroha", "lower-alpha", "lower-greek" ,
                "lower-latin", "lower-roman", "square", "upper-alpha", "upper-greek", "upper-latin", "upper-roman"
            )
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ListStyle(CSSPropertyShorthand):
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
class MarginBottom(CSSProperty):
    name="margin-bottom"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginLeft(CSSProperty):
    name="margin-left"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginRight(CSSProperty):
    name="margin-right"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MarginTop(CSSProperty):
    name="margin-top"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            str: (AUTO,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Margin(CSSPropertyShorthand):
    top: MarginTop
    right: MarginRight
    bottom: MarginBottom
    left: MarginLeft

    __slots__ = [
        "top",RIGHT,"bottom", LEFT
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
class MaskImage(CSSProperty):
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
class MaskMode(CSSProperty):
    name="mask-mode"
    value_logic = ValueLogic(
        default="match-source",
        value_choice={
            str: ("match-source","luminance","alpha")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskOrigin(CSSProperty):
    name="mask-origin"
    value_logic = ValueLogic(
        default="border-box",
        value_choice={
            str: ("border-box","content-box","padding-box","margin-box","fill-box","stroke-box","view-box")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskPosition(CSSProperty):
    name="mask-position"
    value_logic = ValueLogic(
        default=(PERCENT_EMPTY, PERCENT_EMPTY),
        value_choice={
            (Percent, Percent):(Any, Any),
            (str,str): ((LEFT, RIGHT, "center"),("top", "center", "bottom")),
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                LENGTHS_TUPLE,
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskRepeat(CSSProperty):
    name="mask-repeat"
    value_logic = ValueLogic(
        default="repeat",
        value_choice={
            str: ("repeat","repeat-x","repeat-y","space","round","no-repeat")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaskSize(CSSProperty):
    name="mask-size"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO, "contain", "cover"),
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaxHeight(CSSProperty):
    name="max-height"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MaxWidth(CSSProperty):
    name="max-width"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MinHeight(CSSProperty):
    name="min-height"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MinWidth(CSSProperty):
    name="min-width"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class MixBlendMode(CSSProperty):
    name="mix-blend-mode"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: BLENDMODES
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ObjectFit(CSSProperty):
    name="object-fit"
    value_logic = ValueLogic(
        default="fill",
        value_choice={
            None:None,
            str: ("fill", "contain", "cover", "scale-down")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ObjectPosition(CSSProperty):
    name="object-position"
    value_logic = ValueLogic(
        default=(Percent(50), Percent(50)),
        value_choice={
            str:(LEFT, RIGHT, "center"),
            **{length_combo: (Any, Any) for length_combo in itertools.product(
                (Pixel, Percent),
                repeat=2
            )}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Opacity(CSSProperty):
    name="opacity"
    value_logic = ValueLogic(
        default=1,
        value_choice={
            int: (0,1),
            float: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Order(CSSProperty):
    name="order"
    value_logic = ValueLogic(
        default=0,
        value_choice={
            int: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Orphans(CSSProperty):
    name="orphans"
    value_logic = ValueLogic(
        default=2,
        value_choice={
            int: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OutlineColor(CSSProperty):
    name="outline-color"
    value_logic = ValueLogic(
        value_choice={
            str: ("invert", *COLORS_STR),
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OutlineOffset(CSSProperty):
    name="outline-offset"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OutlineStyle(CSSProperty):
    name="outline-style"
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
class OutlineWidth(CSSProperty):
    name="outline-style"
    value_logic = ValueLogic(
        default=MEDIUM,
        value_choice={
            str: BORDERWIDTH,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Outline(CSSPropertyShorthand):
    width: OutlineWidth
    style: OutlineStyle
    color: OutlineColor

    __slots__ = [
        "width","style","color",
    ]
    def __init__(
            self,
            width=MarginTop.value_logic.default,
            style=MarginRight.value_logic.default,
            color=MarginBottom.value_logic.default,
    ):
        self.width=OutlineWidth(width)
        self.style=OutlineStyle(style)
        self.color=OutlineColor(color)

    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.width._value.printer(),
            self.style._value.printer(),
            self.color._value.printer(),
        ))
        return f"outline: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class Overflow(CSSProperty):
    name="overflow"
    value_logic = ValueLogic(
        default=VISIBLE,
        value_choice={
            str: (VISIBLE,"hidden","clip","scroll",AUTO)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OverflowWrap(CSSProperty):
    name="overflow-wrap"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: ("anywhere",NORMAL,"break-word")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OverflowX(CSSProperty):
    name="overflow-x"
    value_logic = ValueLogic(
        default=VISIBLE,
        value_choice={
            str: (VISIBLE,"hidden","scroll",AUTO)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class OverflowY(CSSProperty):
    name="overflow-y"
    value_logic = ValueLogic(
        default=VISIBLE,
        value_choice={
            str: (VISIBLE,"hidden","scroll",AUTO)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PaddingBottom(CSSProperty):
    name="padding-bottom"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PaddingTop(CSSProperty):
    name="padding-top"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PaddingLeft(CSSProperty):
    name="padding-left"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PaddingRight(CSSProperty):
    name="padding-right"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            Percent: Any,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Padding(CSSPropertyShorthand):
    top: PaddingTop
    right: PaddingRight
    bottom: PaddingBottom
    left: PaddingLeft

    __slots__ = [
        "top",RIGHT,"bottom", LEFT
    ]
    def __init__(
            self,
            top=PaddingTop.value_logic.default,
            right=PaddingRight.value_logic.default,
            bottom=PaddingBottom.value_logic.default,
            left=PaddingLeft.value_logic.default,
    ):
        self.top=PaddingTop(top)
        self.right=PaddingRight(right)
        self.bottom=PaddingBottom(bottom)
        self.left=PaddingLeft(left)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.top._value.printer(),
            self.right._value.printer(),
            self.bottom._value.printer(),
            self.left._value.printer(),
        ))
        return f"padding: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class PageBreakAfter(CSSProperty):
    name="page-break-after"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,"always","avoid",LEFT,RIGHT)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PageBreakBefore(CSSProperty):
    name="page-break-before"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,"always","avoid",LEFT,RIGHT)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PageBreakInside(CSSProperty):
    name="page-break-inside"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,"always","avoid",LEFT,RIGHT)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Perspective(CSSProperty):
    name="perspective"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PerspectiveOrigin(CSSProperty):
    name="perspective-origin"
    value_logic = ValueLogic(
        default=(Percent(50), Percent(50)),
        value_choice={
            (str,str): ((LEFT, RIGHT, "center"), ("top", "center", "bottom")),
            **{(val, str): (Any, ("top", "center", "bottom")) for val in (*LENGTHS_TUPLE, Percent)},
            **{(str, val): ((LEFT, RIGHT, "center"), Any) for val in (*LENGTHS_TUPLE, Percent)}
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class PointerEvents(CSSProperty):
    name="pointer-events"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str: (AUTO,)
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Position(CSSProperty):
    name="position"
    value_logic = ValueLogic(
        default="static",
        value_choice={
            None:None,
            str: ("static", "absolute", "fixed", "relative", "sticky")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Quotes(CSSProperty):
    name="quotes"
    value_logic = ValueLogic(
        value_choice=ANY,
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Resize(CSSProperty):
    name="resize"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: ("both","horizontal","vertical")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Right(CSSProperty):
    name=RIGHT
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            **PERCENT,
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class RowGap(CSSProperty):
    name="row-gap"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,),
            **LENGTHS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ScrollBehavior(CSSProperty):
    name="scroll-behavior"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO, "smooth"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TabSize(CSSProperty):
    name="tab-size"
    value_logic = ValueLogic(
        default=8,
        value_choice={
            int:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TableLayout(CSSProperty):
    name="table-layout"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO, "fixed")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextAlign(CSSProperty):
    name="text-align"
    value_logic = ValueLogic(
        default=LEFT,
        value_choice={
            str:(LEFT, RIGHT, "center", "justify")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextAlignLast(CSSProperty):
    name="text-align-last"
    value_logic = ValueLogic(
        default=LEFT,
        value_choice={
            str:(LEFT, RIGHT, "center", "justify", "start", "end")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextDecorationColor(CSSProperty):
    name="text-decoration-color"
    value_logic = ValueLogic(
        value_choice={
            str:COLORS_STR,
            **COLORS_CHOICE
        },
    )
    def __init__(self, value, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextDecorationLine(CSSProperty):
    name="text-decoration-line"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str: ("underline", "overline", "line-through"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextDecorationStyle(CSSProperty):
    name="text-decoration-style"
    value_logic = ValueLogic(
        default="solid",
        value_choice={
            None:None,
            str: ("solid", "double", "dotted", "dashed", "wavy"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextDecorationThickness(CSSProperty):
    name="text-decoration-thickness"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str: (AUTO, "from-font"),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextDecoration(CSSPropertyShorthand):
    line: TextDecorationLine
    color: TextDecorationColor
    style: TextDecorationStyle
    thickness: TextDecorationThickness

    __slots__ = [
        "line","color","style", "thickness"
    ]
    def __init__(
            self,
            line=TextDecorationLine.value_logic.default,
            color=TextDecorationColor.value_logic.default,
            style=TextDecorationStyle.value_logic.default,
            thickness=TextDecorationThickness.value_logic.default,
    ):
        self.line=TextDecorationLine(line)
        self.color=TextDecorationColor(color)
        self.style=TextDecorationStyle(style)
        self.thickness=TextDecorationThickness(thickness)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.line._value.printer(),
            self.color._value.printer(),
            self.style._value.printer(),
            self.thickness._value.printer(),
        ))
        return f"text-decoration: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class TextIndent(CSSProperty):
    name="text-indent"
    value_logic = ValueLogic(
        default=PIXEL_EMPTY,
        value_choice={
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextJustify(CSSProperty):
    name="text-justify"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str:(AUTO, "inter-word", "inter-character")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextOverflow(CSSProperty):
    name="text-overflow"
    value_logic = ValueLogic(
        default="clip",
        value_choice={
            str:Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextShadow(CSSProperty):
    name="text-shadow"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None: None,
            # h-shadow,  v-shadow,   blur,   spread, color
            (Pixel, Pixel, Pixel, Pixel, COLORS_UNION): (Any, Any, Any, Any, Any),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TextTransform(CSSProperty):
    name="text-transform"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            str:("capitalize","uppercase","lowercase")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Top(CSSProperty):
    name="top"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str:(AUTO,),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Transform(CSSProperty):
    name="transform"
    value_logic = ValueLogic(
        default=None,
        value_choice={
            None:None,
            **TRANSFORMS
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransformOrigin(CSSProperty):
    name="transform-origin"
    value_logic = ValueLogic(
        default=(Percent(50), Percent(50), PIXEL_EMPTY),
        value_choice={
            (str,str): ((LEFT, RIGHT, "center"), ("top", "center", "bottom")),
            **{(val, str): (Any, ("top", "center", "bottom")) for val in (*LENGTHS_TUPLE, Percent)},
            **{(str, val): ((LEFT, RIGHT, "center"), Any) for val in (*LENGTHS_TUPLE, Percent)},
            **{(str, str, val): ((LEFT, RIGHT, "center"), ("top", "center", "bottom"), Any) for val in (*LENGTHS_TUPLE, Percent)},
            **{(val, str, val): (Any, ("top", "center", "bottom"), Any) for val in (*LENGTHS_TUPLE, Percent)},
            **{(str, val, val): ((LEFT, RIGHT, "center"), Any, Any) for val in (*LENGTHS_TUPLE, Percent)},
            **{val_combination: (Any,Any,Any) for val_combination in itertools.product((*LENGTHS_TUPLE, Percent), repeat=3)},
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransformStyle(CSSProperty):
    name="transform-style"
    value_logic = ValueLogic(
        default="flat",
        value_choice={
            str:("flat","preserve-3d")
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransitionDelay(CSSProperty):
    name="transition-delay"
    value_logic = ValueLogic(
        default=SECOND_EMPTY,
        value_choice={
            Second: Any,
            MilliSecond: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransitionDuration(CSSProperty):
    name="transition-duration"
    value_logic = ValueLogic(
        default=SECOND_EMPTY,
        value_choice={
            Second: Any,
            MilliSecond: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransitionProperty(CSSProperty):
    name="transition-property"
    value_logic = ValueLogic(
        default="all",
        value_choice={
            str: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class TransitionTimingFunction(CSSProperty):
    name="transition-timing-function"
    value_logic = ValueLogic(
        default="ease",
        value_choice={
            str: ("ease", "linear", "ease-in", "ease-out", "ease-in-out", "step-start","step-end"),
            CubicBezier: Any,
            Steps: Any
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Transition(CSSPropertyShorthand):
    property: TransitionProperty
    duration: TransitionDuration
    timing_function: TransitionTimingFunction
    delay: TransitionDelay

    __slots__ = [
        "property","duration","timing_function", "delay"
    ]
    def __init__(
            self,
            property_=TransitionProperty.value_logic.default,
            duration=TransitionDuration.value_logic.default,
            timing_function=TransitionTimingFunction.value_logic.default,
            delay=TransitionDelay.value_logic.default,
    ):
        self.property=TransitionProperty(property_)
        self.duration=TransitionDuration(duration)
        self.timing_function=TransitionTimingFunction(timing_function)
        self.delay=TransitionDelay(delay)
    # noinspection PyProtectedMember
    def printer(self) -> str:
        parts = " ".join((
            self.property._value.printer(),
            self.duration._value.printer(),
            self.timing_function._value.printer(),
            self.delay._value.printer(),
        ))
        return f"transition: {parts}"
# ----------------------------------------------------------------------------------------------------------------------
class UnicodeBidi(CSSProperty):
    name="unicode-bidi"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL, "embed", "bidi-override"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class UserSelect(CSSProperty):
    name="user-select"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            None:None,
            str: (AUTO, "text"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class VerticalAlign(CSSProperty):
    name="vertical-align"
    value_logic = ValueLogic(
        default="baseline",
        value_choice={
            str: ("baseline","sub","super","top","text-top","middle","bottom","text-bottom"),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Visibility(CSSProperty):
    name="visibility"
    value_logic = ValueLogic(
        default=VISIBLE,
        value_choice={
            str: (VISIBLE, "hidden", "collapse"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class WhiteSpace(CSSProperty):
    name="white-space"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,"nowrap", "pre", "pre-line", "pre-wrap"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Widows(CSSProperty):
    name="widows"
    value_logic = ValueLogic(
        default=2,
        value_choice={
            int: Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class Width(CSSProperty):
    name="width"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            **LENGTHS,
            **PERCENT
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class WordBreak(CSSProperty):
    name="word-break"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,"break-all","keep-all","break-word"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class WordSpacing(CSSProperty):
    name="word-spacing"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL,),
            **LENGTHS,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class WordWrap(CSSProperty):
    name="word-wrap"
    value_logic = ValueLogic(
        default=NORMAL,
        value_choice={
            str: (NORMAL, "break-word"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class WritingMode(CSSProperty):
    name="writing-mode"
    value_logic = ValueLogic(
        default="horizontal-tb",
        value_choice={
            str: ("horizontal-tb", "vertical-rl", "vertical-lr"),
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
# ----------------------------------------------------------------------------------------------------------------------
class ZIndex(CSSProperty):
    name="z-index"
    value_logic = ValueLogic(
        default=AUTO,
        value_choice={
            str: (AUTO,),
            int:Any,
        },
    )
    def __init__(self, value=value_logic.default, **kwargs):
        super().__init__(value, **kwargs)
