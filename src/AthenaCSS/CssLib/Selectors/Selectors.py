# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import abstractmethod, ABC
from dataclasses import dataclass

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Selector(ABC):
    @abstractmethod
    def print(self) -> str:...

@dataclass
class Selector_Element(Selector):
    name:str
    def print(self) -> str:
        return self.name