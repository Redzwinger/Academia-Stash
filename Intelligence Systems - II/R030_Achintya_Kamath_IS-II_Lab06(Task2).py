'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 06 (Task 2)
Date: 07/02/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 06 (Task 2) \n Date: 07/02/2024")

print("\n ############# ################ ####################\n")

print(" Task 2\n")

print(" ############# ################ ####################\n")

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

DenTraf = ctrl.Antecedent(np.arange(0,101,1),"traffic_density")
WAIT = ctrl.Antecedent(np.arange(0,11,1),"waiting_time")

light_phase = ctrl.Consequent(np.arange(0,101,1),"light_phase")

DenTraf['low'] = fuzz.trimf(DenTraf.universe,[0,20,40])
DenTraf['medium'] = fuzz.trimf(DenTraf.universe,[20,30,80])
DenTraf['high'] = fuzz.trimf(DenTraf.universe,[60,80,100])

WAIT['short'] = fuzz.trimf(WAIT.universe,[0,2,4])
WAIT['medium'] = fuzz.trimf(WAIT.universe,[2,5,8])
WAIT['long'] = fuzz.trimf(WAIT.universe,[6,9,10])

light_phase['red'] = fuzz.trimf(light_phase.universe,[0,20,40])
light_phase['yellow'] = fuzz.trimf(light_phase.universe,[20,50,80])
light_phase['green'] = fuzz.trimf(light_phase.universe,[60,80,100])

rule1 = ctrl.Rule(DenTraf['low'] & WAIT['short'],light_phase['green'])
rule2 = ctrl.Rule(DenTraf['medium'] & WAIT['medium'],light_phase['yellow'])
rule3 = ctrl.Rule(DenTraf['high'] & WAIT['long'],light_phase['red'])

trafLiteCon = ctrl.ControlSystem([rule1,rule2,rule3])

trafLite = ctrl.ControlSystemSimulation(trafLiteCon)

trafLite.input["traffic_density"] = 30
trafLite.input["waiting_time"] = 5

trafLite.compute()

print(" Light Phase: ",trafLite.output['light_phase'])

DenTraf.view()
plt.show()

WAIT.view()
plt.show()

light_phase.view(sim = trafLite)
plt.show()

# Confusedly Crafted By Redzwinger #

