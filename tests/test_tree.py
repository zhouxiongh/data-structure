#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/2/11

""" 
Enter module description here
"""
import unittest

from tree import Bst, in_order_traversal, MinBst, Solution, Node


class TestBst(unittest.TestCase):
    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        results = []
        in_order_traversal(bst.root, results)
        self.assertEqual([1, 2, 3, 5, 8], results)

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        results = []
        in_order_traversal(bst.root, results)
        self.assertEqual([1, 2, 3, 4, 5], results)


class TestMinBst(unittest.TestCase):
    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        self.assertEqual(height(root), 4)
        print('Success: test_bst_min')


class TestBstSecondLargest(unittest.TestCase):

    def test_bst_second_largest(self):

        bst = Solution(None)

        self.assertRaises(TypeError, bst.find_second_largest)

        root = Node(10)

        bst = Solution(root)

        node5 = bst.insert(5)

        node15 = bst.insert(15)

        node3 = bst.insert(3)

        node8 = bst.insert(8)

        node12 = bst.insert(12)

        node20 = bst.insert(20)

        node2 = bst.insert(2)

        node4 = bst.insert(4)

        node30 = bst.insert(30)

        self.assertEqual(node20, bst.find_second_largest())

        root = Node(10)

        bst = Solution(root)

        node5 = bst.insert(5)

        node3 = bst.insert(3)

        node7 = bst.insert(7)

        self.assertEqual(node7, bst.find_second_largest())

        print('Success: test_bst_second_largest')


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


if __name__ == '__main__':
    unittest.main()
