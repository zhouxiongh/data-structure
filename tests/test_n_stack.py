import unittest

from n_stack import NStacks


class MyTestCase(unittest.TestCase):
    num_stacks = 3
    stack_size = 100

    def test_pop_on_empty(self):
        stacks = NStacks(self.num_stacks, self.stack_size)
        with self.assertRaises(Exception):
            stacks.pop(0)

    def test_push_on_full(self):
        stacks = NStacks(self.num_stacks, self.stack_size)
        for i in range(0, self.stack_size):
            stacks.push(2, i)
        with self.assertRaises(Exception):
            stacks.push(2, self.stack_size)

    def test_stacks(self):
        stacks = NStacks(self.num_stacks, self.stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')

        self.assertEqual(stacks.pop(0), 2)
        self.assertEqual(stacks.pop(0), 1)
        self.assertEqual(stacks.pop(1), 3)
        self.assertEqual(stacks.pop(2), 4)

        print('Success: test_stacks\n')


if __name__ == '__main__':
    unittest.main()
