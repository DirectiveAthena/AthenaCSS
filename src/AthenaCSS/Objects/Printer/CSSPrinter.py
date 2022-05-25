# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from collections import namedtuple
from enum import Enum
from dataclasses import dataclass, field
from typing import Iterable

# Custom Library
from AthenaColor import ForeNest, StyleNest

# Custom Packages
from AthenaCSS.Objects.ElementSelection.CSSSelection import CSSSelection
from AthenaCSS.Objects.Properties.CSSProperty import CSSProperty
from AthenaCSS.Objects.Properties.CSSPropertyShorthand import CSSPropertyShorthand
from AthenaCSS.Library.Support import locked
from AthenaCSS.Objects.Printer.PrinterColors import PrinterColors

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand
Content_Styling = namedtuple("Content_Styling", ["Selection", "Styling", "Comment"])
Content_Comment = namedtuple("Content_Comment", ["Comment"])
Content_Line = namedtuple("Content_Line", [])
Content_Seperation = namedtuple("Content_Seperation", [])

CONTENT = Content_Comment | Content_Styling | Content_Line | Content_Seperation

Content_Yielder = namedtuple("Content_Yielder", ["text", "console_styling"])

class YIELD(Enum):
    COMMENT = "comment"
    SELECTOR = "selector"
    TEXT = "text"
    LINE = "line"

PRINTER_COLORS = PrinterColors(
    comment=ForeNest.SeaGreen,
    property_name=ForeNest.CornFlowerBlue,
    property_value=ForeNest.White,
    text=ForeNest.SlateGray,
    selector=ForeNest.GoldenRod,
    line=StyleNest.NoForeground,
    empty=StyleNest.NoForeground
)

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
    indentation:int=4 # thanks to Twidi for showing me my typo, and showing me that field is not needed for default
    one_line:bool=False
    seperation_character:str="-"
    seperation_length:int=64
    comments:bool=True
    file_overwrite:bool=True
    console_printer_colors:PrinterColors=PRINTER_COLORS

    # Not needed on init
    _manager:CSSPrinterManager=field(init=False, default=None)

    def __enter__(self):
        return self.manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._manager._lock = True

    # ------------------------------------------------------------------------------------------------------------------
    # - Support Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def _format_comment(self, comment:str):
        if self.one_line:
            new_line = '\n'
            return f"/*{comment.replace(new_line, ' ')}*/"
        else:
            return "\n".join(f"/*{c}*/" for c in comment.split("\n"))

    def _string_generator(self):
        new_line = "" if self.one_line else "\n"
        indentation = "" if self.one_line else (" " * self.indentation)

        for content in self.manager.content:
            match content:
                # only print if comments are enabled
                case Content_Comment() if self.comments:
                    yield Content_Yielder(
                        self._format_comment(content.comment) + new_line,
                        self.console_printer_colors.comment
                    )

                # only print if comments are enabled
                case Content_Seperation() if self.comments:
                    yield Content_Yielder(
                        self._format_comment(self.seperation_character * self.seperation_length) + new_line,
                        self.console_printer_colors.comment
                    )

                case Content_Line():
                    yield Content_Yielder(
                        new_line,
                        self.console_printer_colors.line
                    )

                case Content_Styling():
                    if content.comment is not None and self.comments:
                        yield Content_Yielder(
                            self._format_comment(content.comment) + new_line,
                            self.console_printer_colors.comment
                        )
                    # yield the Selectors
                    yield Content_Yielder(
                        f"{content.selection}{{{new_line}",
                        self.console_printer_colors.selector
                    )
                    # yield the styling
                    for style_prop in content.styling: #type:PROPERTIES
                        # yield indentation, to not have it have a styling makup
                        yield Content_Yielder(
                            indentation,
                            self.console_printer_colors.empty
                        )

                        # yield the name
                        yield Content_Yielder(
                            f"{style_prop.name}",
                            self.console_printer_colors.property_name
                        )

                        # yield the colon
                        yield Content_Yielder(
                            f": ",
                            self.console_printer_colors.text
                        )
                        # yield the value
                        yield Content_Yielder(
                            style_prop.value_printer(),
                            self.console_printer_colors.property_value
                        )
                        # yield the semicolon
                        yield Content_Yielder(
                            f";{new_line}",
                            self.console_printer_colors.text
                        )

                    # yield the closing of the selector
                    yield Content_Yielder(
                        f"}}{new_line * 2}",
                        self.console_printer_colors.selector
                    )

                # else it will catch the ones that were commented but now defunct
                case Content_Comment() | Content_Styling() | Content_Line() | Content_Seperation():
                    continue

                case _:
                    raise SyntaxError

    # ------------------------------------------------------------------------------------------------------------------
    # - Properties -
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def manager(self):
        # if the manager is not set yet, it will be created
        if self._manager is None:
            self._manager = CSSPrinterManager()
        return self._manager

    # ------------------------------------------------------------------------------------------------------------------
    # - Output Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def to_string(self):
        return ''.join(segement.text for segement in self._string_generator())

    def to_console(self):
        for segement in self._string_generator():
            print(
                segement.console_styling(segement.text),
                end=""
            )

    def to_file(self, file_path:str|Iterable=None):
        if file_path is None:
            raise ValueError

        if self.file_overwrite:
            file_operation = "w+"
        else:
            file_operation = "a+"

        if isinstance(file_path, str):
            with open(file_path, file_operation) as file:
                for segement in self._string_generator():
                    file.write(segement.text)

        elif isinstance(file_path, Iterable):
            for file_path_ in file_path:
                with open(file_path_, file_operation) as file:
                    for segement in self._string_generator():
                        file.write(segement.text)
        else:
            raise TypeError