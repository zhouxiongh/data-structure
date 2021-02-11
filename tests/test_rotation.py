import unittest

from rotation import Rotation


class MyTestCase(unittest.TestCase):

    def test_rotation(self):
        func = Rotation().is_rotation
        self.assertEqual(func('foobarbaz', 'barbazfoo'), True)

        self.assertEqual(func('o', 'oo'), False)

        self.assertEqual(func(None, 'foo'), False)

        self.assertEqual(func('', 'foo'), False)

        self.assertEqual(func('', ''), True)



if __name__ == '__main__':
    unittest.main()
