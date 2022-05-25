# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import NamedTuple, Callable

# Custom Library

# Custom Packages
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ContentStyling(NamedTuple):
    selection:CSSSelection
    styling: tuple[CSSProperty|CSSPropertyShorthand]
    comment: str

class ContentComment(NamedTuple):
    comment: str

class ContentLine(NamedTuple):
    pass

class ContentSeperation(NamedTuple):
    pass

class ContentYielder(NamedTuple):
    text:str
    console_styling:Callable
