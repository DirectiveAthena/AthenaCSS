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
from AthenaCSS.Library.Support import INITIALINHERIT

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class LogicComponent:
    types:Any=field(default=None)
    specific:Any=field(default=None)

    allow_all:bool=field(kw_only=True,default=False)

def LogicAssembly(value_choice:dict) -> list[LogicComponent]:
    LogicList = []
    for key, value in value_choice.items():
        match key, value:
            case key, _  if key is Any:
                component = LogicComponent(allow_all=True)
            case _, value if value is Any:
                component = LogicComponent(key, Any)

            case _:
                component = LogicComponent(key, value)

        LogicList.append(component)

    return LogicList

def LogicEmpty() -> list:
    return [LogicComponent(allow_all=True)]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class ValueLogic:
    _value:Any=field(init=False)
    value_choice:list|dict=field(default_factory=LogicEmpty)
    default:Any=None
    printer_space:str=" "

    def __post_init__(self):
        # Because of old code that I don't want to rewrite,
        #   the old dictionary is replaced into the new format
        if isinstance(self.value_choice, dict):
            self.value_choice = LogicAssembly(self.value_choice)

    def validate_value(self, value) -> Exception | None:
        # catch for the widly used initial or inherit value, which is possible at every property
        if value in INITIALINHERIT:
            return None

        value_type = type(value) if not isinstance(value, tuple) else tuple(type(v) for v in value)

        for logic in self.value_choice:
            match logic:
                case LogicComponent(allow_all=True):
                    return
                case LogicComponent(types=value_type(), specific=specific) if specific is Any:
                    return
                case LogicComponent(types=value_type(),specific=specific) if isinstance(specific, tuple) and isinstance(value, tuple):
                    if all(v in s for v, s in zip(value, specific)):
                        return
                    else:
                        return ValueError(value, self.value_choice)
                case LogicComponent(types=value_type(),specific=specific) if isinstance(specific, object) and value in specific:
                    return
                case _:
                    return TypeError(value, self.value_choice)

    # ------------------------------------------------------------------------------------------------------------------
    # - Value -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if (error := self.validate_value(value)) is None:
            self._value = value
        else:
            raise error

    @value.deleter
    def value(self):
        self._value = copy.copy(self.default)

    # ------------------------------------------------------------------------------------------------------------------
    # - Generator -
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
