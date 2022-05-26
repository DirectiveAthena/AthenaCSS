# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Iterable

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Content.Rules.Managers.ManagerDeclarations import ManagerDeclarations
from AthenaCSS.Objects.Generator.Content.Rules.Managers.ManagerSelectors import ManagerSelectors

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
class CSSRule:
    selectors:frozenset=field(init=False, hash=True)
    declarations:frozenset=field(init=False, hash=True)

    # Manager Options
    manager_overwrite:bool=field(default=False, repr=False, hash=False) # If the rule is entered twice, it will create new managers every time (resulting in the previous managers being lost)
    manager_allow_duplicate:bool=field(default=False, repr=False, hash=False) # Managers will not allow for duplicate parts within them

    # Managers
    _selector_manager:ManagerSelectors=field(default=None, repr=False, hash=False)
    _declaration_manager:ManagerDeclarations=field(default=None, repr=False, hash=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Enter / Exit - (aka, the with statement)
    # ------------------------------------------------------------------------------------------------------------------
    def _define_managers(self):
        kw_args = {
            "allow_duplicate": self.manager_allow_duplicate
        }

        self._selector_manager = ManagerSelectors(**kw_args)
        self._declaration_manager = ManagerDeclarations(**kw_args)

    def __enter__(self) -> tuple[ManagerSelectors, ManagerDeclarations]:
        if None in {self._selector_manager, self._declaration_manager} or self.manager_overwrite:
           self._define_managers()

        return self._selector_manager, self._declaration_manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.selectors = self._selector_manager.convert_to_frozenset()
        self.declarations = self._declaration_manager.convert_to_frozenset()