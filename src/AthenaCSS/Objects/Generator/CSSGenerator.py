# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.ManagerGenerator import ManagerGenerator
from AthenaCSS.Objects.Generator.Content import (
    CSSComment, CSSRule, CSSEmptyLine,CSSCommentSeparator
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class CSSGenerator:
    content: ManagerGenerator.content=field(init=False)

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
    # - Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def to_console(self):
        for content in self.content:
            match content:
                case CSSRule():
                    selectors =  ",".join(group.group_type.value.join(str(e) for e in group.elements) for group in content.selectors)
                    declarations = ";".join(str(d) for d in content.declarations)
                    print(
                        f"{selectors}{{{declarations};}}"
                    )
                case CSSComment():
                    print(f"/*{content.comment}*/")
                case CSSEmptyLine():
                    print()
                case CSSCommentSeparator():
                    print("-"*content.length)