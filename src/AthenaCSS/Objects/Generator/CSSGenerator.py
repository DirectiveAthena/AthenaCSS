# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Managers.ManagerGenerator import ManagerGenerator
from AthenaCSS.Library.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class CSSGenerator:
    content: ManagerGenerator.content=field(init=False)
    console_color_guide:ConsoleColorGuide=field(default_factory=lambda : ConsoleColorGuide())

    # Manager
    _manager:ManagerGenerator=field(default=None, repr=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Enter / Exit - (aka, the with statement)
    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self) -> ManagerGenerator:
        self._manager = ManagerGenerator()
        return self._manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.content = self._manager.content

    # ------------------------------------------------------------------------------------------------------------------
    # - String Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def to_string(self) -> str:
        return '\n'.join(content.to_string() for content in self.content)

    def to_console(self) :
        for content in self.content:
            print(content.to_console(self.console_color_guide))

    def to_file(self, filepath:str):
        with open(filepath, "w+") as file:
            for content in self.content:
                file.write(
                    f"{content.to_string()}"
                )