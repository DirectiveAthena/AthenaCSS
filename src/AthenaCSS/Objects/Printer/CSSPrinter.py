# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from collections import namedtuple

# Custom Library

# Custom Packages
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Library.Support import locked

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand
Content_Styling = namedtuple("Content_Styling", ["Selection", "Styling", "Comment"])
Content_Comment = namedtuple("Content_Comment", ["Comment"])
Content_Line = namedtuple("Content_Line", [])
Content_Seperation = namedtuple("Content_Seperation", [])

CONTENT = Content_Comment | Content_Styling | Content_Line | Content_Seperation

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class CSSPrinterManager:
    content: list[CONTENT]
    _lock:bool
    __slots__ = ["content", "_lock"]

    def __init__(self):
        self.content = []
        self._lock = False

    # ------------------------------------------------------------------------------------------------------------------
    # - Population Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @locked
    def add_style(self, selection:CSSSelection, styling:tuple[PROPERTIES],*,comment:str=None):
        if not isinstance(selection, CSSSelection):
            raise TypeError
        if not all(isinstance(s, PROPERTIES) for s in styling):
            raise TypeError
        if comment is not None and not isinstance(comment, str):
            raise TypeError
        self.content.append(Content_Styling(selection, styling, comment))

    @locked
    def add_comment(self, comment:str):
        if comment is not None and not isinstance(comment, str):
            raise TypeError
        self.content.append(Content_Comment(comment))

    @locked
    def add_seperation(self):
        self.content.append(Content_Seperation())

    @locked
    def add_line(self):
        self.content.append(Content_Line())


# ----------------------------------------------------------------------------------------------------------------------
class CSSPrinter:
    _indentation:int # thanks to Twidi for showing me my typo
    _one_line:bool
    _seperation_character:str
    _seperation_length:int
    _comments:bool
    __slots__ = ["_indentation", "_one_line", "_manager", "_seperation_character", "_seperation_length", "_comments"]

    def __init__(self,
                 *,
                 indentation:int=4,
                 one_line=False,
                 seperation_character="-",
                 seperation_length=255,
                 comments=True
                 ):
        self._manager = None

        self.indentation = indentation
        self.one_line = one_line
        self.seperation_character = seperation_character
        self.seperation_length = seperation_length
        self.comments = comments

    def __enter__(self):
        return self.manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._manager._lock = True

    # ------------------------------------------------------------------------------------------------------------------
    # - Support Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def _create_manager(self) -> CSSPrinterManager:
        if self._manager is None:
            self._manager = CSSPrinterManager()
        return self._manager

    def _format_comment(self, comment:str):
        if self.one_line:
            new_line = '\n'
            return f"/*{comment.replace(new_line, ' ')}*/"
        else:
            return "\n".join(f"/*{c}*/" for c in comment.split("\n"))

    # ------------------------------------------------------------------------------------------------------------------
    # - Properties -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def manager(self):
        # if the manager is not set yet, it will be created
        return self._create_manager()
    @property
    def content(self) -> list:
        return self.manager.content

    @property
    def indentation(self) -> int:
        return self._indentation
    @indentation.setter
    def indentation(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._indentation = max(0,value)

    @property
    def one_line(self):
        return self._one_line
    @one_line.setter
    def one_line(self, value):
        if not isinstance(value, bool):
            raise TypeError
        self._one_line = value

    @property
    def seperation_character(self):
        return self._seperation_character
    @seperation_character.setter
    def seperation_character(self, value):
        if not isinstance(value, str):
            raise TypeError
        self._seperation_character = value

    @property
    def seperation_length(self) -> int:
        return self._seperation_length
    @seperation_length.setter
    def seperation_length(self, value):
        if not isinstance(value, int):
            raise TypeError
        self._seperation_length = max(0,value)

    @property
    def comments(self):
        return self._comments
    @comments.setter
    def comments(self, value):
        if not isinstance(value, bool):
            raise TypeError
        self._comments = value

    # ------------------------------------------------------------------------------------------------------------------
    # - Output Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def to_string(self):
        result = ""
        new_line = "" if self.one_line else "\n"
        indentation = "" if self.one_line  else (" " * self.indentation)

        for content in self.content:
            match content:
                # only print if comments are enabled
                case Content_Comment() if self.comments:
                    comment, = content
                    result += self._format_comment(comment) + new_line

                # only print if comments are enabled
                case Content_Seperation() if self.comments:
                    result += self._format_comment(self.seperation_character*self.seperation_length) + new_line

                case Content_Line():
                    result += new_line

                case Content_Styling():
                    selection, styling, comment = content
                    if comment is not None and self.comments:
                        result += self._format_comment(comment) + new_line
                    styling_string = new_line.join(f'{indentation}{s};' for s in styling)
                    result += f"{selection}{{{new_line}{styling_string}{new_line}}}{new_line * 2}"

                case _ if self.comments:
                    raise SyntaxError

        return result

    def to_console(self):
        pass

    def to_file(self):
        pass

