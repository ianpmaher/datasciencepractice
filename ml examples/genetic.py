# To make the algorithm more efficient, we can move away from pure brute force and incorporate some more intelligent guessing strategies. One such strategy is the genetic algorithm, which is inspired by the process of natural selection. Here's a basic outline of how a genetic algorithm can be used to guess a 7-digit number:

# Genetic Algorithm Steps:
# Initialization: Create an initial population of random guesses.
# Evaluation: Evaluate each guess by comparing it to the secret number and assigning a fitness score based on how many digits are correct.
# Selection: Select the best guesses to be parents for the next generation.
# Crossover: Combine pairs of parents to create a new generation of guesses.
# Mutation: Randomly alter some guesses to maintain genetic diversity.
# Repeat: Repeat the evaluation, selection, crossover, and mutation steps until the correct number is found.
# Here is a Python implementation of the genetic algorithm:

import random
import time

# Generate a random 7-digit guess
def generate_random_guess():
    return ''.join([str(random.randint(0, 9)) for _ in range(7)])

# Evaluate the fitness of a guess by comparing it to the secret number
def evaluate_guess(guess, secret_number):
    return sum(1 for g, s in zip(guess, secret_number) if g == s)

# Select the best parents based on fitness
def select_parents(population, fitnesses):
    # Sort population by fitness in descending order and select top 50%
    sorted_population = sorted(zip(population, fitnesses), key=lambda x: x[1], reverse=True)
    return [guess for guess, fitness in sorted_population[:len(population) // 2]]

# Perform crossover between two parents to create two children
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Randomly mutate a single digit in a guess
def mutate(guess):
    guess_list = list(guess)
    mutation_index = random.randint(0, len(guess) - 1)
    guess_list[mutation_index] = str(random.randint(0, 9))
    return ''.join(guess_list)

def genetic_algorithm(secret_number):
    # Initialization: Create initial population of random guesses
    population_size = 100
    population = [generate_random_guess() for _ in range(population_size)]
    generation = 0
    start_time = time.time()
    last_print_time = start_time

    while True:
        generation += 1

        # Evaluation: Evaluate each guess and assign fitness score
        fitnesses = [evaluate_guess(guess, secret_number) for guess in population]

        # Check if the correct number is found
        if max(fitnesses) == len(secret_number):
            best_guess = population[fitnesses.index(max(fitnesses))]
            elapsed_time = (time.time() - start_time) * 1000
            print(f"Guessed correctly! The number is {best_guess}.")
            print(f"It took {generation} generations and {elapsed_time:.2f} milliseconds.")
            break

        # Selection: Select the best guesses to be parents
        parents = select_parents(population, fitnesses)
        next_generation = []

        # Crossover: Combine pairs of parents to create new guesses
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            next_generation.extend([mutate(child1), mutate(child2)])

        # Update population with new generation
        population = next_generation[:population_size]

        # Print the elapsed time and generation number every 100 milliseconds
        current_time = time.time()
        elapsed_time = (current_time - start_time) * 1000
        if (current_time - last_print_time) >= 0.1:  # Check if 100 milliseconds have passed
            print(f"Elapsed time: {elapsed_time:.2f} milliseconds, Generation: {generation}")
            last_print_time = current_time

if __name__ == "__main__":
    secret_number = input("Enter a 7-digit number as the secret number: ")
    while len(secret_number) != 7 or not secret_number.isdigit():
        secret_number = input("Invalid input. Please enter a valid 7-digit number: ")
    genetic_algorithm(secret_number)


# 1) Initialization: Create initial population of random guesses
# population_size = 100
# population = [generate_random_guess() for _ in range(population_size)]
# generation = 0
# start_time = time.time()
# last_print_time = start_time

# 2) Evaluation: Evaluate each guess and assign fitness score
# Evaluation: Evaluate each guess by comparing it to the secret number and assigning a fitness score based on how many digits are correct.
# fitnesses = [evaluate_guess(guess, secret_number) for guess in population]

# 3) Check if the correct number is found: If a guess matches the secret number, print the result and exit.
# Check if the correct number is found
# if max(fitnesses) == len(secret_number):
#     best_guess = population[fitnesses.index(max(fitnesses))]
#     elapsed_time = (time.time() - start_time) * 1000
#     print(f"Guessed correctly! The number is {best_guess}.")
#     print(f"It took {generation} generations and {elapsed_time:.2f} milliseconds.")
#     break

# 4) Selection: Select the best guesses to be parents # Selection: Select the best guesses to be parents
# parents = select_parents(population, fitnesses)
# next_generation = []

# 5) Crossover: Combine pairs of parents to create new guesses
# Crossover: Combine pairs of parents to create new guesses
# while len(next_generation) < population_size:
#     parent1, parent2 = random.sample(parents, 2)
#     child1, child2 = crossover(parent1, parent2)
#     next_generation.extend([mutate(child1), mutate(child2)])

# 6) Mutation: Randomly alter some guesses to maintain genetic diversity / Update Population: Replace the old population with the new generation.
# Update population with new generation
# population = next_generation[:population_size]
