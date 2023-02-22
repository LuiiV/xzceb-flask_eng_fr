import unittest
from translator import english_to_french, french_to_english


class testEnglish(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

    def test_null_input_english_to_french(self):
        self.assertIsNone(english_to_french(None))

class testFrench(unittest.TestCase):

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

    def test_null_input_french_to_english(self):
        self.assertIsNone(french_to_english(None))

unittest.main()