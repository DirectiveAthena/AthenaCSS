# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Callable, NamedTuple

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class PrinterColors(NamedTuple):
    comment: Callable
    property_name:Callable
    property_value:Callable
    text: Callable
    selector: Callable
    line: Callable
    empty:Callable