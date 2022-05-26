# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
from typing import Callable

# Custom Library
from AthenaColor import ForeNest

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class ConsoleColorGuide:
    selector:Callable = ForeNest.GoldenRod

    descriptor_name:Callable = ForeNest.RoyalBlue
    descriptor_value:Callable = ForeNest.White

    text_general:Callable = ForeNest.SlateGray

    comment:Callable = ForeNest.SpringGreen
