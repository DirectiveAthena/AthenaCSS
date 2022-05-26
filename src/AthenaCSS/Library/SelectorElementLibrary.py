# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Elements.CSSElement import CSSElement
from AthenaCSS.Objects.Elements.CSSPseudo import CSSPseudo
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
All = CSSElement(defined_name="*")

# ----------------------------------------------------------------------------------------------------------------------
PseudoActive = CSSPseudo(defined_name=":active")
Pseudoafter = CSSPseudo(defined_name="::after")
Pseudobefore = CSSPseudo(defined_name="::before")
PseudoChecked = CSSPseudo(defined_name=":checked")
PseudoDefault = CSSPseudo(defined_name=":default")
PseudoDisabled = CSSPseudo(defined_name=":disabled")
PseudoEmpty = CSSPseudo(defined_name=":empty")
PseudoEnabled = CSSPseudo(defined_name=":enabled")
PseudoFirstChild = CSSPseudo(defined_name=":first-child")
PseudoFirstLetter = CSSPseudo(defined_name=":first-letter")
PseudoFirstLine = CSSPseudo(defined_name="::first-line")
PseudoFirstOfType = CSSPseudo(defined_name=":first-of-type")
PseudoFocus = CSSPseudo(defined_name=":focus")
PseudoFullscreen = CSSPseudo(defined_name=":fullscreen")
PseudoHover = CSSPseudo(defined_name=":hover")
PseudoInRange = CSSPseudo(defined_name=":in-range")
PseudoIndeterminate = CSSPseudo(defined_name=":indeterminate")
PseudoInvalid = CSSPseudo(defined_name=":invalid")
PseudoLang = CSSPseudo(defined_name=":lang")
PseudoLastChild = CSSPseudo(defined_name=":last-child")
PseudoLastOfType = CSSPseudo(defined_name=":last-of-type")
PseudoLink = CSSPseudo(defined_name=":link")
PseudoMarker = CSSPseudo(defined_name="::marker")
PseudoNot = CSSPseudo(defined_name=":not")
PseudoNthChild = CSSPseudo(defined_name=":nth-child")
PseudoNthLastChild = CSSPseudo(defined_name=":nth-last-child")
PseudoNthLastOfType = CSSPseudo(defined_name=":nth-last-of-child")
PseudoNthOfType = CSSPseudo(defined_name=":nth-of-child")
PseudoOnlyOfType = CSSPseudo(defined_name=":only-of-type")
PseudoOnlyChild = CSSPseudo(defined_name=":only-child")
PseudoOptional = CSSPseudo(defined_name=":optional")
PseudoOutOfRange = CSSPseudo(defined_name=":out-of-range")
PseudoPlaceholder = CSSPseudo(defined_name="::placeholder")
PseudoReadOnly = CSSPseudo(defined_name=":read-only")
PseudoReadWrite = CSSPseudo(defined_name=":read-write")
PseudoRequired = CSSPseudo(defined_name=":required")
PseudoRoot = CSSPseudo(defined_name=":root")
PseudoSelection = CSSPseudo(defined_name="::selection")
PseudoTarget = CSSPseudo(defined_name=":target")
PseudoValid = CSSPseudo(defined_name=":valid")
PseudoVisited = CSSPseudo(defined_name=":visited")

