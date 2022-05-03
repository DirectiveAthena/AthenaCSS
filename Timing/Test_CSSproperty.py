import timeit
from AthenaCSS.CssLib.CSSproperties import align_content


def main():
    align_content("stretch")

if __name__ == '__main__':
    print(timeit.repeat(lambda:main(),number=1000000, repeat=5))
    # [0.9583764999988489, 0.9730730000010226, 0.9776122000184841, 0.9555353000178002, 0.9556455000129063]