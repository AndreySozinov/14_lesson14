import unittest
from Task01 import only_alphabet


class TestCaseAlphabet(unittest.TestCase):
    def setUp(self) -> None:
        self.text_ = 'another fine myth'

    def test_method01(self):
        self.assertSequenceEqual(only_alphabet(self.text_), self.text_)

    def test_method02(self):
        self.assertEqual(only_alphabet('Another fine myth'), self.text_)

    def test_method03(self):
        self.assertEqual(only_alphabet('another, fine- myth.'), self.text_)

    def test_method04(self):
        self.assertSequenceEqual(only_alphabet('русanother fineкие myth'), self.text_)

    def test_method05(self):
        self.assertSequenceEqual(only_alphabet('65_Another 570fine* myth.Русский'), self.text_)


if __name__ == '__main__':
    unittest.main(verbosity=2)
