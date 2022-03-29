import unittest

from machinetranslation.translator import english_to_french, french_to_english

class TranslationTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('None'), '')

    def test_two(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('None'), '')

if __name__ == "__main__":
    unittest.main()