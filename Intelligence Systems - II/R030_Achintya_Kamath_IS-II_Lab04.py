'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 04
Date: 31/01/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 04 \n Date: 31/01/2024")

print("\n ############# ################ ####################\n")

#pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperature = np.arange(15, 40)

temp = ctrl.Antecedent(temperature, 'temp')
print(" ",temp)

ac_temperature = np.arange(15, 45)
print(" ",ac_temperature)

ac_temp = ctrl.Consequent(ac_temperature, 'ac_temp')
print(" ",ac_temp)

temp.automf(3)
ac_temp.automf(3)

temp.view()
plt.show()

rule1 = ctrl.Rule(temp['poor'],ac_temp['good'])
rule2 = ctrl.Rule(temp['good'],ac_temp['poor'])
rule3 = ctrl.Rule(temp['average'],ac_temp['average'])

temperature_control = ctrl.ControlSystem([rule1, rule2, rule3])
detect_temp = ctrl.ControlSystemSimulation(temperature_control)
detect_temp.input['temp'] = 24
detect_temp.compute()

detect_temp.output['ac_temp']

ac_temp.view(sim = detect_temp)