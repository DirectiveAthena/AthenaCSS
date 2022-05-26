# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import NamedTuple, Any
from enum import Enum, auto

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.ManagerGenerator import ManagerGenerator
from AthenaCSS.Objects.Generator.Content import (
    CSSComment, CSSRule, CSSEmptyLine,CSSCommentSeparator
)
from AthenaCSS.Objects.Generator.Content.Rules.Managers.ManagerSelectors import SelectorGroup

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class ContentYieldType(Enum):
    comment = auto
    selector_group = auto
    selector_group_final = auto
    declaration_start = auto
    declaration_end =auto
    declaration = auto
    empty_line = auto
    comment_separator = auto

class ContentYield(NamedTuple):
    content:Any
    type:ContentYieldType

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