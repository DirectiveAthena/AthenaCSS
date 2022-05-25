# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable

# Custom Library
from AthenaColor import ForeNest, StyleNest

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
PRINTER_COLORS:dict[str:Callable] = {
    "comment": ForeNest.SeaGreen,
    "text": ForeNest.SlateGray,
    "selector": ForeNest.PaleGoldenRod,
    "line": StyleNest.NoForeground
}