import timeit
from AthenaCSS.CssLib.Element import CSSelement
from AthenaCSS.CssLib.Selectors.CSSselectors import *
from AthenaCSS.CssLib.Selectors.CSSselectorCombination import Selector_Combination
from AthenaCSS.CssLib.Properties.CSSproperties import *


def main():
    el = CSSelement()
    el.append(
        Selector_Combination(
            Selector_Header1,
            Selector_Id("test-id"),
            Selector_Class("test-class")
        ),
        Selector_Element("elementX"), # <elementX></elementX>
        Selector_Class("test"), # <element class="test"> -> .test
        Selector_Class("test2"),
        align_items("center")
    )

    print(el)


if __name__ == '__main__':
    main()
    # print(timeit.repeat(lambda:main(),number=1000000, repeat=5))
    # [0.9583764999988489, 0.9730730000010226, 0.9776122000184841, 0.9555353000178002, 0.9556455000129063]