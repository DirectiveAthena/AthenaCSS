# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaLib.Decorators.ClassMethods import return_self_classmethod as return_self

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSSelection"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
AFTER="+"
DESCENDANT=" "
COMBINE=","
CHILD=">"
PRECEDING="~"


class CSSSelection:
    parts:list
    __slots__ = ["parts"]
    def __init__(self, *parts):
        self.parts = list(parts)

    def __str__(self) -> str:
        return ''.join(''.join(str(p_) for p_ in p) if isinstance(p, tuple) else str(p) for p in self.parts)

    # ------------------------------------------------------------------------------------------------------------------
    # - Combinators -
    # ------------------------------------------------------------------------------------------------------------------
    @return_self
    def combine(self, *parts):  # ''
        for p in parts:
            self.parts.append(
                (COMBINE, p) if len(self.parts) != 0 else p
            )

    @return_self
    def after(self, *parts):  # +
        for p in parts:
            self.parts.append(
                (AFTER, p) if len(self.parts) != 0 else p
            )

    @return_self
    def descendant(self, *parts):  # ' '
        for p in parts:
            self.parts.append(
                (DESCENDANT, p) if len(self.parts) != 0 else p
            )

    @return_self
    def child(self, *parts):  # >
        for p in parts:
            self.parts.append(
                (CHILD, p) if len(self.parts) != 0 else p
            )

    @return_self
    def preceding(self, *parts):  # ~
        for p in parts:
            self.parts.append(
                (PRECEDING, p) if len(self.parts) != 0 else p
            )
