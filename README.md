# 🧩 Comparative Analysis of N-Queens Problem Solutions

This repository presents a research-based comparison of multiple algorithmic strategies for solving the classic N-Queens problem — a benchmark in artificial intelligence and combinatorial optimization.

## 📘 Abstract
The N-Queens problem challenges algorithms to place N queens on an N×N chessboard such that no two queens threaten each other. Our study compares four methods:

- ✅ Depth-First Search (DFS)
- 🔥 Simulated Annealing
- 🧬 Genetic Algorithm
- ⚡ Greedy Hill Climbing

We evaluate each approach based on **solution quality**, **execution time**, and **memory usage**. While DFS guarantees perfect solutions for smaller N (≤30), metaheuristic algorithms scale up to N=200 effectively — with the Genetic Algorithm achieving zero-conflict configurations in 78% of trials.

## 📊 Results Snapshot

| Algorithm           | Max N Solved | Avg. Time (s) | Success Rate |
|---------------------|--------------|---------------|--------------|
| DFS                 | 30           | 142.7         | 100%         |
| Simulated Annealing | 100          | 29.1          | 92%          |
| Genetic Algorithm   | 200          | 68.4          | 78%          |

> 📌 Implemented in **Python 3.9** and benchmarked on Intel i7 / 8GB RAM.

## 📁 Repository Structure
- `dfs_nqueens.py` — Exhaustive DFS implementation
- `annealing_nqueens.py` — Simulated Annealing strategy
- `genetic_nqueens.py` — Evolutionary optimization
- `report/` — IEEE-style LaTeX paper with charts
- `images/` — Plots and board configurations

---

