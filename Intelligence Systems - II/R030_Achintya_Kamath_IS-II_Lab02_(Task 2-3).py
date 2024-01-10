'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 02
Date: 20/12/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 02 \n Date: 20/12/2023")

print("\n ############# ################ ####################\n")

print(" Task 2 and 3\n")

print(" ############# ################ ####################\n")

from pgmpy.base import *
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete.CPD import TabularCPD

# Task 2 #
print("\n --------------------- \n Task 2 [add_cpds()] \n ---------------------")

STU = BayesianNetwork([('diff', 'grades'), ('aptitude', 'grades')])

grades_cpd = TabularCPD('grades', 3, [[0.1,0.1,0.1,0.1,0.1,0.1],
                                      [0.1,0.1,0.1,0.1,0.1,0.1],
                                      [0.8,0.8,0.8,0.8,0.8,0.8]],
                        evidence=['diff', 'aptitude'], evidence_card=[2, 3],
                        state_names={'grades': ['gradeA', 'gradeB', 'gradeC'],
                                     'diff': ['easy', 'hard'],
                                     'aptitude': ['low', 'medium', 'high']})

STU.add_cpds(grades_cpd)

print(f"\n Joint Distribution Table: \n{grades_cpd}")

# Task 3 #
print("\n --------------------- \n Task 3 \n ---------------------")

print(" Domain: E-commerce\n Event A: The product sales will increase.\n Event B: The advertisement campaign was good.\n Probability Scenario: What is the probability that the product sales will increase knowing that the advertisement campaign was good?\n ---------------------")

ECOM = BayesianNetwork([('Sales', 'Campaign'), ('Sales', 'Quality')])

sales_cpd = TabularCPD('Campaign', 2, [[0.300,0.015,0.025,0.105],
                                       [0.175,0.005,0.095,0.280]],
                        evidence=['Sales', 'Quality'], evidence_card=[2,2],
                        state_names={'Sales': ['Sales Increases', 'Sales Decreases'],
                                     'Quality': ['Good Quality', 'Bad Quality'],
                                     'Campaign': ['Good Campaign', 'Bad Campaign']})

ECOM.add_cpds(sales_cpd)

print(f"\n Joint Distribution Table: \n{sales_cpd}")

# Catestrophically Crafted by Redzwinger #

