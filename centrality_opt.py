# centrality_opt.py
"""
Optimized centrality functions:
- degree_centrality (unchanged)
- approximate_betweenness: adaptive k, memory-light per-source BFS,
  optional multiprocessing
"""

from collections import deque, defaultdict
import random
import math
import multiprocessing as mp

def degree_centrality(graph):
    return {n: graph.out_degree.get(n, 0) for n in graph.nodes}

def _single_source_betweenness(graph, s):
    """
    Single-source Brandes-like BFS accumulation.
    Returns partial betweenness contributions as dict node->value.
    """
    S = []
    P = defaultdict(list)
    sigma = defaultdict(float)
    dist = {}

    sigma[s] = 1.0
    dist[s] = 0
    Q = deque([s])

    while Q:
        v = Q.popleft()
        S.append(v)
        for w in graph.edges.get(v, []):
            if w not in dist:
                dist[w] = dist[v] + 1
                Q.append(w)
            if dist[w] == dist[v] + 1:
                sigma[w] += sigma[v]
                P[w].append(v)

    delta = defaultdict(float)
    contrib = defaultdict(float)
    while S:
        w = S.pop()
        for v in P[w]:
            coeff = (sigma[v] / sigma[w]) * (1.0 + delta[w])
            delta[v] += coeff
        if w != s:
            contrib[w] += delta[w]
    return contrib

def approximate_betweenness(graph, k=None, parallel=False):
    """
    Approximate betweenness centrality.
    - k: number of sample sources (default: adaptive based on graph size)
    - parallel: use multiprocessing to compute samples in parallel
    """
    N = len(graph.nodes)
    if N == 0:
        return {}

    if k is None:
        # adaptive: at least 20, or 1% of nodes, whichever larger, capped by N
        k = min(max(20, int(math.ceil(0.01 * N))), N)

    nodes = list(graph.nodes)
    sample_nodes = random.sample(nodes, k)

    betweenness = defaultdict(float)

    if parallel and k > 1:
        # worker map
        with mp.Pool() as pool:
            results = pool.map(lambda s: _single_source_betweenness(graph, s), sample_nodes)
        for partial in results:
            for v, val in partial.items():
                betweenness[v] += val
    else:
        for s in sample_nodes:
            partial = _single_source_betweenness(graph, s)
            for v, val in partial.items():
                betweenness[v] += val

    # scale by number of samples
    scale = 1.0 / k
    for v in betweenness:
        betweenness[v] *= scale

    return dict(betweenness)
