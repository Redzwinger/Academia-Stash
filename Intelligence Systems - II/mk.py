# %%
"""
Absolutely, here's a Python code for a Markov chain model with a real-time weather example:
"""

# %%
import random

# Define weather states
states = ("Sunny", "Rainy", "Cloudy")

# Transition probability matrix (rows represent current state, columns represent next state)
transition_matrix = {
  "Sunny": [0.7, 0.2, 0.1],
  "Rainy": [0.3, 0.5, 0.2],
  "Cloudy": [0.4, 0.3, 0.3]
}

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

# %%
"""
**Explanation:**

1. We import the `random` library for random number generation.
2. We define the weather states as a tuple.
3. We create a transition probability matrix. Each row represents the current state, and each column represents the next possible state. The values in the cells represent the probability of transitioning from the current state to the next state (each row must sum to 1).
4. We get the initial weather state. This can be user input or randomly chosen.
5. We define the number of days to simulate the weather for.
6. We loop for the specified number of days:
    - Get the probability distribution for the next day's weather based on the current state (using the current row of the transition matrix).
    - Use the `random.choices` function with weights to randomly choose the next state based on the probabilities.
    - Update the current state and print the predicted weather for the next day.

This is a basic example, and you can extend it further:

*  Read weather data from an API and use it to populate the initial state and potentially refine the transition matrix.
*  Visualize the weather simulation using libraries like Matplotlib.
*  Predict the probability of a specific weather sequence for a longer period.
"""