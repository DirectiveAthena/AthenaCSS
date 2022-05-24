# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Elements.CSSElement import CSSElement
from AthenaCSS.Objects.Selectors.CSSSelector import CSSSelector

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Class","Id","Attribute","ColonElement","ColonElementDouble","ColonActive","Colonafter","Colonbefore","ColonChecked",
    "ColonDefault","ColonDisabled","ColonEmpty","ColonEnabled","ColonFirstChild","ColonFirstLetter","ColonFirstLine",
    "ColonFirstOfType","ColonFocus","ColonFullscreen","ColonHover","ColonInRange","ColonIndeterminate","ColonInvalid",
    "ColonLang","ColonLastChild","ColonLastOfType","ColonLink","ColonMarker","ColonNot","ColonNthChild","ColonNthLastChild",
    "ColonNthLastOfType","ColonNthOfType","ColonOnlyOfType","ColonOnlyChild","ColonOptional","ColonOutOfRange",
    "ColonPlaceholder","ColonReadOnly","ColonReadWrite","ColonRequired","ColonRoot","ColonSelection","ColonTarget",
    "ColonValid","ColonVisited","Element","A","Abbr","Acronym","Address","Applet","Area","Article","Aside","Audio","B",
    "Base","Basefont","Bdi","Bdo","Big","Blockquote","Body","Br","Button","Canvas","Caption","Center","Cite","Code","Col",
    "Colgroup","Data","Datalist","Dd","Del","Details","Dfn","Dialog","Dir","Div","Dl","Dt","Em","Embed","Fieldset",
    "Figcaption","Figure","Font","Footer","Form","Frame","Frameset","H1","H2","H3","H4","H5","H6","Head","Header","Hr",
    "Html","I","Iframe","Img","Input","Ins","Kbd","Label","Legend","Li","Link","Main","Map","Mark","Meta","Meter","Nav",
    "Noframes","Noscript","Object","Ol","Optgroup","Option","Output","P","Param","Picture","Pre","Progress","Q","Rp",
    "Rt","Ruby","S","Samp","Script","Section","Select","Small","Source","Span","Strike","Strong","Style","Sub",
    "Summary","Sup","Svg","Table","Tbody","Td","Template","Textarea","Tfoot","Th","Thead","Time","Title","Tr","Track",
    "Tt","U","Ul","Var","Video","Wbr"
]

# ----------------------------------------------------------------------------------------------------------------------
# - SupportCode -
# ----------------------------------------------------------------------------------------------------------------------
RB_OPEN = "("
RB_CLOSE= ")"

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Class(CSSElement):
    prefix="."

class Id(CSSElement):
    prefix="#"

