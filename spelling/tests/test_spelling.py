import unittest
from spelling.spelling_eng import *


class TestSpelling(unittest.TestCase):

    def test_units(self):
        self.assertEqual('zero',  spell_out_english(0))
        self.assertEqual('one',   spell_out_english(1))
        self.assertEqual('two',   spell_out_english(2))
        self.assertEqual('three', spell_out_english(3))
        self.assertEqual('four',  spell_out_english(4))
        self.assertEqual('five',  spell_out_english(5))
        self.assertEqual('six',   spell_out_english(6))
        self.assertEqual('seven', spell_out_english(7))
        self.assertEqual('eight', spell_out_english(8))
        self.assertEqual('nine',  spell_out_english(9))

if __name__ == '__main__':
    unittest.main()
