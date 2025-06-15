import random
import time
import psutil
import os

def get_memory_usage():
    """Get current memory usage in MB."""
    return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)

def calculate_conflicts(state):
    """Count attacking queen pairs."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(state[i] - state[j]):
                conflicts += 1
    return conflicts

def hill_climb(state):
    """Perform one hill climbing iteration."""
    n = len(state)
    current_conflicts = calculate_conflicts(state)
    
    for i in range(n):
        for j in range(i + 1, n):
            # Try swapping queens
            state[i], state[j] = state[j], state[i]
            new_conflicts = calculate_conflicts(state)
            
            if new_conflicts < current_conflicts:
                return state, True  # Found better move
            
            # Swap back
            state[i], state[j] = state[j], state[i]
    
    return state, False  # No improvement found

def solve_n_queens_greedy(n, max_restarts=100):
    """Solve N-Queens using greedy hill climbing."""
    start_time = time.time()
    best_state = []
    best_conflicts = n + 1
    
    for _ in range(max_restarts):
        # Random restart
        current_state = list(range(n))
        random.shuffle(current_state)
        
        # Hill climb until stuck
        while True:
            current_state, improved = hill_climb(current_state)
            current_conflicts = calculate_conflicts(current_state)
            
            if current_conflicts == 0:
                end_time = time.time()
                return current_state, 0, end_time - start_time, get_memory_usage()
            
            if not improved:
                break
        
        # Update best solution
        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_state = current_state[:]
    
    end_time = time.time()
    return best_state, best_conflicts, end_time - start_time, get_memory_usage()

def print_solution(state):
    """Print board from state representation."""
    if not state:
        print("No state to print.")
        return
    
    n = len(state)
    board = [['.' for _ in range(n)] for _ in range(n)]
    for row, col in enumerate(state):
        board[row][col] = 'Q'
    
    for row in board:
        print(" ".join(row))

# Main execution
if __name__ == '__main__':
    N = 200
    print(f"--- Solving N-Queens for N={N} with Greedy Search ---")
    
    final_state, final_conflicts, time_taken, memory_used = solve_n_queens_greedy(N, max_restarts=200)
    
    print("\nFinal Board State:")
    print_solution(final_state)
    
    print(f"\nNumber of conflicts: {final_conflicts}")
    if final_conflicts == 0:
        print("A solution was found!")
    else:
        print("No perfect solution found. The above is the best state achieved.")
    
    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Memory used: {memory_used:.4f} MB")