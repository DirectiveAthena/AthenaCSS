# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaCSS.CssLib.CSSproperties import animation, animantion_name

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Main(unittest.TestCase):
    def test_Main(self):
        a = animation(
            name= None,
            duration= 0,
            timing_function= None,
            delay= 0,
            iteration_count= 1,
            direction= "normal",
            fill_mode= None,
            play_state= "running",
        )
        print(a)
        self.assertTrue(
            isinstance(a.name, animantion_name)
        )


        # self.fail("Create a system that houses all CSS  properties")