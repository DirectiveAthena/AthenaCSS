# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaCSS.Library.SelectorElementLibrary as ElementLib
from AthenaCSS.Objects.Elements.CSSAttribute import CSSAttribute
from AthenaCSS.Objects.Elements.CSSClass import CSSClass
from AthenaCSS.Objects.Elements.CSSId import CSSId
from AthenaCSS.Objects.Rule.CSSRule import CSSRule

# Custom Packages
from BulkTests import BulkTests

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------

class CSSSelectors(BulkTests):
    def test_CSSRule0(self):
        rule = CSSRule()
        with rule as (selector,declaration):
            print(selector,declaration)
