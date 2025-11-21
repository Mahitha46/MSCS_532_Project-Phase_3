# main.py
"""
Driver script to run demonstrations and basic benchmarking for Phase 3.
"""

import time
from utils import build_sample_graph, build_random_er, build_powerlaw_graph
from centrality_opt import degree_centrality, approximate_betweenness
from pagerank_opt import pagerank
from visualize import draw_graph

def quick_demo():
    G = build_sample_graph()
    print("Graph:", G)

    print("\nDegree centrality:")
    dc = degree_centrality(G)
    print(dc)

    print("\nPageRank:")
    t0 = time.time()
    pr = pagerank(G, damping=0.85, max_iter=200, tol=1e-6, verbose=True)
    t1 = time.time()
    print("PageRank (time {:.4f}s):".format(t1 - t0))
    print(pr)

    print("\nApproximate betweenness (k adaptive):")
    t0 = time.time()
    ab = approximate_betweenness(G, k=None, parallel=False)
    t1 = time.time()
    print("Approx Betweenness (time {:.4f}s):".format(t1 - t0))
    print(ab)

    draw_graph(G, metric_dict=pr, title="Sample Graph - PageRank")

def benchmark_sizes():
    sizes = [100, 1000, 5000]  # scale as needed
    for n in sizes:
        print(f"\n=== Benchmark: n={n} (powerlaw) ===")
        G = build_powerlaw_graph(n, avg_deg=3, seed=42)
        print(G)
        t0 = time.time()
        pr = pagerank(G, max_iter=200, tol=1e-5)
        t1 = time.time()
        print(f"PageRank time: {t1-t0:.4f}s (n={n})")

        t0 = time.time()
        ab = approximate_betweenness(G, k=max(20, int(0.01*n)))
        t1 = time.time()
        print(f"Approx Betweenness time: {t1-t0:.4f}s (n={n})")

if __name__ == "__main__":
    quick_demo()
    # benchmark_sizes()
