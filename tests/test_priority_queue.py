import unittest

from priority_queue import PriorityQueue, QueueNode


class MyTestCase(unittest.TestCase):

    def test_something(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)

        priority_queue.insert(QueueNode('a', 20))

        priority_queue.insert(QueueNode('b', 5))

        priority_queue.insert(QueueNode('c', 15))

        priority_queue.insert(QueueNode('d', 22))

        priority_queue.insert(QueueNode('e', 40))

        priority_queue.insert(QueueNode('f', 3))

        priority_queue.decrease_key('f', 2)

        priority_queue.decrease_key('a', 19)

        mins = []
        print(priority_queue.array)
        while priority_queue.array:

            mins.append(priority_queue.extract_min().key)

        self.assertEqual([2, 5, 15, 19, 22, 40], mins)

        print('Success: test_min_heap')


if __name__ == '__main__':
    unittest.main()
