# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True,slots=True)
class CSSRuleManager:
    # Manager settings
    allow_duplicate: bool = field(default=False)  # Manager will not allow for duplicate parts within them

    # Actual attributes
    content: Iterable = field(init=False)

    def __post_init__(self):
        if self.allow_duplicate:
            self.content = list()
        else:
            self.content = set()

    # ------------------------------------------------------------------------------------------------------------------
    # - Content manipulations -
    # ------------------------------------------------------------------------------------------------------------------
    def _add_to_content(self, value):
        if isinstance(self.content, list):
            self.content.append(value)
        elif isinstance(self.content, set):
            self.content.add(value)
        else:
            raise SystemError
