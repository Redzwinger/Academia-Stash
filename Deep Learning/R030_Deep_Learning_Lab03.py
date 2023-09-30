'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 02
Date: 16/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 02 \n Date: 16/08/2023")

#print("\n Task 1 & 2")

print("\n ############# ################ ####################\n")

import numpy as np
import matplotlib.pyplot as plt

# Plot Stuff
plt.figure(figsize=(10,10))
wavy = np.arange(-1,1,0,1)

# Sigmoid Function
siggy = 1/(1+np.exp(-wavy))

# Plot
plt.title("Sigmoid Function")
plt.plot(wavy,siggy, color="xkcd:lime green")

siggy2 = 1/(1+np.exp(-wavy)) + 1/(1+np.exp(-wavy))

plt.plot(wavy, siggy2, color="xkcd:lime green")

plt.show()

# Curiously Crafted By Redzwinger #