import unittest

from permutation import Permutations


class MyTestCase(unittest.TestCase):

    def test_permutation(self):
        func = Permutations().is_permutation1

        self.assertEqual(func(None, 'foo'), False)

        self.assertEqual(func('', 'foo'), False)

        self.assertEqual(func('Nib', 'bin'), False)

        self.assertEqual(func('act', 'cat'), True)

        self.assertEqual(func('a ct', 'ca t'), True)

        print('Success: test_permutation1')

    # def test_something(self):
    #     func = Permutations().is_permutation
    #     self.assertEqual(func(None, 'foo'), False)
    #
    #     self.assertEqual(func('', 'foo'), False)
    #
    #     self.assertEqual(func('Nib', 'bin'), False)
    #
    #     self.assertEqual(func('act', 'cat'), True)
    #
    #     self.assertEqual(func('a ct', 'ca t'), True)
    #
    #     print('Success: test_permutation')


if __name__ == '__main__':
    unittest.main()
