'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 08
Date: 13/03/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 08 \n Date: 13/03/2024")

print("\n ############# ################ ####################\n")

print(" Task 1: Basic Genetic Algorithm.")

print("\n ############# ################ ####################\n")

import random

# Function to generate initial population
def generate_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

# Fitness function (Example: Counting the number of ones in the chromosome)
def fitness(chromosome):
    return sum(chromosome)

# Function to perform selection (Tournament Selection)
def tournament_selection(population, fitness_values, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected_parents.append(winner)
    return selected_parents

# Function to perform crossover (Single Point Crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to perform mutation
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip the bit
    return chromosome

# Genetic Algorithm
def genetic_algorithm(population_size, chromosome_length, generations, tournament_size, mutation_rate):
    population = generate_population(population_size, chromosome_length)

    for _ in range(generations):
        # Evaluate fitness of each individual in the population
        fitness_values = [fitness(chromosome) for chromosome in population]

        # Select parents using tournament selection
        selected_parents = tournament_selection(population, fitness_values, tournament_size)

        # Create next generation through crossover and mutation
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected_parents, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            next_generation.extend([child1, child2])

        # Replace the old population with the new generation
        population = next_generation[:population_size]

    # Return the best individual
    best_individual = max(population, key=fitness)
    return best_individual

# Example usage
population_size = 100
chromosome_length = 10
generations = 100
tournament_size = 5
mutation_rate = 0.05

best_solution = genetic_algorithm(population_size, chromosome_length, generations, tournament_size, mutation_rate)

print(" Best solution found:", best_solution)
print(" Fitness:", fitness(best_solution), "\n")

# Confusedly Crafted by Redzwinger #


