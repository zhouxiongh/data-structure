#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/10/21

"""
Graph implementation
"""
from enum import Enum
from collections import deque


class State(Enum):
    unvisited = 0
    visiting = 1
    visited = 2


class Node:
    def __init__(self, key):
        self.key = key
        self.visit_state = State.unvisited
        self.incoming_edges = 0
        self.adj_nodes = {}
        self.adj_weights = {}

    def __repr__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    def add_neighbor(self, neighbor, weight=0):
        if neighbor is None or weight is None:
            raise TypeError("neighbor or weight cannot be None")
        neighbor.incoming_edges += 1
        self.adj_weights[neighbor.key] = weight
        self.adj_nodes[neighbor.key] = neighbor

    def remove_neighbor(self, neighbor):
        if neighbor is None:
            raise TypeError("neighbor cannot be None")
        if neighbor.key not in self.adj_nodes:
            raise KeyError("neighbor not found")
        neighbor.incoming_edges -= 1
        del self.adj_weights[neighbor.key]
        del self.adj_nodes[neighbor.key]


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError("key cannot be None")
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight):
        if source_key is None or dest_key is None:
            raise KeyError("Invalid key")
        if source_key not in self.nodes:
            self.nodes[source_key] = Node(source_key)
        if dest_key not in self.nodes:
            self.nodes[dest_key] = Node(dest_key)
        self.nodes[source_key].add_neighbor(self.nodes[dest_key], weight)

    def add_undirected_edge(self, source_key, dest_key, weight):
        if source_key is None or dest_key is None:
            raise KeyError("Invalid key")
        self.add_edge(source_key, dest_key, weight)
        self.add_edge(dest_key, source_key, weight)

    @staticmethod
    def bfs(root, visit_func):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        root.visit_state = State.visited
        while queue:
            node = queue.popleft()
            visit_func(node)
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited

