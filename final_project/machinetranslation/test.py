import unittest
from translator import french_to_english, english_to_french

class TestEnglish(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_not_english_to_french(self):
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


class TestFrench(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_not_french_to_english(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


if __name__ == '__main__':
    unittest.main()