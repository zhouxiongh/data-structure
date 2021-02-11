#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/2/11

""" 
Enter module description here
"""
import unittest

from tree import Bst, in_order_traversal, MinBst


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


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


if __name__ == '__main__':
    unittest.main()
