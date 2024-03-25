'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 09
Date: 20/03/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 09 \n Date: 20/03/2024")

print("\n ############# ################ ####################\n")

print(" Task 1: Basic Markov Chain Model.")

print("\n ############# ################ ####################\n")

import random

# Define weather states
states = ("Sunny", "Rainy", "Cloudy")

# Transition probability matrix (rows represent current state, columns represent next state)
transition_matrix = {"Sunny": [0.7, 0.2, 0.1],
                     "Rainy": [0.3, 0.5, 0.2],
                     "Cloudy": [0.4, 0.3, 0.3]}

# Get initial weather (can be user input or random)
current_state = random.choice(states)
print(f"Today's weather is: {current_state}")

# Simulate next day's weather for a number of days
num_days = 5
for _ in range(num_days):
  # Get probability distribution for next day based on current state
  probabilities = transition_matrix[current_state]

  # Randomly choose the next state based on probabilities
  next_state = random.choices(states, weights=probabilities)[0]

  # Update current state and print the next day's weather
  current_state = next_state
  print(f"Tomorrow's weather will likely be: {current_state}")

# Randomly Crafted by Redzwinger #