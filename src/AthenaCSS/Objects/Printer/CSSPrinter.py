# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
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
from AthenaCSS.Objects.Printer.Content import (
    ContentSeperation, ContentComment, ContentStyling, ContentLine, ContentYielder
)

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
PROPERTIES = CSSProperty|CSSPropertyShorthand
CONTENT = ContentComment | ContentStyling | ContentLine | ContentSeperation
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
@dataclass(slots=True, eq=False)
class CSSPrinterManager:
    content: list[CONTENT]=field(init=False, default_factory=list)
    _lock:bool=field(init=False, default=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Population Methods -
    # ------------------------------------------------------------------------------------------------------------------
    @locked
    def add_style(self, selection:CSSSelection, styling:tuple[PROPERTIES]):
        self.content.append(ContentStyling(selection, styling))

    @locked
    def add_comment(self, comment:str):
        self.content.append(ContentComment(comment))

    @locked
    def add_seperation(self):
        self.content.append(ContentSeperation())

    @locked
    def add_line(self):
        self.content.append(ContentLine())


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

    comment_start:str="/*" # done for easy manipulation
    comment_end:str="*/"

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
            return f"{self.comment_start}{comment.replace(new_line, ' ')}{self.comment_end}"
        else:
            return "\n".join(f"{self.comment_start}{c}{self.comment_end}" for c in comment.split("\n"))

    def _string_generator(self):
        new_line = "" if self.one_line else "\n"
        indentation = "" if self.one_line else (" " * self.indentation)

        for content in self.manager.content:
            match content:
                # ------------------------------------------------------------------------------------------------------
                # only print if comments are enabled
                case ContentComment() if self.comments:
                    yield ContentYielder(
                        self._format_comment(content.comment) + new_line,
                        self.console_printer_colors.comment
                    )

                # ------------------------------------------------------------------------------------------------------
                # only print if comments are enabled
                case ContentSeperation() if self.comments:
                    yield ContentYielder(
                        self._format_comment(self.seperation_character * self.seperation_length) + new_line,
                        self.console_printer_colors.comment
                    )

                # ------------------------------------------------------------------------------------------------------
                case ContentLine():
                    yield ContentYielder(
                        new_line,
                        self.console_printer_colors.line
                    )

                # ------------------------------------------------------------------------------------------------------
                case ContentStyling():
                    # yield the Selectors
                    yield ContentYielder(
                        f"{content.selection}{{{new_line}",
                        self.console_printer_colors.selector
                    )
                    # yield the styling
                    for style_prop in content.styling: #type:PROPERTIES
                        # yield indentation, to not have it have a styling makup
                        yield ContentYielder(
                            indentation,
                            self.console_printer_colors.empty
                        )

                        # yield the name
                        yield ContentYielder(
                            f"{style_prop.name}",
                            self.console_printer_colors.property_name
                        )

                        # yield the colon
                        yield ContentYielder(
                            f": ",
                            self.console_printer_colors.text
                        )
                        # yield the value
                        yield ContentYielder(
                            style_prop.value_printer(),
                            self.console_printer_colors.property_value
                        )
                        # yield the semicolon
                        yield ContentYielder(
                            f";{new_line}",
                            self.console_printer_colors.text
                        )

                    # yield the closing of the selector
                    yield ContentYielder(
                        f"}}{new_line * 2}",
                        self.console_printer_colors.selector
                    )

                # ------------------------------------------------------------------------------------------------------
                # else it will catch the ones that were commented but now defunct
                case ContentComment() | ContentStyling() | ContentLine() | ContentSeperation():
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

        file_operation = "w+" if self.file_overwrite else "a+"

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
