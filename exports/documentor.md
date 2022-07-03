#class AthenaCSS.**CSSAttribute**(value: Any, name: str, *, selection_operator: str = None) -> None

A special class to be used for all CSS attribute selectors.
This is done because these type selectors can a name by itself, or also combined with a specific value

**__str__**(self)

Return str(self).

**equals**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**contains_word**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**starting_equal**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**begins_with**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**ends_with**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**contains_substring**(cls, name: str, value: Any) -> CSSAttribute

*`-!- Missing documentation -!-`*

**__call__**(self, name: str, value: Any = None)

Call self as a function.

**__init__**(self, value: Any, name: str, *, selection_operator: str = None) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

**__hash__**(self)

Return hash(self).

---

#class AthenaCSS.**CSSClass**(*parts: str | CSSElement, defined_name=None)

CSSElement(*parts: 'str | CSSElement', defined_name=None)

**__str__**(self) -> str

Return str(self).

---

#class AthenaCSS.**CSSComment**(comment: str) -> None

CSSComment(comment: 'str')

**to_string**(self, **kwargs) -> str

*`-!- Missing documentation -!-`*

**to_console**(self, console_color_guide: ConsoleColorGuide, **kwargs) -> str

*`-!- Missing documentation -!-`*

**__init__**(self, comment: str) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

**__hash__**(self)

Return hash(self).

---

#class AthenaCSS.**CSSCommentSeparator**(length: int = 64) -> None

CSSCommentSeparator(length: 'int' = 64)

**to_string**(self, **kwargs) -> str

*`-!- Missing documentation -!-`*

**to_console**(self, console_color_guide: ConsoleColorGuide, **kwargs) -> str

*`-!- Missing documentation -!-`*

**__init__**(self, length: int = 64) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**CSSElement**(*parts: str | CSSElement, defined_name=None)

CSSElement(*parts: 'str | CSSElement', defined_name=None)

**__init__**(self, *parts: str | CSSElement, defined_name=None)

Initialize self.  See help(type(self)) for accurate signature.

**__str__**(self) -> str

Return str(self).

**__call__**(self, *parts)

Call self as a function.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

**__hash__**(self)

Return hash(self).

---

#class AthenaCSS.**CSSEmptyLine**()

Helper class that provides a standard way to create an ABC using
inheritance.

**to_string**(self, **kwargs) -> str

*`-!- Missing documentation -!-`*

**to_console**(self, one_line: bool, **kwargs) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.**CSSGenerator**(*, console_color_guide: ConsoleColorGuide = <factory>, output_indentation: int = 4, output_one_line: bool = False, _manager: ManagerGenerator = None) -> None

CSSGenerator(*, console_color_guide: 'ConsoleColorGuide' = <factory>, output_indentation: 'int' = 4, output_one_line: 'bool' = False, _manager: 'ManagerGenerator' = None)

**__enter__**(self) -> ManagerGenerator

*`-!- Missing documentation -!-`*

**__exit__**(self, exc_type, exc_val, exc_tb)

*`-!- Missing documentation -!-`*

**_output_partial**(self, call: Callable) -> Callable

*`-!- Missing documentation -!-`*

**to_string**(self) -> str

*`-!- Missing documentation -!-`*

**to_console**(self) -> None

*`-!- Missing documentation -!-`*

**to_file**(self, filepath: str) -> None

*`-!- Missing documentation -!-`*

**__init__**(self, *, console_color_guide: ConsoleColorGuide = <factory>, output_indentation: int = 4, output_one_line: bool = False, _manager: ManagerGenerator = None) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**CSSId**(*parts: str | CSSElement, defined_name=None)

CSSElement(*parts: 'str | CSSElement', defined_name=None)

**__str__**(self) -> str

Return str(self).

---

#class AthenaCSS.**CSSProperty**(value: InitVar[Any] = <property object at 0x0000022A390520C0>, *, important: bool = False, value_wrapped: bool = False) -> None

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__post_init__**(self, value)

*`-!- Missing documentation -!-`*

**printer**(self) -> str

*`-!- Missing documentation -!-`*

**name_printer**(self) -> str

*`-!- Missing documentation -!-`*

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

