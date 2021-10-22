#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    trie.py
# @Author:      jason
# @Time:        2021/10/22 15:53

""" 
Enter module description here
"""


class Node:
    def __init__(self, key, parent=None, terminates=False):
        self.key = key
        self.terminates = terminates
        self.parent = parent
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node('')

    def find(self, word):
        if word is None:
            raise TypeError("word cannot be None")
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node if node.terminates else None

    def insert(self, word):
        if word is None:
            raise TypeError("word cannot be None")
        node = self.root
        # parent = None
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node(char, parent=node)
                node = node.children[char]
        node.terminates = True

    def remove(self, word):
        if word is None:
            raise TypeError("word cannot be None")
        node = self.find(word)
        if node is None:
            raise TypeError("word does not exist")
        node.terminates = False
        parent = node.parent
        while parent is not None:
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = node.parent

    def list_words(self):
        result = []
        self._list_words(self.root, '', result)
        return result

    def _list_words(self, node, cur_word, result):
        """
        dfs
        :return:
        """
        if not node:
            return
        for key, child in node.children.items():
            if child.terminates:
                result.append(cur_word+key)
            self._list_words(child, cur_word+key, result)
