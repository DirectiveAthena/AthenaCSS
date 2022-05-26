# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Content.CSSContent import CSSContent
from AthenaCSS.Library.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSEmptyLine(CSSContent):
    def to_string(self) -> str:
        return "\n"

    def to_console(self, console_color_guide: ConsoleColorGuide) -> str:
        return "\n"