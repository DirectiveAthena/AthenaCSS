# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Library.Support import (FOLLOWING, DESCENDANT, COMBINE, CHILD, PRECEDING)
from AthenaCSS.Objects.ElementSelection.CSSId import CSSId
from AthenaCSS.Objects.ElementSelection.CSSElement import CSSElement
from AthenaCSS.Objects.ElementSelection.CSSClass import CSSClass
from AthenaCSS.Objects.ElementSelection.CSSPseudo import CSSPseudo
from AthenaCSS.Objects.ElementSelection.CSSAttribute import CSSAttribute

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSSelection"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
ELEMENTS = CSSId|CSSElement|CSSClass|CSSPseudo|CSSAttribute

def locked(fnc):
    def wrapper(self:CSSSelectionManager, *args, **kwargs):
        if self._lock:
            raise PermissionError("Manager is locked")
        return fnc(self, *args,**kwargs)
    return wrapper

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True)
class CSSSelectionPart:
    elements:tuple
    part_type:str=field(default="")

# ----------------------------------------------------------------------------------------------------------------------
class CSSSelectionManager:
    parts:list[CSSSelectionPart]
    _lock:bool
    __slots__ = ["parts", "_lock"]

    def __init__(self):
        self.parts = []
        self._lock = False

    @locked
    def add(self, *elements:ELEMENTS):
        self.parts.append(CSSSelectionPart(
            elements=elements
        ))

    @locked
    def add_descendants(self, *elements:ELEMENTS):
        self.parts.append(CSSSelectionPart(
            elements=elements,
            part_type=DESCENDANT
        ))

    @locked
    def add_following(self, *elements:ELEMENTS):
        self.parts.append(CSSSelectionPart(
            elements=elements,
            part_type=FOLLOWING
        ))

    @locked
    def add_childeren(self, *elements:ELEMENTS):
        self.parts.append(CSSSelectionPart(
            elements=elements,
            part_type=CHILD
        ))

    @locked
    def add_preceding(self, *elements:ELEMENTS):
        self.parts.append(CSSSelectionPart(
            elements=elements,
            part_type=PRECEDING
        ))

# ----------------------------------------------------------------------------------------------------------------------
class CSSSelection:
    __slots__ = ["_manager"]
    def __init__(self):
        self._manager = None

    # ------------------------------------------------------------------------------------------------------------------
    # - Support Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def _create_manager(self) -> CSSSelectionManager:
        if self._manager is None:
            self._manager = CSSSelectionManager()
        return self._manager

    # ------------------------------------------------------------------------------------------------------------------
    # - Properties -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def manager(self):
        # if the manager is not set yet, it will be created
        return self._create_manager()
    @property
    def parts(self) -> list[CSSSelectionPart|CSSSelection]:
        return self.manager.parts

    # ------------------------------------------------------------------------------------------------------------------
    # - Dunders -
    # ------------------------------------------------------------------------------------------------------------------
    def __str__(self) -> str:
        temp_list = []
        for part in self.parts:
            match part:
                case CSSSelection():
                    temp_list.extend(p.part_type.join(str(e) for e in p.elements) for p in part.parts)
                case CSSSelectionPart():
                    temp_list.append(part.part_type.join(str(e) for e in part.elements))
                case _:
                    raise TypeError

        return COMBINE.join(temp_list)

    def __enter__(self):
        # Create a manager to be used to control the selection structure
        return self.manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.manager._lock = True # Lock the manager to not accept any changes