#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/10/21

"""
unit test for Build order
"""
import unittest

from nose.tools import assert_true

from graph.build_order import Dependency, BuildOrder


class TestBuildOrder:
    def __init__(self):
        self.dependencies = [
            Dependency('d', 'g'),
            Dependency('f', 'c'),
            Dependency('f', 'b'),
            Dependency('f', 'a'),
            Dependency('c', 'a'),
            Dependency('b', 'a'),
            Dependency('a', 'e'),
            Dependency('b', 'e'),
        ]

    def test_build_order(self):
        build_order = BuildOrder(self.dependencies)

        processed_nodes = build_order.find_build_order()

        expected_result0 = ('d', 'f')

        expected_result1 = ('c', 'b', 'g')

        assert_true(processed_nodes[0].key in expected_result0)
        assert_true(processed_nodes[1].key in expected_result0)
        assert_true(processed_nodes[2].key in expected_result1)
        assert_true(processed_nodes[3].key in expected_result1)
        assert_true(processed_nodes[4].key in expected_result1)
        assert_true(processed_nodes[5].key is 'a')
        assert_true(processed_nodes[6].key is 'e')

        print('Success: test_build_order')

    def test_build_order_circular(self):
        self.dependencies.append(Dependency('e', 'f'))

        build_order = BuildOrder(self.dependencies)
        processed_nodes = build_order.find_build_order()
        assert_true(processed_nodes is None)

        print('Success: test_build_order_circular')


if __name__ == '__main__':
    unittest.main()
