# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSAttribute"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSAttribute:
    """
    A special class to be used for all CSS attribute selectors.
    This is done because these type selectors can a name by itself, or also combined with a specific value
    """
    value:Any
    name:str
    selection_operator:str

    __slots__ = ["value", "name", "selection_operator"]

    def __init__(self, name:str, value:Any=None,*, selection_operator:str="="):
        self.name = name
        self.value = value
        self.selection_operator = selection_operator

    def __str__(self):
        if self.value is None:
            return f"[{self.name}]"
        return f"[{self.name}{self.selection_operator}{self.value}]"

    @classmethod
    def equals(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value)

    @classmethod
    def contains_word(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value,selection_operator="~=")

    @classmethod
    def starting_equal(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value,selection_operator="|=")

    @classmethod
    def begins_with(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value,selection_operator="^=")

    @classmethod
    def ends_with(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value,selection_operator="$=")

    @classmethod
    def contains_substring(cls, name:str, value:Any) -> CSSAttribute:
        return cls(name,value,selection_operator="*=")

    def __call__(self, name:str, value:Any=None,):
        return self.__class__(name, value, selection_operator=self.selection_operator)