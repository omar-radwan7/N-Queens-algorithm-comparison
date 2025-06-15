import random
import math
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

def should_accept(old_conflicts, new_conflicts, temperature):
    """Decide whether to accept a worse solution."""
    if new_conflicts < old_conflicts:
        return True
    if temperature <= 0:
        return False
    return random.random() < math.exp(-(new_conflicts - old_conflicts) / temperature)

def solve_n_queens_annealing(n, initial_temp=100.0, cooling_rate=0.995, max_iterations=50000):
    """Solve N-Queens using simulated annealing."""
    start_time = time.time()
    
    # Initialize random state
    current_state = list(range(n))
    random.shuffle(current_state)
    current_conflicts = calculate_conflicts(current_state)
    
    # Track best solution
    best_state = current_state[:]
    best_conflicts = current_conflicts
    temperature = initial_temp
    
    for iteration in range(max_iterations):
        if current_conflicts == 0:
            break
        
        # Generate neighbor by swapping two queens
        i, j = random.sample(range(n), 2)
        current_state[i], current_state[j] = current_state[j], current_state[i]
        new_conflicts = calculate_conflicts(current_state)
        
        # Accept or reject the move
        if should_accept(current_conflicts, new_conflicts, temperature):
            current_conflicts = new_conflicts
        else:
            # Revert the swap
            current_state[i], current_state[j] = current_state[j], current_state[i]
        
        # Update best solution
        if current_conflicts < best_conflicts:
            best_state = current_state[:]
            best_conflicts = current_conflicts
        
        # Cool down
        temperature *= cooling_rate
        if temperature < 1e-5:
            break
    
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
    N = 100
    print(f"--- Solving N-Queens for N={N} with Simulated Annealing ---")
    
    final_state, final_conflicts, time_taken, memory_used = solve_n_queens_annealing(N)
    
    print("\nFinal Board State:")
    print_solution(final_state)
    
    print(f"\nNumber of conflicts: {final_conflicts}")
    if final_conflicts == 0:
        print("A solution was found!")
    else:
        print("No perfect solution found. The above is the best state achieved.")
    
    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Memory used: {memory_used:.4f} MB")