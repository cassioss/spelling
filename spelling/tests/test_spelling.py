import unittest
from spelling.spelling_eng import EnglishSpeller


class TestSpelling(unittest.TestCase):

    def setUp(self):
        self.speller = EnglishSpeller()

    def check_spelling(self, num, word):
        self.assertEqual(word, self.speller.spell_out(num))

    def test_units(self):
        self.check_spelling(0, 'zero')
        self.check_spelling(1, 'one')
        self.check_spelling(2, 'two')
        self.check_spelling(3, 'three')
        self.check_spelling(4, 'four')
        self.check_spelling(5, 'five')
        self.check_spelling(6, 'six')
        self.check_spelling(7, 'seven')
        self.check_spelling(8, 'eight')
        self.check_spelling(9, 'nine')


if __name__ == '__main__':
    unittest.main()
