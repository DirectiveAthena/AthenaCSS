# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.Objects.ElementSelection.CSSElement import CSSElement
from AthenaCSS.Objects.ElementSelection.CSSPseudo import CSSPseudo

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "All","PseudoActive","Pseudoafter","Pseudobefore","PseudoChecked",
    "PseudoDefault","PseudoDisabled","PseudoEmpty","PseudoEnabled","PseudoFirstChild","PseudoFirstLetter","PseudoFirstLine",
    "PseudoFirstOfType","PseudoFocus","PseudoFullscreen","PseudoHover","PseudoInRange","PseudoIndeterminate","PseudoInvalid",
    "PseudoLang","PseudoLastChild","PseudoLastOfType","PseudoLink","PseudoMarker","PseudoNot","PseudoNthChild","PseudoNthLastChild",
    "PseudoNthLastOfType","PseudoNthOfType","PseudoOnlyOfType","PseudoOnlyChild","PseudoOptional","PseudoOutOfRange",
    "PseudoPlaceholder","PseudoReadOnly","PseudoReadWrite","PseudoRequired","PseudoRoot","PseudoSelection","PseudoTarget",
    "PseudoValid","PseudoVisited","A","Abbr","Acronym","Address","Applet","Area","Article","Aside","Audio","B",
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
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class All:
    @classmethod
    def __str__(cls):
        return "*"

# ----------------------------------------------------------------------------------------------------------------------
class PseudoActive(CSSPseudo):
    defined_name = ":active"
class Pseudoafter(CSSPseudo):
    defined_name = "::after"
class Pseudobefore(CSSPseudo):
    defined_name = "::before"
class PseudoChecked(CSSPseudo):
    defined_name = ":checked"
class PseudoDefault(CSSPseudo):
    defined_name = ":default"
class PseudoDisabled(CSSPseudo):
    defined_name = ":disabled"
class PseudoEmpty(CSSPseudo):
    defined_name = ":empty"
class PseudoEnabled(CSSPseudo):
    defined_name = ":enabled"
class PseudoFirstChild(CSSPseudo):
    defined_name = ":first-child"
class PseudoFirstLetter(CSSPseudo):
    defined_name = "first-::letter"
class PseudoFirstLine(CSSPseudo):
    defined_name = "first-::line"
class PseudoFirstOfType(CSSPseudo):
    defined_name = ":first-of-type"
class PseudoFocus(CSSPseudo):
    defined_name = ":focus"
class PseudoFullscreen(CSSPseudo):
    defined_name = ":fullscreen"
class PseudoHover(CSSPseudo):
    defined_name = ":hover"
class PseudoInRange(CSSPseudo):
    defined_name = ":in-range"
class PseudoIndeterminate(CSSPseudo):
    defined_name = ":indeterminate"
class PseudoInvalid(CSSPseudo):
    defined_name = ":invalid"
class PseudoLang(CSSPseudo):
    defined_name = ":lang"
class PseudoLastChild(CSSPseudo):
    defined_name = ":last-child"
class PseudoLastOfType(CSSPseudo):
    defined_name = ":last-of-type"
class PseudoLink(CSSPseudo):
    defined_name = ":link"
class PseudoMarker(CSSPseudo):
    defined_name = "::marker"
class PseudoNot(CSSPseudo):
    defined_name = ":not"
class PseudoNthChild(CSSPseudo):
    defined_name = ":nth-child"
class PseudoNthLastChild(CSSPseudo):
    defined_name = ":nth-last-child"
class PseudoNthLastOfType(CSSPseudo):
    defined_name = ":nth-last-of-child"
class PseudoNthOfType(CSSPseudo):
    defined_name = ":nth-of-child"
class PseudoOnlyOfType(CSSPseudo):
    defined_name = ":only-of-type"
class PseudoOnlyChild(CSSPseudo):
    defined_name = ":only-child"
