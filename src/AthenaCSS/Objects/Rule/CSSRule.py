# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Rule.Managers.CSSManagerDeclarations import CSSManagerDeclarations
from AthenaCSS.Objects.Rule.Managers.CSSManagerSelectors import CSSManagerSelectors

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSRule"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True, slots=True)
class CSSRule:
    selectors:Iterable=field(init=False)
    declarations:Iterable=field(init=False)

    # Manager Options
    manager_overwrite:bool=field(default=False) # If the rule is entered twice, it will create new managers every time (resulting in the previous managers being lost)
    manager_allow_duplicate:bool=field(default=False) # Managers will not allow for duplicate parts within them

    # Managers
    _selector_manager:CSSManagerSelectors=field(default=None)
    _declaration_manager:CSSManagerDeclarations=field(default=None)

    # ------------------------------------------------------------------------------------------------------------------
    # - Enter / Exit - (aka, the with statement)
    # ------------------------------------------------------------------------------------------------------------------
    def _define_managers(self):
        kw_args = {
            "allow_duplicate": self.manager_allow_duplicate
        }

        self._selector_manager = CSSManagerSelectors(**kw_args)
        self._declaration_manager = CSSManagerDeclarations(**kw_args)

    def __enter__(self) -> tuple[CSSManagerSelectors,CSSManagerDeclarations]:
        if None in {self._selector_manager, self._declaration_manager} or self.manager_overwrite:
           self._define_managers()

        return self._selector_manager, self._declaration_manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.selectors = self._selector_manager.content
        self.declarations = self._declaration_manager.content