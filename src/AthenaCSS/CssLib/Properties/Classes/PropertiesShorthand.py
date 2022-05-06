# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from .CSSproperty import CSSproperty
from .Properties import CSSpropertySingle, CSSpropertyMulti

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSpropertyShorthand(CSSproperty):
    printer_order:list=None # to make sure everything is orderd as it should be
    important:bool

    def __init__(self,*args,important:bool=False, **values):
        # currently *args is not used

        # Inherited classes must have the named attributes set to the type of the to be made attribute
        for k,v in values.items():
            # relies on the fact that Shorthand Properties have their correct attributes set to the mapping CSSproperties
            if isinstance(v, self.__getattribute__(k)):
                self.__setattr__(k, v)
            elif k in self.printer_order:
                self.__setattr__(k, self.__getattribute__(k)(v))
            else:
                raise ValueError
        self.important = important

    def printer_value(self) -> str:
        if self.printer_order is None:
            return " ".join(*(
                str(p.printer_value())
                for p in dir(self)
                if isinstance(p, CSSpropertySingle)
            ))
        elif isinstance(self.printer_order, list | tuple):
            return " ".join(
                str(self.__getattribute__(p).printer_value())
                for p in self.printer_order
                if isinstance(self.__getattribute__(p), CSSpropertySingle)
            )
        # else:
        raise TypeError(self.printer_order)

    def printer_name(self) -> str:
        return str(type(self).__name__).replace('_', '-')

    def print(self) -> str:
        if self.important:
            return f"{self.printer_name()}: {self.printer_value()} !important"
        return f"{self.printer_name()}: {self.printer_value()}"