# ----------------------------------------------------------------------------------------------------------------------
A = CSSElement(defined_name="a")
Abbr = CSSElement(defined_name="abbr")
Acronym = CSSElement(defined_name="acronym")
Address = CSSElement(defined_name="address")
Applet = CSSElement(defined_name="applet")
Area = CSSElement(defined_name="area")
Article = CSSElement(defined_name="article")
Aside = CSSElement(defined_name="aside")
Audio = CSSElement(defined_name="audio")
B = CSSElement(defined_name="b")
Base = CSSElement(defined_name="base")
Basefont = CSSElement(defined_name="basefont")
Bdi = CSSElement(defined_name="bdi")
Bdo = CSSElement(defined_name="bdo")
Big = CSSElement(defined_name="big")
Blockquote = CSSElement(defined_name="blockquote")
Body = CSSElement(defined_name="body")
Br = CSSElement(defined_name="br")
Button = CSSElement(defined_name="button")
Canvas = CSSElement(defined_name="canvas")
Caption = CSSElement(defined_name="caption")
Center = CSSElement(defined_name="center")
Cite = CSSElement(defined_name="cite")
Code = CSSElement(defined_name="code")
Col = CSSElement(defined_name="col")
Colgroup = CSSElement(defined_name="colgroup")
Data = CSSElement(defined_name="data")
Datalist = CSSElement(defined_name="datalist")
Dd = CSSElement(defined_name="dd")
Del = CSSElement(defined_name="del")
Details = CSSElement(defined_name="details")
Dfn = CSSElement(defined_name="dfn")
Dialog = CSSElement(defined_name="dialog")
Dir = CSSElement(defined_name="dir")
Div = CSSElement(defined_name="div")
Dl = CSSElement(defined_name="dl")
Dt = CSSElement(defined_name="dt")
Em = CSSElement(defined_name="em")
Embed = CSSElement(defined_name="embed")
Fieldset = CSSElement(defined_name="fieldset")
Figcaption = CSSElement(defined_name="figcaption")
Figure = CSSElement(defined_name="figure")
Font = CSSElement(defined_name="font")
Footer = CSSElement(defined_name="footer")
Form = CSSElement(defined_name="form")
Frame = CSSElement(defined_name="frame")
Frameset = CSSElement(defined_name="frameset")
H1 = CSSElement(defined_name="h1")
H2 = CSSElement(defined_name="h2")
H3 = CSSElement(defined_name="h3")
H4 = CSSElement(defined_name="h4")
H5 = CSSElement(defined_name="h5")
H6 = CSSElement(defined_name="h6")
Head = CSSElement(defined_name="head")
Header = CSSElement(defined_name="header")
Hr = CSSElement(defined_name="hr")
Html = CSSElement(defined_name="html")
I = CSSElement(defined_name="i")
Iframe = CSSElement(defined_name="iframe")
Img = CSSElement(defined_name="img")
Input = CSSElement(defined_name="input")
Ins = CSSElement(defined_name="ins")
Kbd = CSSElement(defined_name="kbd")
Label = CSSElement(defined_name="label")
Legend = CSSElement(defined_name="legend")
Li = CSSElement(defined_name="li")
Link = CSSElement(defined_name="link")
Main = CSSElement(defined_name="main")
Map = CSSElement(defined_name="map")
Mark = CSSElement(defined_name="mark")
Meta = CSSElement(defined_name="meta")
Meter = CSSElement(defined_name="meter")
Nav = CSSElement(defined_name="nav")
Noframes = CSSElement(defined_name="noframes")
Noscript = CSSElement(defined_name="noscript")
Object = CSSElement(defined_name="object")
Ol = CSSElement(defined_name="ol")
Optgroup = CSSElement(defined_name="optgroup")
Option = CSSElement(defined_name="option")
Output = CSSElement(defined_name="output")
P = CSSElement(defined_name="p")
Param = CSSElement(defined_name="param")
Picture = CSSElement(defined_name="picture")
Pre = CSSElement(defined_name="pre")
Progress = CSSElement(defined_name="progress")
Q = CSSElement(defined_name="q")
Rp = CSSElement(defined_name="rp")
Rt = CSSElement(defined_name="rt")
Ruby = CSSElement(defined_name="ruby")
S = CSSElement(defined_name="s")
Samp = CSSElement(defined_name="samp")
Script = CSSElement(defined_name="script")
Section = CSSElement(defined_name="section")
Select = CSSElement(defined_name="select")
Small = CSSElement(defined_name="small")
Source = CSSElement(defined_name="source")
Span = CSSElement(defined_name="span")
Strike = CSSElement(defined_name="strike")
Strong = CSSElement(defined_name="strong")
Style = CSSElement(defined_name="style")
Sub = CSSElement(defined_name="sub")
Summary = CSSElement(defined_name="summary")
Sup = CSSElement(defined_name="sup")
Svg = CSSElement(defined_name="svg")
Table = CSSElement(defined_name="table")
Tbody = CSSElement(defined_name="tbody")
Td = CSSElement(defined_name="td")
Template = CSSElement(defined_name="template")
Textarea = CSSElement(defined_name="textarea")
Tfoot = CSSElement(defined_name="tfoot")
Th = CSSElement(defined_name="th")
Thead = CSSElement(defined_name="thead")
Time = CSSElement(defined_name="time")
Title = CSSElement(defined_name="title")
Tr = CSSElement(defined_name="tr")
Track = CSSElement(defined_name="track")
Tt = CSSElement(defined_name="tt")
U = CSSElement(defined_name="u")
Ul = CSSElement(defined_name="ul")
Var = CSSElement(defined_name="var")
Video = CSSElement(defined_name="video")
Wbr = CSSElement(defined_name="wbr")