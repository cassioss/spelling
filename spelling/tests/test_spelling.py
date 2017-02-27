import unittest
from spelling.spelling import *


class TestSpelling(unittest.TestCase):

    

    def test_units(self):
        self.assertEqual('ZERO', spell_out(0))
        self.assertEqual('ONE', spell_out(1))
        self.assertEqual('TWO', spell_out(2))
        self.assertEqual('THREE', spell_out(3))
        self.assertEqual('FOUR', spell_out(4))
        self.assertEqual('FIVE', spell_out(5))
        self.assertEqual('SIX', spell_out(6))
        self.assertEqual('SEVEN', spell_out(7))
        self.assertEqual('EIGHT', spell_out(8))
        self.assertEqual('NINE', spell_out(9))

if __name__ == '__main__':
    unittest.main()
