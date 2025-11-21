# pagerank_opt.py
"""
Optimized PageRank implementation (Phase 3).

Improvements:
- uses out_degree cache from Graph
- single pass accumulation with dangling mass computed once per iteration
- early stopping on L1 diff
- returns dict: node -> rank
"""

def pagerank(graph, damping=0.85, max_iter=100, tol=1.0e-6, verbose=False):
    nodes = list(graph.nodes)
    N = len(nodes)
    if N == 0:
        return {}

    # initial uniform rank
    rank = {n: 1.0 / N for n in nodes}
    base = (1.0 - damping) / N

    for it in range(max_iter):
        new_rank = {n: base for n in nodes}

        # compute total dangling mass
        dangling_sum = 0.0
        for n in nodes:
            if graph.out_degree.get(n, 0) == 0:
                dangling_sum += rank[n]

        # distribute non-dangling contributions
        # accumulate contributions locally to reduce repeated dict writes
        contribs = {}
        for n in nodes:
            out_deg = graph.out_degree.get(n, 0)
            if out_deg == 0:
                continue
            share = rank[n] / out_deg
            for nbr in graph.edges[n]:
                contribs[nbr] = contribs.get(nbr, 0.0) + share

        # apply contributions
        for n, v in contribs.items():
            new_rank[n] += damping * v

        # apply dangling mass uniformly
        if dangling_sum > 0.0:
            add = damping * dangling_sum / N
            for n in nodes:
                new_rank[n] += add

        # finalize: apply teleport/base already added
        diff = sum(abs(new_rank[n] - rank[n]) for n in nodes)
        if verbose:
            print(f"[PageRank] iter={it+1}, diff={diff:.6e}")
        rank = new_rank
        if diff < tol:
            break

    return rank
