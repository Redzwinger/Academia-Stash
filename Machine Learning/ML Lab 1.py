'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 24/12/2022
Practical 1
B1_P1_030
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Date: 24/12/2022 \n Practical 1 \n Machine Learning: Pandas")

print("\n ############# ################ ####################\n")

# importing stuff
import numpy as np
import pandas as pd

# Creating a dataframe by reading the .csv
csvdtfra = pd.read_csv("indian_food.csv")
#print(csvdtfra)

# Finding the shape of the Dataframe

print("\n The shape of the current dataframe is",csvdtfra.shape)
print(" ----------------- --------------------- -------------------")

# Finding the size of the Dataframe

print("\n", csvdtfra.size, "is the size of the current dataframe.\n")
print(" ----------------- --------------------- -------------------")

# Info regarding the Dataframe

print("\n Some info about the dataframe 'indian_food.csv':\n")
print(csvdtfra.info())
print(" ----------------- --------------------- -------------------")

# Getting the top 5 dishes in the Dataframe

print("\n These are the top 5 dishes:\n\n",csvdtfra.head(5))
print(" ----------------- --------------------- -------------------")

# Description of the Dataframe

print("\n Here is the Description of the Dataframe:\n\n",csvdtfra.describe())
print(" ----------------- --------------------- -------------------")

# Finding and replacing the non-existing values with NaN in the Dataframe

print("\n The missing values are set as '-1' in the csv.\nReplacing '-1' with 'nan'\n\n")
replaced_csv = csvdtfra.replace(-1, "NaN")
print(replaced_csv.to_markdown())
#print(csvdtfra.to_string())
print(" ----------------- --------------------- -------------------")

#Finding out the numeric and categorical data in the dataset

print("\nNumeric and Categorical Data:\n\n")
print(csvdtfra._get_numeric_data())
print(" ----------------- --------------------- -------------------")

# Unique Stuff

print("\n These are unique:\n\n", csvdtfra.nunique())
print(" ----------------- --------------------- -------------------")

# Listing the columns in the Dataframe

col = csvdtfra.columns
print("\n The names of the columns are as follows:\n\n", col)
print(" ----------------- --------------------- -------------------")

# Adding a column that gives the total time taken to prepare a dish (prep time + cook time)

print("\nAdding a column that gives the total time taken to prepare a dish (prep time + cook time)...\n\n")

#replaced_again_csv = csvdtfra.replace(-1, 0)
#replaced_again_csv['Total_time_taken'] = csvdtfra['prep_time'] + csvdtfra['cook_time']
#print(replaced_again_csv.to_markdown())

#replacing the missing data with 0
csvdtfra['Total_time_taken'] = csvdtfra['prep_time'].replace(-1, 0) + csvdtfra['cook_time'].replace(-1, 0)
print(csvdtfra.to_markdown())
print(" ----------------- --------------------- -------------------")

# Adding a new column that gives the number of ingredients for each dish

csvdtfra['number of ingredients'] = (csvdtfra['ingredients'].str.split(",").str.len())
print(csvdtfra.to_markdown())
print(" ----------------- --------------------- -------------------")

##---------------------------------------------##
##--- Program by Achintya Kamath/Redzwinger ---##
##---------------------------------------------##
