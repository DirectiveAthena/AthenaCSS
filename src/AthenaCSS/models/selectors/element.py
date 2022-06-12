# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import itertools
from dataclasses import dataclass, field
from typing import Any

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
__all__=[
    "CSSElement"
]

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, unsafe_hash=True)
class CSSElement:
    parts:Any=field(default_factory=list)
    defined_name:str=field(kw_only=True, default=None)

    def __str__(self) -> str:
        # spread out for a bit better readability
        return ''.join(
            str(p)
            for p in itertools.chain((self.defined_name,), self.parts)  # if parts is empty, then it is simply ignored
            if p is not None
        )

    # noinspection PyArgumentList
    def __call__(self, *parts):
        # dissassemble the parts into it's bare stuff and then combine it together
        parts_ = []
        for p in parts:
            if type(p) is type(self):
                parts_.extend(p.parts)
            else:
                parts_.append(p)

        if self.parts is not None and parts_ is not None:
            return self.__class__((*self.parts,*parts_), defined_name=self.defined_name)
        elif self.parts is None and parts_ is not None:
            return self.__class__(*parts_, defined_name=self.defined_name)
        elif self.parts is not None and parts_ is None:
            return self.__class__(*self.parts, defined_name=self.defined_name)
        else:
            return self.__class__(defined_name=self.defined_name)