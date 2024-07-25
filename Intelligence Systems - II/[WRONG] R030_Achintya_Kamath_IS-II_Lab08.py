import random

# Parameters
POPULATION_SIZE = 100
CHROMOSOME_LENGTH = 12
MUTATION_RATE = 0.01
NUM_GENERATIONS = 100

# Defining the fitness function
def fitness_function(chromosome):
    return sum(chromosome)

# Generating the initial population
def generate_population(size, length):
    return [[random.randint(0, 256) for something in range(length)] for something in range(size)]

# Crossover operation
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation operation
def mutate(chromosome):
    for i in range(len(chromosome)):
        if random.random() < MUTATION_RATE:
            chromosome[i] = 1 - chromosome[i]  # Fliping the bit
    return chromosome

def genetic_algorithm():
    # Initializing the population
    population = generate_population(POPULATION_SIZE, CHROMOSOME_LENGTH)

    for generation in range(NUM_GENERATIONS):
        # Evaluating fitness of each individual in the population
        fitness_scores = [fitness_function(chromosome) for chromosome in population]

        # Selecting parents based on fitness scores
        parents = []
        for _ in range(POPULATION_SIZE // 2):
            idx1, idx2 = random.sample(range(POPULATION_SIZE), 2)
            parent1 = population[idx1] if fitness_scores[idx1] > fitness_scores[idx2] else population[idx2]
            idx1, idx2 = random.sample(range(POPULATION_SIZE), 2)
            parent2 = population[idx1] if fitness_scores[idx1] > fitness_scores[idx2] else population[idx2]
            parents.append((parent1, parent2))

        # Creating offsprings via crossover
        offspring = []
        for parent1, parent2 in parents:
            child1, child2 = crossover(parent1, parent2)
            offspring.append(mutate(child1))
            offspring.append(mutate(child2))

        # Replacing the population with the offspring
        population = offspring

    # Returning the best individual from the final population
    best_individual = max(population, key=fitness_function)
    return best_individual

best_solution = genetic_algorithm()
print("Best solution:", best_solution)
print("Fitness:", fitness_function(best_solution))
