# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .Selectors import Selector
from .CSSselectors import *

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Selector_Combination(Selector):
    selectors:list
    def __init__(self, *selectors: Selector|type[Selector]):
        if not all(isinstance(s, Selector) or issubclass(s,Selector) for s in selectors):
            raise TypeError
        self.selectors = list(selectors)

    def print(self) -> str:
        return "".join(
            s.print() if isinstance(s, Selector) else s.name
            for s in self.selectors)