**__str__**(self) -> str

Return str(self).

**__init__**(self, value: InitVar[Any] = <property object at 0x0000022A390520C0>, *, important: bool = False, value_wrapped: bool = False) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**CSSPropertyShorthand**()

Helper class that provides a standard way to create an ABC using
inheritance.

**name_printer**(self) -> str

*`-!- Missing documentation -!-`*

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

**printer**(self) -> str

*`-!- Missing documentation -!-`*

**__str__**(self) -> str

Return str(self).

---

#class AthenaCSS.**CSSPseudo**(value: Any = None, *, defined_name: str = None) -> None

A special class to be inherited from by all Pseudo CSS selectors.
This is done because these type selectors can have an extra value tied to them.

**__str__**(self) -> str

Return str(self).

**__call__**(self, value: Any = None)

Call self as a function.

**__init__**(self, value: Any = None, *, defined_name: str = None) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

**__hash__**(self)

Return hash(self).

---

#class AthenaCSS.**CSSRule**(*, one_line_overwrite: bool = False, manager_overwrite: bool = False, _selector_manager: ManagerSelectors = None, _declaration_manager: ManagerDeclarations = None) -> None

CSSRule(*, one_line_overwrite: 'bool' = False, manager_overwrite: 'bool' = False, _selector_manager: 'ManagerSelectors' = None, _declaration_manager: 'ManagerDeclarations' = None)

**_define_managers**(self)

*`-!- Missing documentation -!-`*

**__enter__**(self) -> tuple[ManagerSelectors, ManagerDeclarations]

*`-!- Missing documentation -!-`*

**__exit__**(self, exc_type, exc_val, exc_tb)

*`-!- Missing documentation -!-`*

**_selectors_generator**(self) -> str

*`-!- Missing documentation -!-`*

**_declaration_generator**(self) -> tuple[str, str]

*`-!- Missing documentation -!-`*

**_to_options**(self, indentation: int, one_line: bool) -> tuple[str, str]

*`-!- Missing documentation -!-`*

**to_string**(self, /, indentation: int, one_line: bool, **kwargs) -> str

*`-!- Missing documentation -!-`*

**to_console**(self, /, console_color_guide: ConsoleColorGuide, one_line: bool, indentation: int, **kwargs) -> str

*`-!- Missing documentation -!-`*

**__init__**(self, *, one_line_overwrite: bool = False, manager_overwrite: bool = False, _selector_manager: ManagerSelectors = None, _declaration_manager: ManagerDeclarations = None) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

**__hash__**(self)

Return hash(self).

---

#class AthenaCSS.**ConsoleColorGuide**(selector: Callable = <bound method RgbControlledNested.GoldenRod of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_name: Callable = <bound method RgbControlledNested.LightSkyBlue of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_value: Callable = <bound method RgbControlledNested.Snow of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, text_general: Callable = <bound method RgbControlledNested.SlateGray of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, comment: Callable = <bound method RgbControlledNested.ForestGreen of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>) -> None

ConsoleColorGuide(selector: 'Callable' = <bound method RgbControlledNested.GoldenRod of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_name: 'Callable' = <bound method RgbControlledNested.LightSkyBlue of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_value: 'Callable' = <bound method RgbControlledNested.Snow of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, text_general: 'Callable' = <bound method RgbControlledNested.SlateGray of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, comment: 'Callable' = <bound method RgbControlledNested.ForestGreen of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>)

**__init__**(self, selector: Callable = <bound method RgbControlledNested.GoldenRod of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_name: Callable = <bound method RgbControlledNested.LightSkyBlue of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, descriptor_value: Callable = <bound method RgbControlledNested.Snow of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, text_general: Callable = <bound method RgbControlledNested.SlateGray of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>, comment: Callable = <bound method RgbControlledNested.ForestGreen of <AthenaColor.models.console.styling.rgb_controlled_nested.RgbControlledNested object at 0x0000022A390153F0>>) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**ManagerDeclarations**() -> None

ManagerDeclarations()

**add**(self, *declarations: Declarations) -> ManagerDeclarations

*`-!- Missing documentation -!-`*

**__init__**(self) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**ManagerGenerator**() -> None

ManagerGenerator()

**add_rule**(self, *rules: CSSRule) -> ManagerGenerator

*`-!- Missing documentation -!-`*

**add_comment**(self, comment: str | CSSComment) -> ManagerGenerator

*`-!- Missing documentation -!-`*

**add_empty_line**(self) -> ManagerGenerator

*`-!- Missing documentation -!-`*

**add_comment_separator**(self, separator_length: int = 64) -> ManagerGenerator

*`-!- Missing documentation -!-`*

**add**(self, *content: CSSComment | CSSRule | CSSEmptyLine | CSSCommentSeparator)

*`-!- Missing documentation -!-`*

**__init__**(self) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.**ManagerSelectors**() -> None

ManagerSelectors()

**SelectorGroup**(selectors: ForwardRef(tuple[SELECTORS]), group_type: ForwardRef(SELECTORGROUP_TYPES))

SelectorGroup(selectors, group_type)

**add**(self, *selectors: SELECTORS) -> ManagerSelectors

*`-!- Missing documentation -!-`*

**add_descendants**(self, *selectors: SELECTORS) -> ManagerSelectors

*`-!- Missing documentation -!-`*

**add_following**(self, *selectors: SELECTORS) -> ManagerSelectors

*`-!- Missing documentation -!-`*

**add_family**(self, *selectors: SELECTORS) -> ManagerSelectors

*`-!- Missing documentation -!-`*

**add_preceding**(self, *selectors: SELECTORS) -> ManagerSelectors

*`-!- Missing documentation -!-`*

**__init__**(self) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.models.athenalib_imports.**CentiMeter**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**CubicBezier**(x1: float | int = 0, y1: float | int = 0, x2: float | int = 0, y2: float | int = 0)

CubicBezier(x1: 'float | int' = 0, y1: 'float | int' = 0, x2: 'float | int' = 0, y2: 'float | int' = 0)

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**DeciMeter**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Degree**(value: int | float = 0) -> None

Degree(value: 'int | float' = 0)

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ElementFontHeight**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ElementFontSize**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Hour**(value: int | float | TimeValue)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Inch**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Meter**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**MilliMeter**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**MilliSecond**(value: int | float | TimeValue)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Minute**(value: int | float | TimeValue)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**NewEmpty**()

*`-!- Missing documentation -!-`*

**new_empty**(cls)

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.models.athenalib_imports.**Percent**(value: int | float)

*`-!- Missing documentation -!-`*

**new_full**(cls)

