# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
from dataclasses import dataclass, field

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
@dataclass(slots=True, unsafe_hash=True)
class CSSAttribute:
    """
    A special class to be used for all CSS attribute selectors.
    This is done because these type selectors can a name by itself, or also combined with a specific value
    """
    value:Any
    name:str
    selection_operator:str=field(kw_only=True, default=None)

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

    # noinspection PyArgumentList
    def __call__(self, name:str, value:Any=None,):
        return self.__class__(name, value, selection_operator=self.selection_operator)