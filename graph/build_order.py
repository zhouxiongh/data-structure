#!/usr/bin/env python
# -*- encoding=utf8 -*-
# Added by <zhouxiong.he@outlook.com>
# Added on 2021/10/21

""" 
Find a build order given a list of projects and dependencies.
"""

from graph.graph import Graph


class Dependency(object):
    def __init__(self, node_key_before, node_key_after):
        self.node_key_before = node_key_before
        self.node_key_after = node_key_after

class BuildOrder(object):
    def __init__(self, dependencies):
        self.dependencies = dependencies
        self.graph = Graph()
        self._build_graph()

    def _build_graph(self):
        for d in self.dependencies:
            self.graph.add_edge(d.node_key_before, d.node_key_after)

    def _find_start_nodes(self, processed_nodes):
        nodes_to_process = {}
        for k, n in self.graph.nodes.items():
            if n.incoming_edges == 0 and k not in processed_nodes:
                nodes_to_process[k] = n
        return nodes_to_process

    @staticmethod
    def _process_nodes(nodes_to_process, processed_nodes):
        for node in nodes_to_process.values():
            for adj_node in list(node.adj_nodes.values()):
                node.remove_neighbor(adj_node)
            processed_nodes[node.key] = node

    def find_build_order(self):
        result = []
        process_nodes = {}
        while len(result) != len(self.graph.nodes):
            nodes_to_process = self._find_start_nodes(process_nodes)
            if not nodes_to_process:
                return None
            result.extend(nodes_to_process.values())
            self._process_nodes(nodes_to_process, process_nodes)
        return result

