import unittest

from reverse_string import RevereString


class MyTestCase(unittest.TestCase):

    def test_reverse(self):
        func = RevereString().reverse
        self.assertEqual(func(None), None)
        self.assertEqual(func(['']), [''])
        self.assertEqual(func(['f', 'o', 'o', ' ', 'b', 'a', 'r']),
                         ['r', 'a', 'b', ' ', 'o', 'o', 'f'])

    def test_reverse_inplace(self):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func = RevereString().reverse
        self.assertEqual(func(None), None)
        self.assertEqual(func(['']), [''])
        self.assertEqual(func(['f', 'o', 'o', ' ', 'b', 'a', 'r']),
                         ['r', 'a', 'b', ' ', 'o', 'o', 'f'])

if __name__ == '__main__':
    unittest.main()
