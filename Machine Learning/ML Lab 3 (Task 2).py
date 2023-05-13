import random as dice
import matplotlib.pyplot as plt
import numpy as np

'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 24/12/2022
Practical 3
B1_P1_030
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Practical 3 \n Machine Learning: Data Visualization Techniques")

print("\n ############# ################ ####################\n")

# Task 2 #
import pandas as pd

# Importing the Dataset #
seeds = pd.read_csv('seeds.csv')
print(f'''

Shape of DataFrame :\n {seeds.shape}\n
Size of DataFrame  :\n {seeds.size}\n
All the DataTypes  :\n {seeds.info()}\n
Columns in CSV     :\n {seeds.columns}\n
Top Five Values    :\n {seeds.head(5)}\n
Description of CSV :\n {seeds.describe()}

''')

column = seeds["Type"].unique()
numb = []

for z in column:
    numb.append(seeds["Type"].value_counts()[z])

print(f"Counts are as Follows \n")

for x in range(len(numb)):
    print("Type ",column[x]," : ",numb[x])

# Plotting Scatter for Kernel Width against Length #
plt.title("Relation of Sepals")
plt.xlabel("Kernel Width")
plt.ylabel("Kernel Length")
plt.scatter(seeds["Kernel.Width"],seeds["Kernel.Length"],color="xkcd:Neon Pink")
plt.show()

# Different Type with Different Colors #
plt.title("Classification of Types")
plt.xlabel("Kernel Width")
plt.ylabel("Kernel Length")

for z in seeds.index:
    colorme = str()
    if seeds["Type"][z] == 1:
        colorMe = "Dark Pink"

    elif seeds["Type"][z] == 2:
        colorMe = "Azure"

    elif seeds["Type"][z] == 3:
        colorMe = "Spring Green"

    plt.scatter(seeds["Kernel.Width"][z],seeds["Kernel.Length"][z],color=f"xkcd:{colorMe}")

plt.show()