class PseudoOptional(CSSPseudo):
    defined_name = ":optional"
class PseudoOutOfRange(CSSPseudo):
    defined_name = ":out-of-range"
class PseudoPlaceholder(CSSPseudo):
    defined_name = "::placeholder"
class PseudoReadOnly(CSSPseudo):
    defined_name = ":read-only"
class PseudoReadWrite(CSSPseudo):
    defined_name = ":read-write"
class PseudoRequired(CSSPseudo):
    defined_name = ":required"
class PseudoRoot(CSSPseudo):
    defined_name = ":root"
class PseudoSelection(CSSPseudo):
    defined_name = "::selection"
class PseudoTarget(CSSPseudo):
    defined_name = ":target"
class PseudoValid(CSSPseudo):
    defined_name = ":valid"
class PseudoVisited(CSSPseudo):
    defined_name = ":visited"

# ----------------------------------------------------------------------------------------------------------------------
class A(CSSElement):
    defined_name = "a"
class Abbr(CSSElement):
    defined_name = "abbr"
class Acronym(CSSElement):
    defined_name = "acronym"
class Address(CSSElement):
    defined_name = "address"
class Applet(CSSElement):
    defined_name = "applet"
class Area(CSSElement):
    defined_name = "area"
class Article(CSSElement):
    defined_name = "article"
class Aside(CSSElement):
    defined_name = "aside"
class Audio(CSSElement):
    defined_name = "audio"
class B(CSSElement):
    defined_name = "b"
class Base(CSSElement):
    defined_name = "base"
class Basefont(CSSElement):
    defined_name = "basefont"
class Bdi(CSSElement):
    defined_name = "bdi"
class Bdo(CSSElement):
    defined_name = "bdo"
class Big(CSSElement):
    defined_name = "big"
class Blockquote(CSSElement):
    defined_name = "blockquote"
class Body(CSSElement):
    defined_name = "body"
class Br(CSSElement):
    defined_name = "br"
class Button(CSSElement):
    defined_name = "button"
class Canvas(CSSElement):
    defined_name = "canvas"
class Caption(CSSElement):
    defined_name = "caption"
class Center(CSSElement):
    defined_name = "center"
class Cite(CSSElement):
    defined_name = "cite"
class Code(CSSElement):
    defined_name = "code"
class Col(CSSElement):
    defined_name = "col"
class Colgroup(CSSElement):
    defined_name = "colgroup"
class Data(CSSElement):
    defined_name = "data"
class Datalist(CSSElement):
    defined_name = "datalist"
class Dd(CSSElement):
    defined_name = "dd"
class Del(CSSElement):
    defined_name = "del"
class Details(CSSElement):
    defined_name = "details"
class Dfn(CSSElement):
    defined_name = "dfn"
class Dialog(CSSElement):
    defined_name = "dialog"
class Dir(CSSElement):
    defined_name = "dir"
class Div(CSSElement):
    defined_name = "div"
class Dl(CSSElement):
    defined_name = "dl"
class Dt(CSSElement):
    defined_name = "dt"
class Em(CSSElement):
    defined_name = "em"
class Embed(CSSElement):
    defined_name = "embed"
class Fieldset(CSSElement):
    defined_name = "fieldset"
class Figcaption(CSSElement):
    defined_name = "figcaption"
class Figure(CSSElement):
    defined_name = "figure"
class Font(CSSElement):
    defined_name = "font"
class Footer(CSSElement):
    defined_name = "footer"
class Form(CSSElement):
    defined_name = "form"
class Frame(CSSElement):
    defined_name = "frame"
class Frameset(CSSElement):
    defined_name = "frameset"
class H1(CSSElement):
    defined_name = "h1"
class H2(CSSElement):
    defined_name = "h2"
class H3(CSSElement):
    defined_name = "h3"
class H4(CSSElement):
    defined_name = "h4"
class H5(CSSElement):
    defined_name = "h5"
