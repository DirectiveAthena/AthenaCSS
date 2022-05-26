# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Content.CSSContent import CSSContent
from AthenaCSS.Library.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class CSSCommentSeparator(CSSContent):
    length:int=64

    def to_string(self) -> str:
        return f"/*{'-'*self.length}*/"

    def to_console(self, console_color_guide:ConsoleColorGuide) -> str:
        return console_color_guide.comment(self.to_string())