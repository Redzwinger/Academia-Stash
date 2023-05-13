'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 11/03/2022
Machine Learning
Lab 7
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Date: 11/03/2022 \n Lab 7 \n Machine Learning: Naive Based Classifier")

print("\n ############# ################ ####################\n")

# importing stuff
import numpy as np
import pandas as pd

# Creating a dataframe by reading the .csv
hu = pd.read_csv("humanData.csv")

# Find and Displaying all the details of the Dataframe

# Finding the size of the Dataframe

print("\n", hu.size, "is the size of the current dataframe.\n")
print(" ----------------- --------------------- -------------------")

# Finding the shape of the Dataframe

print("\n The shape of the current dataframe is\n\n",hu.shape)
print("\n ----------------- --------------------- -------------------")

# Info regarding the Dataframe

print("\n Some info about the dataframe:\n\n")
print(hu.info())
print(" ----------------- --------------------- -------------------")

# Listing the columns in the Dataframe

print("\n The columns in this dataframe are as follows:\n\n", hu.columns)
print("\n ----------------- --------------------- -------------------")

# Displaying first 5 data entries in the Dataframe

print("\n The first 5 data entries in this Dataframe are as follows:\n\n", hu.head)
print("\n ----------------- --------------------- -------------------")

# Displaying some more info regarding the Dataframe

print("\n Some more info about the dataframe:\n\n")
print(hu.describe())
print(" ----------------- --------------------- -------------------")

# Checking the number of NUll values if they exist, here NULL values are '?'

print("\n Number of NULL values in the database:\n\n")
print(hu.isin([' ?']).sum())
print(" ----------------- --------------------- -------------------")

# Rectifying the problems in the columns that have NULL values by dropping the rows containing them.

hu[~hu.workingclass.str.contains(" ?")]

print("\n Number of NULL values in the database:\n\n")
print(hu.isin([' ?']).sum())
print(" ----------------- --------------------- -------------------")