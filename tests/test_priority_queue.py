import unittest

from priority_queue import PriorityQueue, PriorityQueueNode


class MyTestCase(unittest.TestCase):

    def test_something(self):
        priority_queue = PriorityQueue()
        self.assertEqual(priority_queue.extract_min(), None)

        priority_queue.insert(PriorityQueueNode('a', 20))

        priority_queue.insert(PriorityQueueNode('b', 5))

        priority_queue.insert(PriorityQueueNode('c', 15))

        priority_queue.insert(PriorityQueueNode('d', 22))

        priority_queue.insert(PriorityQueueNode('e', 40))

        priority_queue.insert(PriorityQueueNode('f', 3))

        priority_queue.decrease_key('f', 2)

        priority_queue.decrease_key('a', 19)

        mins = []

        while priority_queue.array:

            mins.append(priority_queue.extract_min().key)

        self.assertEqual(mins, [2, 5, 15, 19, 22, 40])

        print('Success: test_min_heap')


if __name__ == '__main__':
    unittest.main()
