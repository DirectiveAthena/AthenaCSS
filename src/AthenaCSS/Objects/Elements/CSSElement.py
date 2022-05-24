# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.Decorators.ClassMethods import return_self_classmethod as return_self
from AthenaCSS.Objects.Elements.CSSAttribute import CSSAttrubite

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSElement"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
AFTER="+"
DESCENDANT=" "
COMBINE=","
CHILD=">"
PRECEDING="~"

class CSSElement:
    prefix=None
    defined_name = None
    parts: list
    __slots__ = ["parts"]

    def __init__(self, *parts: str|CSSElement|CSSAttrubite):
        if self.defined_name is None:
            self.parts = []
        elif self.prefix is None:
            self.parts = [self.defined_name]
        else:
            self.parts = [self.prefix, self.defined_name]

        self.parts += (self._partPrep(p) for p in parts)

    def __str__(self) -> str:
        result_string = ""
        for e in self.parts:
            if isinstance(e, tuple):
                result_string += "".join(str(e_) for e_ in e)
            elif isinstance(e, CSSElement|CSSAttrubite):
                result_string += str(e)
            else:
                result_string += e
        return result_string

    # ------------------------------------------------------------------------------------------------------------------
    # - Support Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def _partPrep(self, part):
        if self.prefix is None:
            return part
        else:
            return self.prefix, part

    # ------------------------------------------------------------------------------------------------------------------
    # - Combinators -
    # ------------------------------------------------------------------------------------------------------------------
    @return_self
    def after(self, *parts):  # +
        for p in parts:
            self.parts.append(
                (AFTER, p) if len(self.parts) != 0 else p
            )

    @return_self
    def descendant(self, *parts):  #
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
