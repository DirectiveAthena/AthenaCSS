# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaCSS.Library.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSContent(ABC):
    @abstractmethod
    def to_string(self) -> str:...

    @abstractmethod
    def to_console(self, console_color_guide:ConsoleColorGuide) -> str:...