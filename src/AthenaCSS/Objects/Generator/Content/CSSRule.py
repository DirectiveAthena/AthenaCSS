# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Managers.ManagerDeclarations import ManagerDeclarations
from AthenaCSS.Objects.Generator.Managers.ManagerSelectors import ManagerSelectors
from AthenaCSS.Objects.Generator.Content.CSSContent import CSSContent
from AthenaCSS.Library.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSRule"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True, unsafe_hash=True)
class CSSRule(CSSContent):
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
    def _to_string_assembler(self) -> tuple[list[str], list[tuple[str,str]]]:
        selectors = [
            selector_group.group_type.value.join(
                str(element)
                for element in selector_group.elements
            )
            for selector_group in self.selectors
        ]
        declarations = [
            (declaration.name_printer(), declaration.value_printer())
            for declaration in self.declarations
        ]
        return selectors, declarations

    def to_string(self) -> str:
        selectors, declarations = self._to_string_assembler()
        selectors_new_line = ",\n"
        declarations_new_line = "\n"
        indentation=4
        return (
f"""
{selectors_new_line.join(selectors)}{{
{declarations_new_line.join(
    f"{' ' * indentation}{name}: {value};" 
    for name,value in declarations
)}
}}
"""
        )

    def to_console(self, console_color_guide:ConsoleColorGuide) -> str:
        selectors, declarations = self._to_string_assembler()
        selectors_new_line = console_color_guide.text_general(",\n")
        declarations_new_line = console_color_guide.text_general("\n")
        indentation = 4
        return (
f"""
{selectors_new_line.join(console_color_guide.selector(selector) for selector in selectors)}{{
{declarations_new_line.join(
    f"{' ' * indentation}{console_color_guide.descriptor_name(name)}: {console_color_guide.descriptor_value(value)};" 
    for name, value in declarations
)}
}}
"""
        )