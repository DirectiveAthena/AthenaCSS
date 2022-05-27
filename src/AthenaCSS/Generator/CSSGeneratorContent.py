# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Library.Support import NEW_LINE

from AthenaCSS.Generator.ManagerCSSRule import ManagerSelectors, ManagerDeclarations
from AthenaCSS.Generator.ConsoleColorGuide import ConsoleColorGuide


# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSRule", "CSSComment", "CSSCommentSeparator", "CSSEmptyLine"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
class _Content(ABC):
    @abstractmethod
    def to_string(self, **kwargs) -> str:...
    @abstractmethod
    def to_console(self, **kwargs) -> str:...

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, unsafe_hash=True)
class CSSComment(_Content):
    comment:str

    def to_string(self, **kwargs) -> str:
        return f"/*{self.comment}*/"

    def to_console(self, console_color_guide:ConsoleColorGuide, **kwargs) -> str:
        return console_color_guide.comment(self.to_string())
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class CSSCommentSeparator(_Content):
    length:int=64

    def to_string(self, **kwargs) -> str:
        return f"/*{'-'*self.length}*/"

    def to_console(self, console_color_guide:ConsoleColorGuide, **kwargs) -> str:
        return console_color_guide.comment(self.to_string())

# ----------------------------------------------------------------------------------------------------------------------
class CSSEmptyLine(_Content):
    def to_string(self, **kwargs) -> str:
        return NEW_LINE

    def to_console(self, one_line: bool, **kwargs) -> str:
        return NEW_LINE if one_line else " "
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True, unsafe_hash=True)
class CSSRule(_Content):
    selectors:list=field(init=False, hash=True)
    declarations:list=field(init=False, hash=True)

    # Manager Options
    manager_overwrite:bool=field(default=False, repr=False, hash=False) # If the rule is entered twice, it will create new managers every time (resulting in the previous managers being lost)

    # Managers
    _selector_manager:ManagerSelectors=field(default=None, repr=False, hash=False)
    _declaration_manager:ManagerDeclarations=field(default=None, repr=False, hash=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Enter / Exit - (aka, the with statement)
    # ------------------------------------------------------------------------------------------------------------------
    def _define_managers(self):
        self._selector_manager = ManagerSelectors()
        self._declaration_manager = ManagerDeclarations()

    def __enter__(self) -> tuple[ManagerSelectors, ManagerDeclarations]:
        if None in {self._selector_manager, self._declaration_manager} or self.manager_overwrite:
           self._define_managers()

        return self._selector_manager, self._declaration_manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.selectors = self._selector_manager.content
        self.declarations = self._declaration_manager.content

    # ------------------------------------------------------------------------------------------------------------------
    # - String Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def _selectors_generator(self):
        for selector_group in self.selectors:
            yield selector_group.group_type.value.join(str(el)for el in selector_group.selectors)

    def _declaration_generator(self) -> list[tuple[str,str]]:
        for declaration in self.declarations:
            yield declaration.name_printer(), declaration.value_printer()

    def to_string(self, /,indentation:int, one_line:bool, **kwargs) -> str:
        new_line = NEW_LINE if not one_line else ' '

        declarations_full = new_line.join(
            f"{' ' * indentation}{name}: {value};"
            for name,value in self._declaration_generator()
        )
        # if one_line is set to True, then the "new_line" block below will only print out a space
        return f"{f',{new_line}'.join(self._selectors_generator())}{{{new_line}{declarations_full}{new_line}}}"

    def to_console(self, /,console_color_guide:ConsoleColorGuide, one_line:bool, indentation:int, **kwargs) -> str:
        new_line = NEW_LINE if not one_line else ' '

        selectors_full = console_color_guide.text_general(f',{new_line}').join(
            console_color_guide.selector(selector)
            for selector in self._selectors_generator()
        )

        declarations_full = console_color_guide.text_general(new_line).join(
            f"{' ' * indentation}{console_color_guide.descriptor_name(name)}: {console_color_guide.descriptor_value(value)};"
            for name, value in self._declaration_generator()
        )

        # if one_line is set to True, then the "new_line" block below will only print out a space
        return f"{selectors_full}{{{new_line}{declarations_full}{new_line}}}"