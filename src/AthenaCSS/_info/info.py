# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
import AthenaLib._info.formatting as f
from AthenaCSS._info._v import _version

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def info(*, to_str: bool = False) -> None | str:
    line = "-" * 128
    header = f.header(f"""{line}
{f.title("AthenaCSS", to_str)} v{_version()}
is made by Andreas Sas and is a CSS generator for Python.
{line}
""", to_str)

    body = f"""
Package setup:
    {f.sub_modules("models", to_str)} : Basic classes which are meant to hold data. 
        These sort of classes are not meant to house a lot methods which interact with lots of other classes

    {f.sub_modules("data", to_str)} : A collection of all premade CSS properties, HTML named elements (H1, p, ...)
        These data objects are instances of the models which are described in the module mentioned above
"""

    text = f"{header}{body}{line}"

    # export to console or string
    if to_str:
        return text
    else:
        print(text)