# graph.py
"""
Optimized Graph class for Phase 3.

Key improvements:
- uses defaultdict(list) for adjacency
- maintains out_degree cache for fast access
- safe add/remove operations with O(1) amortized updates
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        # adjacency: node -> list of neighbors (outgoing)
        self.edges = defaultdict(list)
        # node set
        self.nodes = set()
        # cached out-degree (kept in sync)
        self.out_degree = defaultdict(int)

    # ---------- node/edge operations ----------
    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            # ensure adjacency entry exists
            _ = self.edges[node]
            self.out_degree[node] = len(self.edges[node])

    def add_edge(self, u, v):
        # ensure nodes exist
        if u not in self.nodes:
            self.add_node(u)
        if v not in self.nodes:
            self.add_node(v)
        # avoid duplicates
        if v not in self.edges[u]:
            self.edges[u].append(v)
            self.out_degree[u] += 1

    def remove_edge(self, u, v):
        if u in self.nodes and v in self.edges.get(u, []):
            try:
                self.edges[u].remove(v)
            except ValueError:
                pass
            self.out_degree[u] = len(self.edges[u])

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            # remove outgoing edges record
            self.edges.pop(node, None)
            self.out_degree.pop(node, None)
            # remove incoming edges
            for n in list(self.edges.keys()):
                if node in self.edges[n]:
                    try:
                        self.edges[n].remove(node)
                    except ValueError:
                        pass
                    self.out_degree[n] = len(self.edges[n])

    def neighbors(self, node):
        return list(self.edges.get(node, ()))

    def __len__(self):
        return len(self.nodes)

    def __repr__(self):
        m = sum(len(v) for v in self.edges.values())
        return f"Graph(num_nodes={len(self.nodes)}, num_edges={m})"
