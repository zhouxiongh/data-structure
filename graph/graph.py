#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/10/21

"""
Graph implementation
"""
import sys
from enum import Enum
from collections import deque

from priority_queue import PriorityQueueNode, PriorityQueue


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
    def init(self):
        for key in self.nodes.keys():
            # Set each node's previous node key to None
            # Set each node's shortest path weight to infinity
            # Add each node's shortest path weight to the priority queue
            self.previous[key] = None
            self.path_weight[key] = sys.maxsize
            self.remaining.insert(PriorityQueueNode(key, self.path_weight[key]))

    def __init__(self):
        self.remaining = PriorityQueue()  # Queue of node key, path weight
        self.path_weight = {}  # Key: node key, val: weight, shortest path
        self.previous = {}  # Key: node key, val: prev node key, shortest path
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            raise TypeError("key cannot be None")
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, source_key, dest_key, weight=0):
        if source_key is None or dest_key is None:
            raise KeyError("Invalid key")
        if source_key not in self.nodes:
            self.add_node(source_key)
        if dest_key not in self.nodes:
            self.add_node(dest_key)
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

    def dfs(self, root, visit_func):
        if root is None:
            return
        visit_func(root)
        root.visit_state = State.visited
        for node in root.adj_nodes.values():
            if node.visit_state == State.unvisited:
                self.dfs(node, visit_func)

    @staticmethod
    def path_exists(start, end):
        """
        bfs from start to end
        :param start: Node
        :param end: Node
        :return: True or False
        """
        if start is None or end is None:
            return False
        if start is end:
            return True
        queue = deque()
        queue.append(start)
        start.visit_state = State.visited
        while queue:
            node = queue.popleft()
            if node is end:
                return True
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    adj_node.visit_state = State.visited
        return False

    def find_shortest_path(self, start, end):
        if start is None or end is None:
            raise TypeError('Input node keys cannot be None')
        if start not in self.nodes or end not in self.nodes:
            raise ValueError('Invalid start or end node key')
        self.init()
        self.path_weight[start] = 0
        self.remaining.decrease_key(start, 0)
        while self.remaining:
            # Extract the min node (node with minimum path weight)
            # from the priority queue
            min_node_key = self.remaining.extract_min().obj
            min_node = self.nodes[min_node_key]
            # Loop through each adjacent node in the min node
            for adj_key in min_node.adj_nodes.keys():
                # Node's path:
                # Adjacent node's edge weight + the min node's
                # shortest path weight
                new_weight = (min_node.adj_weights[adj_key] +
                              self.path_weight[min_node_key])
                # Only update if the newly calculated path is
                # less than the existing node's shortest path
                if self.path_weight[adj_key] > new_weight:
                    # Set the node's previous node key leading to the shortest path
                    # Update the adjacent node's shortest path and
                    # update the value in the priority queue
                    self.previous[adj_key] = min_node_key
                    self.path_weight[adj_key] = new_weight
                    self.remaining.decrease_key(adj_key, new_weight)
        result = []
        current_key = end
        while current_key is not None:
            result.append(current_key)
            current_key = self.previous[current_key]
        return result[::-1]
