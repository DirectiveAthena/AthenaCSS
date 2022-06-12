# - AthenaCSS -
[![pypi](https://img.shields.io/pypi/v/AthenaCSS)](https://pypi.org/project/AthenaCSS/) [![GitHub license](https://img.shields.io/github/license/DirectiveAthena/AthenaCSS)](https://github.com/DirectiveAthena/VerSC-AthenaColor/blob/master/LICENSE) [![Discord](https://img.shields.io/discord/814599159926620160?color=maroon)](https://discord.gg/6JcDbhXkCH) [![Downloads](https://pepy.tech/badge/athenalib)](https://pepy.tech/project/athenalib)



--- 
## Package Details
#### Details and features 
- A Python package which allows CSS to be written as a Python script
- CSS output to file, string or console from the Python script

#### Python Version
- Supported Python versions: **3.10**
  - Other older versions of Python are not currently supported. 
  - These older versions will probably not be supported by [@AndreasSas](https://github.com/AndreasSas) himself, but if you want to contribute to the project and make this package compatible with older versions of Python, Pull requests are always welcome.

---
## Quick Examples
The following example is only a very small CSS code piece, but should bring the idea across of how it works.
```python
from AthenaCSS import *
from AthenaColor import RGB # Dependecy on own other package

with (css_generator := CSSGenerator()) as generator:
    with (rule0 := CSSRule()) as (selector, declaration):
        selector.add(
            SelectorElement.H1(CSSClass("title")),
        )
        declaration.add(
            Property.Color(RGB(128,64,32)),
        )
    generator.add_comment(
        "The following sets the Header with the class of 'title' to have a specific color"
    ).add_rule(
        rule0
    )
css_generator.to_console()
```
The above code will output the following CSS to the console:
```css
/*The following sets the Header with the class of 'title' to have a specific color*/
h1.title {
    color: rgb(128, 64, 32);
}
```

---
## Documentation
Full documentation can be found at:
**[directiveathena.com](https://publish.obsidian.md/directiveathena/)** (redirect to Obsidian.md publish site)
(Reminder, the documentation is still under heavy development)

---
## Install
To install the package in your Python environment

```
pip install AthenaCSS --upgrade
```

---

## Links 
Project files can be found at:    
- [GitHub Repo](https://github.com/DirectiveAthena/AthenaCSS)     
- [Pypi link](https://pypi.org/project/AthenaCSS/)    

---

## Disclaimer
With  *No Dependency*, the standard library is not counted as a dependency

---
Made By Andreas Sas,` 2022`