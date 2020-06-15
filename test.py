import unittest

from main import analyze


class TestTriplets(unittest.TestCase):
    def test_sample(self):
        expected = [(('a', 'k', 'u'), 2), (('a', 'k', 'l'), 1), (('a', 'l', 'u'), 1), (('k', 'l', 'u'), 1), (('a', 'k', 'n'), 1), (('a', 'n', 'u'), 1), (('k', 'n', 'u'), 1)]
        self.assertEqual(analyze('input/sample.txt'), expected)

    def test_top_n(self):
        expected = [(('a', 'k', 'u'), 2), (('a', 'k', 'l'), 1)]
        self.assertEqual(analyze('input/sample.txt', top_n=2), expected)

    def test_char_length(self):
        expected = [(('a', 'k', 'l', 'u'), 1), (('a', 'k', 'n', 'u'), 1)]
        self.assertEqual(analyze('input/sample.txt', char_length=4), expected)

    def test_char_length2(self):
        expected = []
        self.assertEqual(analyze('input/sample.txt', char_length=5), expected)


if __name__ == '__main__':
    unittest.main()
