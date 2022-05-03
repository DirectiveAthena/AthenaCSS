# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass,field
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

@dataclass
class CubicBezier(ValueType):
    x1:float=field(default=0)
    y1:float=field(default=0)
    x2:float=field(default=0)
    y2:float=field(default=0)

    def __post_init__(self):
        self.x1 = max(min(self.x1, 1.0),0.0)
        self.y1 = max(min(self.y1, 1.0),0.0)
        self.x2 = max(min(self.x2, 1.0),0.0)
        self.y2 = max(min(self.y2, 1.0),0.0)

    def __str__(self):
        return f"cubic-bezier({self.x1}, {self.y1}, {self.x2}, {self.y2})"