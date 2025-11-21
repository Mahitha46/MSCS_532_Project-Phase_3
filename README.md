Phase 3: Optimization, Scaling, and Final Evaluation

Project Overview

This repository contains the Phase 3 implementation of the Social Network Influence Analysis system.
Phase 3 builds on the design (Phase 1) and proof-of-concept implementation (Phase 2) by:

Optimizing the underlying data structures and algorithms

Scaling the system to support large datasets

Evaluating performance improvements through testing and profiling

Finalizing a robust, modular, and scalable analysis pipeline

This implementation simulates social network influence metrics using:

PageRank

Degree Centrality

Approximate Betweenness Centrality

What’s New in Phase 3?

1. Optimized Data Structures

Replaced standard adjacency lists with defaultdict(list)

Added out-degree caching for O(1) access during PageRank

Reduced memory usage in betweenness via lightweight containers

Memoized partial BFS structures for repeated source nodes

2. Algorithmic Enhancements

Re-designed PageRank loop to reduce Python overhead

Improved treatment of dangling nodes

Adaptive sampling in approximate betweenness (k = max(20, 0.01 * N))

3. Improved Scalability

Successfully tested on synthetic graphs up to 10,000+ nodes

Introduced scalable random graph generators:

Erdős–Rényi (ER)

Power-law style networks

Reduced BFS path memory by early cleanup

4. Advanced Testing & Validation

Benchmarks comparing Phase 2 vs Phase 3

Stress tests on large sparse and dense graphs

Correctness verification using NetworkX equivalents

Repository Structure

Project_Phase_3


├── graph.py                # Optimized graph structure with out-degree caching

├── pagerank_opt.py         # Improved PageRank with reduced overhead

├── centrality_opt.py       # Adaptive betweenness + degree centrality

├── utils.py                # Sample graph & large graph generators

├── visualize.py            # Improved visualization

├── main.py                 # Demo runner & benchmarking


└── README.md               # Instructions and Project Summary

Key Algorithms

PageRank (Optimized)

One-pass accumulation

Uses cached out-degree values

Computes dangling mass once per iteration

Early stopping with L1 threshold

Approximate Betweenness (Optimized)

BFS with minimal overhead

Sampling adapts to graph size

Optional multiprocessing parallelism

Memory-efficient path recording

How to Run

1. Install Requirements

pip install matplotlib networkx

3. Run the Phase 3 Demo
   
python main.py


This performs:

PageRank computation

Approximate betweenness

Degree centrality

Visualization

Timing benchmarks
