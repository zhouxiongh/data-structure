import unittest
from compress import CompressString


class MyTestCase(unittest.TestCase):
    def test_something(self):
        func = CompressString().compress
        self.assertEqual(func(None), None)

        self.assertEqual(func(''), '')

        self.assertEqual(func('AABBCC'), 'AABBCC')

        self.assertEqual(func('AAABCCDDDDE'), 'A3BC2D4E')

        self.assertEqual(func('BAAACCDDDD'), 'BA3C2D4')

        self.assertEqual(func('AAABAACCDDDD'), 'A3BA2C2D4')

        print('Success: test_compress')
        # self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
