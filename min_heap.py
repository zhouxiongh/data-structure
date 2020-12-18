from __future__ import division
import sys


class MinHeap(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array) == 1:
            return self.array.pop(0)
        minimum = self.array[0]
        # done: Move the last element to the root
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index=0)
        return minimum

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        if key is None:
            raise TypeError("key can not be None")
        self.array.append(key)
        # done: Move new key if necessary
        self._bubble_up(len(self.array) - 1)

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = (index - 1) // 2
        if self.array[index] < self.array[index_parent]:
            self.array[index], self.array[index_parent] = \
                self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)
        return

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            self.array[index], self.array[min_child_index] = \
                self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _find_smaller_child(self, index):
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        # No right child
        if right_child_index >= len(self.array):
            # No child
            if left_child_index >= len(self.array):
                return -1
            return left_child_index
        else:
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index
