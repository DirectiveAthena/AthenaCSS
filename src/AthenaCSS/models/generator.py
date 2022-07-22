# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages

# Custom Library
import AthenaLib.HTML.models.html_library as HtmlLib
from AthenaLib.HTML.models.html import HTMLElement
from AthenaLib.HTML.models.css import CSSProperty, CSSRule, CSSSelection, CSSComment
from AthenaLib.HTML.data.css_selection_type import CSSSelectionType

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSGenerator:
    content:list[CSSRule|CSSComment]
    def __init__(self, *,content:list[CSSRule|CSSComment]=None):
        if content is None:
            content = []
        self.content = content

    # ------------------------------------------------------------------------------------------------------------------
    # - Additions to the content -
    # ------------------------------------------------------------------------------------------------------------------
    def add_rule(
            self,
            selections:tuple[CSSSelection,...]|CSSSelection,
            properties:tuple[CSSProperty,...]|CSSProperty
    ):
        self.content.append(CSSRule(selections,properties))
        return self

    def add_comment(self, text:str):
        self.content.append(CSSComment(text))
        return self

    # ------------------------------------------------------------------------------------------------------------------
    # - Output -
    # ------------------------------------------------------------------------------------------------------------------
    def _output_generator(self, *,indent:bool=True, indentation:int=4) -> str:
        for c in self.content:
            match c:
                case CSSRule():
                    yield c.to_text(indent=indent, indentation=indentation)
                case CSSComment() | _:
                    yield str(c)

    def to_text(self) -> str:
        return "\n".join(self._output_generator())
