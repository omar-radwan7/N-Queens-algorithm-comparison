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

def calculate_fitness(state, max_fitness):
    """Calculate fitness (higher is better)."""
    return max_fitness - calculate_conflicts(state)

def create_individual(n):
    """Create a random individual."""
    individual = list(range(n))
    random.shuffle(individual)
    return individual

def tournament_selection(population, fitness_scores, tournament_size=3):
    """Select parent using tournament selection."""
    candidates = random.sample(list(zip(population, fitness_scores)), tournament_size)
    return max(candidates, key=lambda x: x[1])[0]

def crossover(parent1, parent2):
    """Create two children using order crossover."""
    n = len(parent1)
    point = random.randint(1, n - 1)
    
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    
    return repair_individual(child1), repair_individual(child2)

def repair_individual(individual):
    """Fix duplicate values in individual."""
    n = len(individual)
    seen = set()
    missing = set(range(n))
    
    # Find duplicates and missing values
    for i, val in enumerate(individual):
        if val in seen:
            individual[i] = None  # Mark for replacement
        else:
            seen.add(val)
            missing.discard(val)
    
    # Replace duplicates with missing values
    missing = list(missing)
    for i in range(n):
        if individual[i] is None:
            individual[i] = missing.pop()
    
    return individual

def mutate(individual):
    """Swap two random positions."""
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

def solve_n_queens_genetic(n, population_size=100, generations=1000, mutation_rate=0.1):
    """Solve N-Queens using genetic algorithm."""
    start_time = time.time()
    max_fitness = n * (n - 1) // 2
    
    # Initialize population
    population = [create_individual(n) for _ in range(population_size)]
    
    best_individual = None
    best_fitness = -1
    
    for generation in range(generations):
        # Calculate fitness for all individuals
        fitness_scores = [calculate_fitness(ind, max_fitness) for ind in population]
        
        # Check for perfect solution
        max_current_fitness = max(fitness_scores)
        if max_current_fitness == max_fitness:
            best_idx = fitness_scores.index(max_current_fitness)
            end_time = time.time()
            return population[best_idx], 0, end_time - start_time, get_memory_usage()
        
        # Update best solution
        if max_current_fitness > best_fitness:
            best_fitness = max_current_fitness
            best_individual = population[fitness_scores.index(max_current_fitness)][:]
        
        # Create new generation
        new_population = []
        
        for _ in range(population_size // 2):
            # Select parents
            parent1 = tournament_selection(population, fitness_scores)
            parent2 = tournament_selection(population, fitness_scores)
            
            # Create children
            child1, child2 = crossover(parent1, parent2)
            
            # Apply mutation
            if random.random() < mutation_rate:
                child1 = mutate(child1)
            if random.random() < mutation_rate:
                child2 = mutate(child2)
            
            new_population.extend([child1, child2])
        
        # Handle odd population size
        if len(new_population) < population_size:
            new_population.append(create_individual(n))
        
        population = new_population[:population_size]
    
    end_time = time.time()
    final_conflicts = max_fitness - best_fitness
    return best_individual, final_conflicts, end_time - start_time, get_memory_usage()

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
    print(f"--- Solving N-Queens for N={N} with a Genetic Algorithm ---")
    
    final_state, final_conflicts, time_taken, memory_used = solve_n_queens_genetic(N)
    
    print("\nFinal Board State:")
    print_solution(final_state)
    
    print(f"\nNumber of conflicts: {final_conflicts}")
    if final_conflicts == 0:
        print("A solution was found!")
    else:
        print("No perfect solution found. The above is the best state achieved.")
    
    print(f"Time taken: {time_taken:.6f} seconds")
    print(f"Memory used: {memory_used:.4f} MB")