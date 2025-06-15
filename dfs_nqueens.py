import time
import psutil
import os

def get_memory_usage():
    """Get current memory usage in MB."""
    return psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)

def is_safe(board, row, col, n):
    """Check if queen placement is safe."""
    # Check row and diagonals
    for i in range(col):
        if (board[row][i] == 'Q' or 
            (row - i >= 0 and board[row - i][col - i] == 'Q') or
            (row + i < n and board[row + i][col - i] == 'Q')):
            return False
    return True

def solve_dfs(board, col, n):
    """Recursive DFS solver."""
    if col == n:
        return True
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            if solve_dfs(board, col + 1, n):
                return True
            board[row][col] = '.'
    return False

def solve_n_queens_dfs(n):
    """Solve N-Queens using DFS backtracking."""
    start_time = time.time()
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    success = solve_dfs(board, 0, n)
    
    end_time = time.time()
    memory = get_memory_usage()
    
    if success:
        return board, 0, end_time - start_time, memory
    else:
        return None, -1, end_time - start_time, memory

def print_solution(board):
    """Print the board solution."""
    if board:
        for row in board:
            print(" ".join(row))
    else:
        print("No solution found.")

# Main execution
if __name__ == '__main__':
    N = 30
    print(f"--- Solving N-Queens for N={N} with Exhaustive Search (DFS) ---")
    
    solution_board, conflicts, time_taken, memory_used = solve_n_queens_dfs(N)
    
    print("\nBoard:")
    print_solution(solution_board)
    
    if conflicts != -1:
        print(f"\nNumber of conflicts: {conflicts}")
        print("A solution was found!")
    else:
        print("\nNo solution exists for this N.")
    
    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Memory used: {memory_used:.4f} MB")