# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from dataclasses import dataclass
from typing import Any, Iterable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(init=False, repr=True, slots=True)
class CSSSelector:
    elements:tuple[Any]
    prefix:str
    separator:str

    def __init__(self, *elements, prefix="", separator=", "):
        self.elements = elements
        self.prefix = prefix
        self.separator = separator

    # ------------------------------------------------------------------------------------------------------------------
    # - Printer -
    # ------------------------------------------------------------------------------------------------------------------
    def printer(self) -> str:
        if isinstance(self.elements, str):
            return f"{self.prefix}{self.elements}"
        if isinstance(self.elements, Iterable):
            return self.separator.join(f"{self.prefix}{v}" for v in self.elements)
        else:
            raise TypeError

    def __str__(self) -> str:
        return self.printer()