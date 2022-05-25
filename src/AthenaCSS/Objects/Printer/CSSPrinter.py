# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from collections import namedtuple
from enum import Enum
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Library.Support import locked
from AthenaCSS.Library.PrinterColors import PRINTER_COLORS

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand
Content_Styling = namedtuple("Content_Styling", ["Selection", "Styling", "Comment"])
Content_Comment = namedtuple("Content_Comment", ["Comment"])
Content_Line = namedtuple("Content_Line", [])
Content_Seperation = namedtuple("Content_Seperation", [])

CONTENT = Content_Comment | Content_Styling | Content_Line | Content_Seperation

Content_Yielder = namedtuple("Content_Yielder", ["String", "StringType"])
class YIELD(Enum):
    COMMENT = "comment"
    SELECTOR = "selector"
    TEXT = "text"
    LINE = "line"

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
@dataclass(kw_only=True, eq=False, slots=True)
class CSSPrinter:
    indentation:int=field(default=4) # thanks to Twidi for showing me my typo
    one_line:bool=field(default=False)
    seperation_character:str=field(default="-")
    seperation_length:int=field(default=255)
    comments:bool=field(default=True)
    file_path:str=field(default=None)
    _manager:CSSPrinterManager=field(init=False, default=None)
    
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

    def _string_generator(self):
        new_line = "" if self.one_line else "\n"
        indentation = "" if self.one_line else (" " * self.indentation)

        for content in self.content:
            match content:
                # only print if comments are enabled
                case Content_Comment() if self.comments:
                    comment, = content
                    yield Content_Yielder(self._format_comment(comment) + new_line, YIELD.COMMENT)

                # only print if comments are enabled
                case Content_Seperation() if self.comments:
                    yield Content_Yielder(self._format_comment(self.seperation_character * self.seperation_length) + new_line, YIELD.COMMENT)

                case Content_Line():
                    yield Content_Yielder(new_line, YIELD.LINE)

                case Content_Styling():
                    selection, styling, comment = content
                    if comment is not None and self.comments:
                        yield Content_Yielder(self._format_comment(comment) + new_line, YIELD.COMMENT)
                    styling_string = new_line.join(f'{indentation}{s};' for s in styling)
                    # yield the Selectors
                    yield Content_Yielder(f"{selection}{{", YIELD.SELECTOR)
                    # yield the styling
                    yield Content_Yielder(f"{new_line}{styling_string}{new_line}", YIELD.TEXT)
                    # yield the closing of the selector
                    yield Content_Yielder(f"}}{new_line * 2}", YIELD.SELECTOR)


                case _ if self.comments:
                    raise SyntaxError

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

    # ------------------------------------------------------------------------------------------------------------------
    # - Output Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def to_string(self):
        return ''.join(s.String for s in self._string_generator())

    def to_console(self):
        for segement in self._string_generator():
            text, print_setup = segement
            print(PRINTER_COLORS[print_setup.value](text), end="")

    def to_file(self):
        if self.file_path is None:
            raise ValueError

        with open(self.file_path, "a") as file:
            for segement in self._string_generator():
                file.write(segement.String)

