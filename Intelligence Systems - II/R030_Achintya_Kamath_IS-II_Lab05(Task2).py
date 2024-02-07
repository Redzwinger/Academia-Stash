'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 05 (Task 2)
Date: 31/01/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 05 \n Date: 31/01/2024")

print("\n ############# ################ ####################\n")

print(" Task 2\n")

print(" ############# ################ ####################\n")

import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import numpy as np

subj_1 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_1')
subj_2 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_2')
subj_3 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_3')
subj_4 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_4')
subj_5 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_5')
subj_6 = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'subject_6')

overall_gpa = ctrl.Consequent(np.arange(0, 4.1, 0.1), 'overall_gpa')

for subject in [subj_1, subj_2, subj_3, subj_4, subj_5, subj_6]:
    subject['poor'] = fuzz.trimf(subject.universe, [0, 0, 2])
    subject['average'] = fuzz.trimf(subject.universe, [1, 2, 3])
    subject['good'] = fuzz.trimf(subject.universe, [2, 4, 4])

overall_gpa['poor'] = fuzz.trimf(overall_gpa.universe, [0, 0, 2])
overall_gpa['average'] = fuzz.trimf(overall_gpa.universe, [1, 2, 3])
overall_gpa['good'] = fuzz.trimf(overall_gpa.universe, [2, 4, 4])

rule1 = ctrl.Rule(subj_1['poor'] | subj_2['poor'] | subj_3['poor'] | subj_4['poor'] | subj_5['poor'] | subj_6['poor'], overall_gpa['poor'])

rule2 = ctrl.Rule(subj_1['average'] & subj_2['average'] & subj_3['average'] & subj_4['average'] & subj_5['average'] & subj_6['average'], overall_gpa['average'])

rule3 = ctrl.Rule(subj_1['good'] | subj_2['good'] | subj_3['good'] | subj_4['good'] | subj_5['good'] | subj_6['good'], overall_gpa['good'])

overall_gpa_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

overall_gpa_sim = ctrl.ControlSystemSimulation(overall_gpa_ctrl)

gpa_values = []
for i in range(1, 7):
    gpa = float(input(f"Enter GPA for subject {i}: "))
    gpa_values.append(gpa)

overall_gpa_sim.input['subject_1'] = gpa_values[0]
overall_gpa_sim.input['subject_2'] = gpa_values[1]
overall_gpa_sim.input['subject_3'] = gpa_values[2]
overall_gpa_sim.input['subject_4'] = gpa_values[3]
overall_gpa_sim.input['subject_5'] = gpa_values[4]
overall_gpa_sim.input['subject_6'] = gpa_values[5]

overall_gpa_sim.compute()

print(" \nOverall GPA:", overall_gpa_sim.output['overall_gpa'])

fig, ax = plt.subplots()

for subject in [subj_1, subj_2, subj_3, subj_4, subj_5, subj_6]:
    ax.plot(subject.universe, fuzz.trimf(subject.universe, [0, 0, 2]), 'r--', linewidth=1.5)
    ax.plot(subject.universe, fuzz.trimf(subject.universe, [1, 2, 3]), 'g--', linewidth=1.5)
    ax.plot(subject.universe, fuzz.trimf(subject.universe, [2, 4, 4]), 'b--', linewidth=1.5)

ax.plot(overall_gpa.universe, 
        fuzz.trimf(overall_gpa.universe, [0, 0, 2]), 'r', linewidth=2, label='Poor')
ax.plot(overall_gpa.universe, 
        fuzz.trimf(overall_gpa.universe, [1, 2, 3]), 'g', linewidth=2, label='Average')
ax.plot(overall_gpa.universe, 
        fuzz.trimf(overall_gpa.universe, [2, 4, 4]), 'b', linewidth=2, label='Good')

ax.plot(overall_gpa_sim.output['overall_gpa'], 0.5, 'ko', markersize=10, label='Overall GPA')

ax.legend()
plt.xlabel('GPA')
plt.ylabel('Membership')
plt.title('Fuzzy Membership Functions')

plt.show()

# Carefully Crafted By Redzwinger #

