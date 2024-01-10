'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 03
Date: 16/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 03 \n Date: 16/08/2023")

print("\n ############# ################ ####################\n")

import numpy as np
import matplotlib.pyplot as plt

# Plot Stuff
wavy = np.arange(-10., 10., 0.2)

# Sigmoid Function
siggy = 1/(1+np.exp(-wavy))

# TanH Function
tanny = (2/(1+np.exp(-2*wavy)))-1

def ReLU(x):
  data = [max(0,value) for value in x]
  return np.array(data, dtype=float)

reluy = ReLU(wavy)

# Ploting the things
plt.figure(figsize=(10,10))
plt.style.use('seaborn-darkgrid')

plt.subplot(2,2,1)
plt.title("Linear Function")
plt.plot(wavy, color="xkcd:dark teal")

plt.subplot(2,2,2)
plt.title("Sigmoid Function")
plt.plot(wavy, siggy, color="xkcd:lime green")

plt.subplot(2,2,3)
plt.title("TanH Function")
plt.plot(wavy, tanny, color="xkcd:hot pink")

plt.subplot(2,2,4)
plt.title("ReLU Function")
plt.plot(wavy, reluy, color="xkcd:purple blue")

plt.show()

plt.title("Activation Functions - A Comparison")
plt.plot(wavy, siggy, color="xkcd:green yellow")
plt.plot(wavy, tanny, color="xkcd:hot pink")
plt.plot(wavy, reluy, color="xkcd:purple blue")
plt.legend(['Sigmoid', 'TanH', 'ReLU'])
plt.xlim(left=-5)
plt.xlim(right=5)
plt.ylim(bottom=-1.5)
plt.ylim(top=1.5)

plt.show()

# Curiously Crafted By Redzwinger #

