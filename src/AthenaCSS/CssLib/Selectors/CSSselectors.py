# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from .Selectors import Selector, Selector_Element

# ----------------------------------------------------------------------------------------------------------------------
# - all -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "Selector_Class","Selector_Id","Selector_Element","Selector_Header1","Selector_Header2","Selector_Header3",
    "Selector_Header4","Selector_Header5","Selector_Header6"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass
class Selector_Class(Selector):
    name:str
    def print(self) -> str:
        return f".{self.name}"

@dataclass
class Selector_Id(Selector):
    name:str
    def print(self) -> str:
        return f"#{self.name}"

class Selector_Header1(Selector_Element):
    name="h1"
class Selector_Header2(Selector_Element):
    name="h2"
class Selector_Header3(Selector_Element):
    name="h3"
class Selector_Header4(Selector_Element):
    name="h4"
class Selector_Header5(Selector_Element):
    name="h5"
class Selector_Header6(Selector_Element):
    name="h6"
