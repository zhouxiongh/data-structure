import unittest

from unique_chars import UniqueChars


class MyTestCase(unittest.TestCase):

    def test_something(self):
        # self.assertEqual(True, False)
        func = UniqueChars().has_unique_chars
        self.assertEqual(func(None), False)
        self.assertEqual(func(''), True)
        self.assertEqual(func('foo'), False)
        self.assertEqual(func('bar'), True)
        print('Success')


if __name__ == '__main__':
    unittest.main()
