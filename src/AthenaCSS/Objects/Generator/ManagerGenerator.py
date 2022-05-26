# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.Generator.Content import (
    CSSComment, CSSRule, CSSEmptyLine,CSSCommentSeparator
)

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
CONTENT = CSSRule|CSSComment|CSSEmptyLine|CSSCommentSeparator

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class ManagerGenerator:
    content:list[CONTENT]=field(default_factory=list)

    # ------------------------------------------------------------------------------------------------------------------
    # - Content manipulations -
    # ------------------------------------------------------------------------------------------------------------------
    def _add_to_content(self, value):
        self.content.append(value)

    # ------------------------------------------------------------------------------------------------------------------
    # - Types of content additions -
    # ------------------------------------------------------------------------------------------------------------------
    def add_rule(self, *rules:CSSRule) -> ManagerGenerator:
        for rule in rules:
            self._add_to_content(rule)
        return self

    def add_comment(self, comment:str|CSSComment) -> ManagerGenerator:
        if isinstance(comment, str):
            comment = CSSComment(comment=comment)
        elif not isinstance(comment, CSSComment):
            raise TypeError

        self._add_to_content(comment)
        return self

    def add_emptyline(self) -> ManagerGenerator:
        self._add_to_content(CSSEmptyLine)
        return self

    def add_comment_separator(self, separator_length:int=64) -> ManagerGenerator:
        self._add_to_content(CSSCommentSeparator(separator_length))
        return self