class H6(CSSElement):
    defined_name = "h6"
class Head(CSSElement):
    defined_name = "head"
class Header(CSSElement):
    defined_name = "header"
class Hr(CSSElement):
    defined_name = "hr"
class Html(CSSElement):
    defined_name = "html"
class I(CSSElement):
    defined_name = "i"
class Iframe(CSSElement):
    defined_name = "iframe"
class Img(CSSElement):
    defined_name = "img"
class Input(CSSElement):
    defined_name = "input"
class Ins(CSSElement):
    defined_name = "ins"
class Kbd(CSSElement):
    defined_name = "kbd"
class Label(CSSElement):
    defined_name = "label"
class Legend(CSSElement):
    defined_name = "legend"
class Li(CSSElement):
    defined_name = "li"
class Link(CSSElement):
    defined_name = "link"
class Main(CSSElement):
    defined_name = "main"
class Map(CSSElement):
    defined_name = "map"
class Mark(CSSElement):
    defined_name = "mark"
class Meta(CSSElement):
    defined_name = "meta"
class Meter(CSSElement):
    defined_name = "meter"
class Nav(CSSElement):
    defined_name = "nav"
class Noframes(CSSElement):
    defined_name = "noframes"
class Noscript(CSSElement):
    defined_name = "noscript"
class Object(CSSElement):
    defined_name = "object"
class Ol(CSSElement):
    defined_name = "ol"
class Optgroup(CSSElement):
    defined_name = "optgroup"
class Option(CSSElement):
    defined_name = "option"
class Output(CSSElement):
    defined_name = "output"
class P(CSSElement):
    defined_name = "p"
class Param(CSSElement):
    defined_name = "param"
class Picture(CSSElement):
    defined_name = "picture"
class Pre(CSSElement):
    defined_name = "pre"
class Progress(CSSElement):
    defined_name = "progress"
class Q(CSSElement):
    defined_name = "q"
class Rp(CSSElement):
    defined_name = "rp"
class Rt(CSSElement):
    defined_name = "rt"
class Ruby(CSSElement):
    defined_name = "ruby"
class S(CSSElement):
    defined_name = "s"
class Samp(CSSElement):
    defined_name = "samp"
class Script(CSSElement):
    defined_name = "script"
class Section(CSSElement):
    defined_name = "section"
class Select(CSSElement):
    defined_name = "select"
class Small(CSSElement):
    defined_name = "small"
class Source(CSSElement):
    defined_name = "source"
class Span(CSSElement):
    defined_name = "span"
class Strike(CSSElement):
    defined_name = "strike"
class Strong(CSSElement):
    defined_name = "strong"
class Style(CSSElement):
    defined_name = "style"
class Sub(CSSElement):
    defined_name = "sub"
class Summary(CSSElement):
    defined_name = "summary"
class Sup(CSSElement):
    defined_name = "sup"
class Svg(CSSElement):
    defined_name = "svg"
class Table(CSSElement):
    defined_name = "table"
class Tbody(CSSElement):
    defined_name = "tbody"
class Td(CSSElement):
    defined_name = "td"
class Template(CSSElement):
    defined_name = "template"
class Textarea(CSSElement):
    defined_name = "textarea"
class Tfoot(CSSElement):
    defined_name = "tfoot"
class Th(CSSElement):
    defined_name = "th"
class Thead(CSSElement):
    defined_name = "thead"
class Time(CSSElement):
    defined_name = "time"
class Title(CSSElement):
    defined_name = "title"
class Tr(CSSElement):
    defined_name = "tr"
class Track(CSSElement):
    defined_name = "track"
class Tt(CSSElement):
    defined_name = "tt"
class U(CSSElement):
    defined_name = "u"
class Ul(CSSElement):
    defined_name = "ul"
class Var(CSSElement):
    defined_name = "var"
class Video(CSSElement):
    defined_name = "video"
class Wbr(CSSElement):
    defined_name = "wbr"