'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 06 (Task 1)
Date: 07/02/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 06 (Task 1) \n Date: 07/02/2024")

print("\n ############# ################ ####################\n")

print(" Task 1\n")

print(" ############# ################ ####################\n")

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Task 1-1-a
Age = ctrl.Antecedent(np.arange(1,101,1),'age')
Age['Young'] = fuzz.gbellmf(Age.universe,12,10,17)
Age['Middle-aged'] = fuzz.gbellmf(Age.universe,20, 10, 40)
Age['Old'] = fuzz.gbellmf(Age.universe,20, 10, 70)
Age.view()
plt.show()

# Task 1-1-b
Age['Young'] = fuzz.gbellmf(Age.universe,12,10,17)
Age['Adult'] = fuzz.gbellmf(Age.universe,15,10,27)
Age['Senior Adult'] = fuzz.gbellmf(Age.universe,15,10,80)
Age.view()
plt.show()

# Task 1-2-a
TMP =  ctrl.Antecedent(np.arange(0,101,1),'temperature')
TMP['low'] = fuzz.trimf(TMP.universe,[0,20,40])
TMP['medium'] = fuzz.trimf(TMP.universe,[30,50,70])
TMP['high'] = fuzz.trimf(TMP.universe,[60,80,100])
TMP.view()
plt.show()

# Task 1-2-b
TMP['low'] = fuzz.trapmf(TMP.universe,[0,15,25,40])
TMP['medium'] = fuzz.trapmf(TMP.universe,[30,45,55,70])
TMP['high'] = fuzz.trapmf(TMP.universe,[60,75,85,100])
TMP.view()
plt.show()

# Confusedly Crafted By Redzwinger #

