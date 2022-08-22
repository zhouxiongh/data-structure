#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    disjoint-set.py
# @Author:      jason
# @Time:        2022/8/22 13:15

""" 
Disjoint-set data structure
"""


class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for _ in range(n + 1)]

    def find(self, u):
        """
        :param u:
        :return: parent of u
        if u's parent is u return u
        if u's parent is u father
        """
        while u != self._parents[u]:
            u = self._parents[self._parents[u]]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            pass
        if self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
            self._ranks[pu] += 1
        else:
            self._parents[pu] = pv
            self._ranks[pv] += 1
