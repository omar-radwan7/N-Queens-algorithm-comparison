# Comparative Analysis of N-Queens Problem Solutions

A research-based comparison of multiple algorithmic strategies for solving the classic N-Queens problem — a benchmark in artificial intelligence and combinatorial optimization.

---

## Abstract

The N-Queens problem challenges algorithms to place N queens on an N×N chessboard such that no two queens threaten each other. This study compares four methods:

- Depth-First Search (DFS)
- Simulated Annealing
- Genetic Algorithm
- Greedy Hill Climbing

Each approach is evaluated on **solution quality**, **execution time**, and **memory usage**. While DFS guarantees perfect solutions for smaller N (≤30), metaheuristic algorithms scale up to N=200 effectively — with the Genetic Algorithm achieving zero-conflict configurations in 78% of trials.

---

## Results

| Algorithm | Max N Solved | Avg. Time (s) | Success Rate |
|---|---|---|---|
| DFS | 30 | 142.7 | 100% |
| Simulated Annealing | 100 | 29.1 | 92% |
| Genetic Algorithm | 200 | 68.4 | 78% |

Benchmarked on Intel i7 / 8GB RAM using Python 3.9.

---

## Key Findings

- **DFS** guarantees an exact solution but becomes computationally infeasible beyond N=30 due to exponential search space growth
- **Simulated Annealing** offers the best balance of speed and reliability — 92% success rate up to N=100 in under 30 seconds on average
- **Genetic Algorithm** scales furthest, solving up to N=200, but at the cost of higher runtime and a lower success rate
- **Greedy Hill Climbing** is the fastest but most prone to local optima — suitable only for approximate solutions at smaller scales

---

## Repository Structure

```
N-Queens-algorithm-comparison/
├── dfs_nqueens.py        # Exhaustive DFS implementation
├── annealing_nqueens.py  # Simulated Annealing strategy
├── genetic_nqueens.py    # Evolutionary optimization
├── report/               # IEEE-style LaTeX paper with charts
└── images/               # Plots and board configuration visualizations
```

---

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
git clone https://github.com/omar-radwan7/N-Queens-algorithm-comparison.git
cd N-Queens-algorithm-comparison
pip install -r requirements.txt
```

### Run an Algorithm

```bash
# DFS
python dfs_nqueens.py

# Simulated Annealing
python annealing_nqueens.py

# Genetic Algorithm
python genetic_nqueens.py
```

---

## License

MIT License
