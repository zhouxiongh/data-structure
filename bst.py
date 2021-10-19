#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/2/11

""" 
Enter module description here
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)


class MinBst:
    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array) - 1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid - 1)
        node.right = self._create_min_bst(array, mid + 1, end)
        return node


def in_order_traversal(node, result):
    if node is None:
        return result
    in_order_traversal(node.left, result)
    result.append(node.data)
    in_order_traversal(node.right, result)


class Solution(Bst):
    def _find_second_largest(self, node):
        if node.right is not None:
            if node.right.left is not None or node.right.right is not None:
                return self._find_second_largest(node.right)
            else:
                return node
        else:
            return self._find_right_most_node(node.left)

    def _find_right_most_node(self, node):
        if node.right is not None:
            return self._find_right_most_node(node.right)
        else:
            return node

    def find_second_largest(self):
        if self.root is None:
            raise TypeError('root cannot be None')
        if self.root.left is None and self.root.right is None:
            raise ValueError('root must have at least one child')
        return self._find_second_largest(self.root)


class BstSuccessor:

    def get_next(self, node):
        if node is None:
            raise TypeError('node cannot be none')
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancestor(node)

    @staticmethod
    def _left_most(node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.data

    def _next_ancestor(self, node):
        if node.parent is not None:
            if node.parent.data > node.data:
                return node.parent.data
            else:
                return self._next_ancestor(node.parent)
        return None

