import timeit
from AthenaCSS.CssLib.Element import CSSelement
from AthenaCSS.CssLib.Selectors.CSSselectors import SelectorClass
from AthenaCSS.CssLib.Properties.CSSproperties import *


def main():
    el = CSSelement()
    el.append(
        SelectorClass("test"),
        SelectorClass("test2"),
        align_items("center")
    )

    print(el)


if __name__ == '__main__':
    main()
    # print(timeit.repeat(lambda:main(),number=1000000, repeat=5))
    # [0.9583764999988489, 0.9730730000010226, 0.9776122000184841, 0.9555353000178002, 0.9556455000129063]