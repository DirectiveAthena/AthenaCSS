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
    def add_rule(self, *rules:CSSRule):
        for r in rules:
            if not isinstance(r, CSSRule):
                raise TypeError

            self._add_to_content(r)

    def add_comment(self, comment:str|CSSComment):
        if isinstance(comment, str):
            comment = CSSComment(comment=comment)
        elif not isinstance(comment, CSSComment):
            raise TypeError

        self._add_to_content(comment)

    def add_emptyline(self):
        self._add_to_content(CSSEmptyLine)

    def add_comment_separator(self, separator_length:int=64):
        self._add_to_content(CSSCommentSeparator(separator_length))

    def __iadd__(self, other:CONTENT):
        if not isinstance(other, CONTENT):
            raise TypeError

        self._add_to_content(other)