# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, unsafe_hash=True)
class CSSComment:
    comment:str
# ----------------------------------------------------------------------------------------------------------------------
class CSSEmptyLine:pass
CSSEmptyLine = CSSEmptyLine
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class CSSCommentSeparator:
    length:int=64