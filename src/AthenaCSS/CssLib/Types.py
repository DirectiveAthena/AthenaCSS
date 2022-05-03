# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class ValueType(ABC):
    @abstractmethod
    def __str__(self):...

@dataclass
class Second(ValueType):
    value:int

    def __str__(self):
        return f"{str(self.value)}s"

@dataclass
class MilliSecond(ValueType):
    value:int

    def __str__(self):
        return f"{str(self.value)}ms"