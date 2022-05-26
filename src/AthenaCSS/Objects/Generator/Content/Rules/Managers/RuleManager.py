# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True,slots=True)
class RuleManager:
    # Manager settings
    allow_duplicate: bool = field(default=False, repr=False, hash=False)  # Manager will not allow for duplicate parts within them

    # Actual attributes
    content: list|frozenset = field(init=False, hash=True, default_factory=list)

    # ------------------------------------------------------------------------------------------------------------------
    # - Content manipulations -
    # ------------------------------------------------------------------------------------------------------------------
    def _add_to_content(self, value):
        self.content.append(value)

    def convert_to_frozenset(self) -> frozenset:
        self.content = frozenset(self.content)
        return self.content