# ----------------------------------------------------------------------------------------------------------------------
class Attribute(CSSElement):
    prefix = "["
    sufix = "]"

    def __init__(self, attr:str):
        self.parts = [*self._partPrep(attr)]
    def __str__(self):
        return "".join(self.parts)
    def _partPrep(self, part):
        return self.prefix, part, self.sufix

    @classmethod
    def equals(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}={attr_value}""")
    @classmethod
    def contains_word(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}~={attr_value}""")
    @classmethod
    def starting_equal(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}|={attr_value}""")
    @classmethod
    def begins_with(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}^={attr_value}""")
    @classmethod
    def ends_with(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}$={attr_value}""")
    @classmethod
    def contains_substring(cls, attr_name, attr_value) -> Attribute:
        if isinstance(attr_value, str):
            attr_value = f'"{attr_value}"'
        return cls(fr"""{attr_name}*={attr_value}""")

# ----------------------------------------------------------------------------------------------------------------------
class ColonElement(CSSElement):
    prefix = ":"
class ColonElementDouble(CSSElement):
    prefix = "::"

class ColonActive(ColonElement):
    defined_name = "active"
class Colonafter(ColonElementDouble):
    defined_name = "after"
class Colonbefore(ColonElementDouble):
    defined_name = "before"
class ColonChecked(ColonElement):
    defined_name = "checked"
class ColonDefault(ColonElement):
    defined_name = "default"
class ColonDisabled(ColonElement):
    defined_name = "disabled"
class ColonEmpty(ColonElement):
    defined_name = "empty"
class ColonEnabled(ColonElement):
    defined_name = "enabled"
class ColonFirstChild(ColonElement):
    defined_name = "first-child"
class ColonFirstLetter(ColonElementDouble):
    defined_name = "first-letter"
class ColonFirstLine(ColonElementDouble):
    defined_name = "first-line"
class ColonFirstOfType(ColonElement):
    defined_name = "first-of-type"
class ColonFocus(ColonElement):
    defined_name = "focus"
class ColonFullscreen(ColonElement):
    defined_name = "fullscreen"
class ColonHover(ColonElement):
    defined_name = "hover"
class ColonInRange(ColonElement):
    defined_name = "in-range"
class ColonIndeterminate(ColonElement):
    defined_name = "indeterminate"
class ColonInvalid(ColonElement):
    defined_name = "invalid"
class ColonLang(ColonElement):
    defined_name = "lang"
    # set a new init here to correctly define the language.
    #   Given it's a colon element, it's structure is known and can be defined in the following way
    def __init__(self, language:str):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, language, RB_CLOSE]
class ColonLastChild(ColonElement):
    defined_name = "last-child"
class ColonLastOfType(ColonElement):
    defined_name = "last-of-type"
class ColonLink(ColonElement):
    defined_name = "link"
class ColonMarker(ColonElementDouble):
    defined_name = "marker"
class ColonNot(ColonElement):
    defined_name = "not"
    # set a new init here to correctly define the not statement.
    #   Given it's a colon element, it's structure is known and can be defined in the following way
    def __init__(self, selector:CSSSelector):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, selector, RB_CLOSE]
class ColonNthChild(ColonElement):
    defined_name = "nth-child"
    def __init__(self, n:int):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, n, RB_CLOSE]
class ColonNthLastChild(ColonElement):
    defined_name = "nth-last-child"
    def __init__(self, n:int):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, n, RB_CLOSE]
class ColonNthLastOfType(ColonElement):
    defined_name = "nth-last-of-child"
    def __init__(self, n:int):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, n, RB_CLOSE]
class ColonNthOfType(ColonElement):
    defined_name = "nth-of-child"
    def __init__(self, n:int):
        self.parts = [self.prefix, self.defined_name, RB_OPEN, n, RB_CLOSE]
class ColonOnlyOfType(ColonElement):
    defined_name = "only-of-type"
class ColonOnlyChild(ColonElement):
    defined_name = "only-child"
class ColonOptional(ColonElement):
    defined_name = "optional"
class ColonOutOfRange(ColonElement):
    defined_name = "out-of-range"
class ColonPlaceholder(ColonElementDouble):
    defined_name = "placeholder"
class ColonReadOnly(ColonElement):
    defined_name = "read-only"
class ColonReadWrite(ColonElement):
    defined_name = "read-write"
class ColonRequired(ColonElement):
    defined_name = "required"
class ColonRoot(ColonElement):
    defined_name = "root"
class ColonSelection(ColonElementDouble):
    defined_name = "selection"
class ColonTarget(ColonElement):
    defined_name = "target"
class ColonValid(ColonElement):
    defined_name = "valid"
class ColonVisited(ColonElement):
    defined_name = "visited"

# ----------------------------------------------------------------------------------------------------------------------
class Element(CSSElement):
    pass

class A(Element):
    defined_name = "a"
class Abbr(Element):
    defined_name = "abbr"
class Acronym(Element):
    defined_name = "acronym"
class Address(Element):
    defined_name = "address"
class Applet(Element):
    defined_name = "applet"
class Area(Element):
    defined_name = "area"
class Article(Element):
    defined_name = "article"
class Aside(Element):
    defined_name = "aside"
class Audio(Element):
    defined_name = "audio"
class B(Element):
    defined_name = "b"
class Base(Element):
    defined_name = "base"
class Basefont(Element):
    defined_name = "basefont"
class Bdi(Element):
    defined_name = "bdi"
class Bdo(Element):
    defined_name = "bdo"
class Big(Element):
    defined_name = "big"
class Blockquote(Element):
    defined_name = "blockquote"
class Body(Element):
    defined_name = "body"
class Br(Element):
    defined_name = "br"
class Button(Element):
    defined_name = "button"
class Canvas(Element):
    defined_name = "canvas"
class Caption(Element):
    defined_name = "caption"
class Center(Element):
    defined_name = "center"
class Cite(Element):
    defined_name = "cite"
class Code(Element):
    defined_name = "code"
class Col(Element):
    defined_name = "col"
class Colgroup(Element):
    defined_name = "colgroup"
class Data(Element):
    defined_name = "data"
class Datalist(Element):
    defined_name = "datalist"
class Dd(Element):
    defined_name = "dd"
class Del(Element):
    defined_name = "del"
class Details(Element):
    defined_name = "details"
class Dfn(Element):
    defined_name = "dfn"
class Dialog(Element):
    defined_name = "dialog"
class Dir(Element):
    defined_name = "dir"
class Div(Element):
    defined_name = "div"
class Dl(Element):
    defined_name = "dl"
class Dt(Element):
    defined_name = "dt"
class Em(Element):
    defined_name = "em"
class Embed(Element):
    defined_name = "embed"
class Fieldset(Element):
    defined_name = "fieldset"
class Figcaption(Element):
    defined_name = "figcaption"
class Figure(Element):
    defined_name = "figure"
class Font(Element):
    defined_name = "font"
class Footer(Element):
    defined_name = "footer"
class Form(Element):
    defined_name = "form"
class Frame(Element):
    defined_name = "frame"
class Frameset(Element):
    defined_name = "frameset"
class H1(Element):
    defined_name = "h1"
class H2(Element):
    defined_name = "h2"
class H3(Element):
    defined_name = "h3"
class H4(Element):
    defined_name = "h4"
class H5(Element):
    defined_name = "h5"
class H6(Element):
    defined_name = "h6"
class Head(Element):
    defined_name = "head"
class Header(Element):
    defined_name = "header"
class Hr(Element):
    defined_name = "hr"
class Html(Element):
    defined_name = "html"
class I(Element):
    defined_name = "i>"
class Iframe(Element):
    defined_name = "iframe"
class Img(Element):
    defined_name = "img"
class Input(Element):
    defined_name = "input"
class Ins(Element):
    defined_name = "ins"
class Kbd(Element):
    defined_name = "kbd"
class Label(Element):
    defined_name = "label"
class Legend(Element):
    defined_name = "legend"
class Li(Element):
    defined_name = "li"
class Link(Element):
    defined_name = "link"
class Main(Element):
    defined_name = "main"
class Map(Element):
    defined_name = "map"
class Mark(Element):
    defined_name = "mark"
class Meta(Element):
    defined_name = "meta"
class Meter(Element):
    defined_name = "meter"
class Nav(Element):
    defined_name = "nav"
class Noframes(Element):
    defined_name = "noframes"
class Noscript(Element):
    defined_name = "noscript"
class Object(Element):
    defined_name = "object"
class Ol(Element):
    defined_name = "ol"
class Optgroup(Element):
    defined_name = "optgroup"
class Option(Element):
    defined_name = "option"
class Output(Element):
    defined_name = "output"
class P(Element):
    defined_name = "p>"
class Param(Element):
    defined_name = "param"
class Picture(Element):
    defined_name = "picture"
class Pre(Element):
    defined_name = "pre"
class Progress(Element):
    defined_name = "progress"
class Q(Element):
    defined_name = "q>"
class Rp(Element):
    defined_name = "rp"
class Rt(Element):
    defined_name = "rt"
class Ruby(Element):
    defined_name = "ruby"
class S(Element):
    defined_name = "s>"
class Samp(Element):
    defined_name = "samp"
class Script(Element):
    defined_name = "script"
class Section(Element):
    defined_name = "section"
class Select(Element):
    defined_name = "select"
class Small(Element):
    defined_name = "small"
class Source(Element):
    defined_name = "source"
class Span(Element):
    defined_name = "span"
class Strike(Element):
    defined_name = "strike"
class Strong(Element):
    defined_name = "strong"
class Style(Element):
    defined_name = "style"
class Sub(Element):
    defined_name = "sub"
class Summary(Element):
    defined_name = "summary"
class Sup(Element):
    defined_name = "sup"
class Svg(Element):
    defined_name = "svg"
class Table(Element):
    defined_name = "table"
class Tbody(Element):
    defined_name = "tbody"
class Td(Element):
    defined_name = "td"
class Template(Element):
    defined_name = "template"
class Textarea(Element):
    defined_name = "textarea"
class Tfoot(Element):
    defined_name = "tfoot"
class Th(Element):
    defined_name = "th"
class Thead(Element):
    defined_name = "thead"
class Time(Element):
    defined_name = "time"
class Title(Element):
    defined_name = "title"
class Tr(Element):
    defined_name = "tr"
class Track(Element):
    defined_name = "track"
class Tt(Element):
    defined_name = "tt"
class U(Element):
    defined_name = "u>"
class Ul(Element):
    defined_name = "ul"
class Var(Element):
    defined_name = "var"
class Video(Element):
    defined_name = "video"
class Wbr(Element):
    defined_name = "wbr"