# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from typing import Any
import copy
from dataclasses import dataclass, field

# Custom Library
from AthenaColor import RGB, RGBA, HEX, HEXA, HSL, HSV

# Custom Packages
from AthenaCSS.data.support import INITIALINHERIT

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class LogicComponent:
    types:Any
    specific:Any

def LogicAssembly(value_choice:dict) -> list[LogicComponent]:
    LogicList = []
    for key, value in value_choice.items():
        match key, value:
            case key, _  if key is Any:
                LogicList = [Any]
                break # can break here as Any catches all
            case _, value if value is Any:
                LogicList.append(LogicComponent(key, Any))
            case _, value if value is None:
                LogicList.append(None)
            case _:
                LogicList.append(LogicComponent(key, value))

    return LogicList

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class ValueLogic:
    _value:Any=field(init=False)
    value_choice:list|dict=field(default_factory=lambda:[Any])
    default:Any=None
    printer_space:str=" "

    def __post_init__(self):
        # Because of old code that I don't want to rewrite,
        #   the old dictionary is replaced into the new format
        if isinstance(self.value_choice, dict):
            self.value_choice = LogicAssembly(self.value_choice)

    def validate_value(self, value):
        # catch for the widely used initial or inherit value, which is possible at every property
        #   or there is an "all is allowed" in the choices
        if (value in INITIALINHERIT or Any in self.value_choice) \
        or (value is None and None in self.value_choice):
            return

        value_type = type(value) if not isinstance(value, tuple|list|set|frozenset) else tuple(type(v) for v in value)

        for logic in self.value_choice:
            match logic:
                case LogicComponent(types=vt,specific=specific) if vt == value_type:
                    if specific in (Any, None):
                        break
                    elif isinstance(specific, tuple|list|set|frozenset) and isinstance(value, tuple):
                        for v,s in zip(value, specific):
                            if s not in (Any, None) and v not in s:
                                raise ValueError(value, self.value_choice)
                        break
                    elif isinstance(specific, tuple|list|set|frozenset) and value in specific:
                        break
                    elif isinstance(specific, object) and value == specific:
                        break
        else:
            raise TypeError(value, value_type, self.value_choice)

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, value):
        self.validate_value(value)
        self._value = value

    @value.deleter
    def value(self):
        self._value = copy.copy(self.default)

    # ------------------------------------------------------------------------------------------------------------------
    # - generator -
    # ------------------------------------------------------------------------------------------------------------------
    def printer(self) -> str:
        match self.value:
            case None:
                return "none"
            case RGB()|RGBA()|HEX()|HEXA()|HSL()|HSV():
                return f"{type(self.value).__name__.lower()}{self.value.export()}"
            case tuple(value):
                return self.printer_space.join(str(v) for v in value)
            case value: # catches all
                return str(value)

    def __str__(self) -> str:
        return self.printer()
