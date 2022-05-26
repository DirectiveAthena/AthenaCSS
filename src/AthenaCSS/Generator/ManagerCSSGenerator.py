# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Generator.CSSGeneratorContent import (
    CSSComment, CSSRule, CSSEmptyLine,CSSCommentSeparator
)

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(kw_only=True,slots=True)
class ManagerGenerator:
    content: list = field(init=False, default_factory=list)
    # ------------------------------------------------------------------------------------------------------------------
    # - Types of content additions -
    # ------------------------------------------------------------------------------------------------------------------
    def add_rule(self, *rules:CSSRule) -> ManagerGenerator:
        for rule in rules:
            if not isinstance(rule, CSSRule):
                raise TypeError
            self.content.append(rule)
        return self

    def add_comment(self, comment:str|CSSComment) -> ManagerGenerator:
        if isinstance(comment, str):
            comment = CSSComment(comment=comment)
        elif not isinstance(comment, CSSComment):
            raise TypeError

        self.content.append(comment)
        return self

    def add_emptyline(self) -> ManagerGenerator:
        self.content.append(CSSEmptyLine)
        return self

    def add_comment_separator(self, separator_length:int=64) -> ManagerGenerator:
        self.content.append(CSSCommentSeparator(separator_length))
        return self