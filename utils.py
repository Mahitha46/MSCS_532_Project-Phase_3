# utils.py
from graph import Graph

def build_sample_graph():
    """Small sample graph used for quick tests."""
    G = Graph()
    edges = [
        ("Alice", "Bob"),
        ("Alice", "Charlie"),
        ("Bob", "Charlie"),
        ("Charlie", "Alice"),
        ("Bob", "Eve"),
        ("Eve", "Frank"),
        ("Frank", "Charlie"),
        ("Charlie", "Eve"),
    ]
    for u, v in edges:
        G.add_edge(u, v)
    return G

def build_random_er(n, p, seed=None):
    """Generate an Erdős–Rényi random directed graph."""
    import random
    if seed is not None:
        random.seed(seed)
    G = Graph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:
                G.add_edge(i, j)
    return G

def build_powerlaw_graph(n, avg_deg=4, seed=None):
    """Simple power-law-like generator (not perfect) for testing."""
    import random
    if seed is not None:
        random.seed(seed)
    G = Graph()
    for i in range(n):
        G.add_node(i)
    # preferential attachment-like: nodes pick neighbors with prob proportional to degree+1
    for i in range(1, n):
        targets = set()
        while len(targets) < min(avg_deg, i):
            # roulette wheel on existing nodes
            weights = [G.out_degree.get(j, 0) + 1 for j in range(i)]
            total = sum(weights)
            r = random.uniform(0, total)
            cum = 0.0
            for j, w in enumerate(weights):
                cum += w
                if r <= cum:
                    targets.add(j)
                    break
        for t in targets:
            G.add_edge(i, t)
    return G