*`-!- Missing documentation -!-`*

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Pica**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Pixel**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Point**(value: int | float | AbsoluteLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**RootElementFontSize**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Second**(value: int | float | TimeValue)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**Url**(value: str)

*`-!- Missing documentation -!-`*

**__str__**(self) -> str

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ViewportHeightPercent**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ViewportLargerPercent**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ViewportSmallerPercent**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ViewportWidthPercent**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.models.athenalib_imports.**ZeroCharacterWidth**(value: int | float | RelativeLength)

Helper class that provides a standard way to create an ABC using
inheritance.

**__str__**(self)

Return str(self).

---

#class AthenaCSS.data.properties.**AccentColor**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AlignContent**(value=stretch, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=stretch, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AlignItems**(value=stretch, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=stretch, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AlignSelf**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**All**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Animation**(name=None, duration=Second(value=0), timing_function=ease, delay=Second(value=0), iteration_count=1, direction=normal, fill_mode=None, play_state=running)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, name=None, duration=Second(value=0), timing_function=ease, delay=Second(value=0), iteration_count=1, direction=normal, fill_mode=None, play_state=running)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**AnimationDelay**(value=Second(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Second(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationDirection**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationDuration**(value=Second(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Second(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationFillMode**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationIterationCount**(value=1, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=1, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationName**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationPlayState**(value=running, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=running, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**AnimationTimingFunction**(value=ease, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=ease, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackdropFilter**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackfaceVisibility**(value=visible, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=visible, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Background**(color=transparent, image=None, position=(Percent(value=0), Percent(value=0)), size=auto, repeat=repeat, origin=padding-box, clip=border-box, attachment=scroll)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, color=transparent, image=None, position=(Percent(value=0), Percent(value=0)), size=auto, repeat=repeat, origin=padding-box, clip=border-box, attachment=scroll)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BackgroundAttachment**(value=scroll, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=scroll, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundBlendMode**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundClip**(value=border-box, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=border-box, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundImage**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundOrigin**(value=padding-box, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=padding-box, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundPosition**(value=(Percent(value=0), Percent(value=0)), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(Percent(value=0), Percent(value=0)), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundRepeat**(value=repeat, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=repeat, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BackgroundSize**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Border**(width=medium, style=None, color=transparent)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=transparent)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderBottom**(width=medium, style=None, color=transparent)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=transparent)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderBottomColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderBottomLeftRadius**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderBottomRightRadius**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderBottomStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderBottomWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderCollapse**(value=separate, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=separate, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderImage**(source=None, slice_=Percent(value=100), width=medium, outset=0, repeat=stretch)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, source=None, slice_=Percent(value=100), width=medium, outset=0, repeat=stretch)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderImageOutset**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderImageRepeat**(value=stretch, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=stretch, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderImageSlice**(value=Percent(value=100), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=100), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderImageSource**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderImageWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderLeft**(width=medium, style=None, color=transparent)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=transparent)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderLeftColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderLeftStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderLeftWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderRadius**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderRight**(width=medium, style=None, color=transparent)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=transparent)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderRightColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderRightStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderRightWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderSpacing**(value=Pixel(value=2), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=2), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderTop**(width=medium, style=None, color=transparent)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=transparent)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**BorderTopColor**(value=transparent, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=transparent, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderTopLeftRadius**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderTopRightRadius**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderTopStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderTopWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BorderWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Bottom**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BoxDecorationBreak**(value=slice, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=slice, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BoxShadow**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BoxSizing**(value=content-box, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=content-box, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BreakAfter**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BreakBefore**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**BreakInside**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**CaptionSide**(value=top, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=top, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**CaretColor**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Clear**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ClipPath**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Color**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnCount**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnFill**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnGap**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnRule**(width=medium, style=None, color=None)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=medium, style=None, color=None)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**ColumnRuleColor**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnRuleStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnRuleWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnSpan**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ColumnWidth**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Columns**(width=auto, count=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=auto, count=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**Content**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**CounterIncrement**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**CounterReset**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Cursor**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Direction**(value=ltr, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=ltr, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Display**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**EmptyCells**(value=show, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=show, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Filter**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Flex**(grow=0, shrink=1, basis=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, grow=0, shrink=1, basis=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**FlexBasis**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FlexDirection**(value=row, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=row, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FlexFlow**(value=(row, nowrap), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(row, nowrap), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FlexGrow**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FlexShrink**(value=1, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=1, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FlexWrap**(value=nowrap, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=nowrap, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Float**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Font**(style=normal, variant=normal, weight=normal, size=medium, family=None)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, style=normal, variant=normal, weight=normal, size=medium, family=None)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**FontFamily**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontFeatureSetting**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontKerning**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontSize**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontSizeAdjust**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontStretch**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontStyle**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontVariant**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontVariantCaps**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**FontWeight**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Gap**(value=(normal, normal), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(normal, normal), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Grid**(template_rows=None, template_columns=None, template_areas=None, auto_rows=auto, auto_columns=auto, auto_flow=row)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, template_rows=None, template_columns=None, template_areas=None, auto_rows=auto, auto_columns=auto, auto_flow=row)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridArea**(row_start=auto, column_start=auto, row_end=auto, column_end=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, row_start=auto, column_start=auto, row_end=auto, column_end=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridAutoColumns**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridAutoFlow**(value=row, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=row, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridAutoRows**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridColumn**(start=auto, end=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, start=auto, end=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridColumnEnd**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridColumnGap**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridColumnStart**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridGap**(start=0, end=0)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, start=0, end=0)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridRow**(start=auto, end=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, start=auto, end=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridRowEnd**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridRowGap**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridRowStart**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridTemplate**(rows=None, columns=None, areas=None)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, rows=None, columns=None, areas=None)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**GridTemplateAreas**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridTemplateColumns**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**GridTemplateRows**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**HangingPunctuation**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Height**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Hyphens**(value=manual, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=manual, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ImageRendering**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Isolation**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**JustifyContent**(value=flex-start, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=flex-start, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Left**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**LetterSpacing**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**LineHeight**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ListStyle**(type_=disc, position=outside, image=None)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, type_=disc, position=outside, image=None)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**ListStyleImage**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ListStylePosition**(value=outside, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=outside, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ListStyleType**(value=disc, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=disc, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Margin**(top=Pixel(value=0), right=Pixel(value=0), bottom=Pixel(value=0), left=Pixel(value=0))

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, top=Pixel(value=0), right=Pixel(value=0), bottom=Pixel(value=0), left=Pixel(value=0))

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**MarginBottom**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MarginLeft**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MarginRight**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MarginTop**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskImage**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskMode**(value=match-source, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=match-source, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskOrigin**(value=border-box, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=border-box, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskPosition**(value=(Percent(value=0), Percent(value=0)), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(Percent(value=0), Percent(value=0)), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskRepeat**(value=repeat, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=repeat, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaskSize**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaxHeight**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MaxWidth**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MinHeight**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MinWidth**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**MixBlendMode**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ObjectFit**(value=fill, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=fill, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ObjectPosition**(value=(Percent(value=50), Percent(value=50)), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(Percent(value=50), Percent(value=50)), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Opacity**(value=1, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=1, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Order**(value=0, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=0, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Orphans**(value=2, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=2, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Outline**(width=Pixel(value=0), style=Pixel(value=0), color=Pixel(value=0))

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, width=Pixel(value=0), style=Pixel(value=0), color=Pixel(value=0))

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**OutlineColor**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OutlineOffset**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OutlineStyle**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OutlineWidth**(value=medium, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=medium, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Overflow**(value=visible, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=visible, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OverflowWrap**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OverflowX**(value=visible, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=visible, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**OverflowY**(value=visible, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=visible, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Padding**(top=Pixel(value=0), right=Pixel(value=0), bottom=Pixel(value=0), left=Pixel(value=0))

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, top=Pixel(value=0), right=Pixel(value=0), bottom=Pixel(value=0), left=Pixel(value=0))

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**PaddingBottom**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PaddingLeft**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PaddingRight**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PaddingTop**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PageBreakAfter**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PageBreakBefore**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PageBreakInside**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Perspective**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PerspectiveOrigin**(value=(Percent(value=50), Percent(value=50)), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(Percent(value=50), Percent(value=50)), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**PointerEvents**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Position**(value=static, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=static, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Quotes**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Resize**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Right**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**RowGap**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ScrollBehavior**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TabSize**(value=8, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=8, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TableLayout**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextAlign**(value=left, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=left, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextAlignLast**(value=left, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=left, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextDecoration**(line=None, color=None, style=solid, thickness=auto)

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, line=None, color=None, style=solid, thickness=auto)

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**TextDecorationColor**(value, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextDecorationLine**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextDecorationStyle**(value=solid, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=solid, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextDecorationThickness**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextIndent**(value=Pixel(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextJustify**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextOverflow**(value=clip, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=clip, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextShadow**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TextTransform**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Top**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Transform**(value=None, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TransformOrigin**(value=(Percent(value=50), Percent(value=50), Pixel(value=0)), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=(Percent(value=50), Percent(value=50), Pixel(value=0)), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TransformStyle**(value=flat, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=flat, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Transition**(property_=all, duration=Second(value=0), timing_function=ease, delay=Second(value=0))

Helper class that provides a standard way to create an ABC using
inheritance.

**__init__**(self, property_=all, duration=Second(value=0), timing_function=ease, delay=Second(value=0))

Initialize self.  See help(type(self)) for accurate signature.

**value_printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.properties.**TransitionDelay**(value=Second(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Second(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TransitionDuration**(value=Second(value=0), **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Second(value=0), **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TransitionProperty**(value=all, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=all, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**TransitionTimingFunction**(value=ease, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=ease, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**UnicodeBidi**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**UserSelect**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**VerticalAlign**(value=baseline, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=baseline, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Visibility**(value=visible, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=visible, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**WhiteSpace**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Widows**(value=2, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=2, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**Width**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**WordBreak**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**WordSpacing**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**WordWrap**(value=normal, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=normal, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**WritingMode**(value=horizontal-tb, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=horizontal-tb, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.properties.**ZIndex**(value=auto, **kwargs)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=auto, **kwargs)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**LinearGradient**(*value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, *value)

Initialize self.  See help(type(self)) for accurate signature.

**printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.subproperties.**Steps**(value=None)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Blur**(value=Pixel(value=0))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Pixel(value=0))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Brightness**(value=Percent(value=100))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=100))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Contrast**(value=Percent(value=100))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=100))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**DropShadow**(value=None)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=None)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Grayscale**(value=Percent(value=0))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=0))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**HueRotate**(value=Degree(value=0))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Degree(value=0))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Invert**(value=Percent(value=0))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=0))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Matrix**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Matrix3D**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Rotate**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Rotate3D**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**RotateX**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**RotateY**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**RotateZ**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Saturate**(value=Percent(value=100))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=100))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Scale**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Scale3D**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**ScaleX**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**ScaleY**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**ScaleZ**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Sepia**(value=Percent(value=0))

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value=Percent(value=0))

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Skew**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**SkewX**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**SkewY**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Translate**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**Translate3D**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**TranslateX**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**TranslateY**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.data.subproperties.**TranslateZ**(value)

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**__init__**(self, value)

Initialize self.  See help(type(self)) for accurate signature.

---

#class AthenaCSS.models.declarations.value_logic.**ValueLogic**(*, value_choice: list | dict = <factory>, default: Any = None, printer_space: str =  ) -> None

ValueLogic(*, value_choice: 'list | dict' = <factory>, default: 'Any' = None, printer_space: 'str' = ' ')

**__post_init__**(self)

*`-!- Missing documentation -!-`*

**validate_value**(self, value)

*`-!- Missing documentation -!-`*

**printer**(self) -> str

*`-!- Missing documentation -!-`*

**__str__**(self) -> str

Return str(self).

**__init__**(self, *, value_choice: list | dict = <factory>, default: Any = None, printer_space: str =  ) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#func AthenaCSS.models.declarations.value_logic.**LogicAssembly**(value_choice: dict) -> list[LogicComponent]

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.models.declarations.value_logic.**LogicComponent**(types: Any, specific: Any) -> None

LogicComponent(types: 'Any', specific: 'Any')

**__init__**(self, types: Any, specific: Any) -> None

Initialize self.  See help(type(self)) for accurate signature.

**__repr__**(self)

Return repr(self).

**__eq__**(self, other)

Return self==value.

---

#class AthenaCSS.models.declarations.property_sub.**CSSSubProp**(value: InitVar[Any] = <property object at 0x0000022A390520C0>, *, important: bool = False, value_wrapped: bool = False) -> None

CSSProperty(value: 'InitVar[Any]' = <property object at 0x0000022A390520C0>, *, important: 'bool' = False, value_wrapped: 'bool' = False)

**printer**(self) -> str

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.data.support.**SELECTORGROUP_TYPES**(value, names=None, *, module=None, qualname=None, type=None, start=1)

An enumeration.

**_generate_next_value_**(name, start, count, last_values)

Generate the next value when not given.

name: the name of the member
start: the initial start value or None
count: the number of existing members
last_value: the last value assigned or None

**object**()

The base class of the class hierarchy.

When called, it accepts no arguments and returns a new featureless
instance that has no instance attributes and cannot be given any.

**__new__**(cls, value)

Create and return a new object.  See help(type) for accurate signature.

---

#func AthenaCSS.data.support.**locked**(fnc)

*`-!- Missing documentation -!-`*

---

#func AthenaCSS._info._v.**_version**()

*`-!- Missing documentation -!-`*

---

#class AthenaCSS.models.generator.generator_content.**_Content**()

Helper class that provides a standard way to create an ABC using
inheritance.

**to_string**(self, **kwargs) -> str

*`-!- Missing documentation -!-`*

**to_console**(self, **kwargs) -> str

*`-!- Missing documentation -!-`*

---

