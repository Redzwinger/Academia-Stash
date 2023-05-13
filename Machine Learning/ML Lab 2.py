'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 24/12/2022
Practical 2
B1_P1_030
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Date: 24/12/2022 \n Practical 2 \n Machine Learning: Pandas - Toyota Edition")

print("\n ############# ################ ####################\n")

# importing stuff
import numpy as np
import pandas as pd

# Creating a dataframe by reading the .csv
toyo = pd.read_csv("Toyota.csv")
#print(toyo)

# Finding the size of the Dataframe

print("\n", toyo.size, "is the size of the current dataframe.\n")
print(" ----------------- --------------------- -------------------")

# Finding the shape of the Dataframe

print("\n The shape of the current dataframe is\n\n",toyo.shape)
print("\n ----------------- --------------------- -------------------")

# Info regarding the Dataframe

print("\n Some info about the dataframe 'indian_food.csv':\n\n")
print(toyo.info())
print(" ----------------- --------------------- -------------------")

# Listing the columns in the Dataframe

print("\n The columns in this dataframe are as follows:\n\n", toyo.columns)
print("\n ----------------- --------------------- -------------------")

# Displaying the 'fuel type' column

print("\n All the rows in 'FuelType' column.\n\n")
print(toyo['FuelType'].to_markdown())
print("\n ----------------- --------------------- -------------------")

# Displaying the 'KM', 'HP', 'Automatic' columns

print("\n All the rows in 'KM', 'HP', 'Automatic' column.\n\n")
print(toyo[['KM', 'HP', 'Automatic']].to_markdown())
print("\n ----------------- --------------------- -------------------")

# Displaying rows 1 to 5 for columns 2 to 4 (excluding row 5 and column 4)

print("\n Displaying rows 1 to 5 for columns 2 to 4 (excluding row 5 and column 4):\n\n")
print(toyo.iloc[0:4,0:3].to_markdown())
print("\n ----------------- --------------------- -------------------")

# Displaying the info of dataset

print("\n Displaying the info of dataset:\n\n")
print(toyo.info())
print("\n ----------------- --------------------- -------------------")

# Displaying the unique values of 'KM', 'HP', 'Doors' columns

print("\n Displaying the unique values of 'KM', 'HP', 'Doors' columns:\n\n")
unitoyo = toyo[['KM', 'HP', 'Doors']].drop_duplicates()
print(unitoyo.to_markdown())
print("\n ----------------- --------------------- -------------------")

# Replacing the ?? with NAN
print("\n Replacing the ?? with NAN:\n\n")
nantoyo = toyo.replace("??", "NAN")
print(nantoyo.to_markdown())
print("\n ----------------- --------------------- -------------------")

# Replacing categorical data to numeric in 'Doors' column

print("\n Replacing categorical data to numeric:\n\n")
toyo['Doors'] = toyo['Doors'].replace(to_replace=("three", "four", "five"), value=(3,4,5))
print(toyo['Doors'].to_markdown())
print("\n ----------------- --------------------- -------------------")

# Converting columns 'Doors', 'Metcolour', and 'Automatic' to int and object
'''
toyo['intdoor'] = toyo['Doors'].astype(int)
toyo['intMetcolor'] = toyo['Metcolor'].astype(int)
toyo['intAutomatic'] = toyo['Automatic'].astype(int)

toyo['obdoor'] = toyo['Doors'].astype(object)
toyo['obMetcolor'] = toyo['Metcolor'].astype(object)
toyo['obAutomatic'] = toyo['Automatic'].astype(object)

intobtoyo = toyo[['intdoor','intMetcolour','intAutomatic','obdoor','obMetcolour','obAutomatic']]

print(intobtoyo.to_markdown())
'''

# Total number of null values in each column

null_sum = toyo.isnull().sum()

print("\nTotal number of null values in each column:\n\n")
print(null_sum)
print("\n ----------------- --------------------- -------------------")

# Dropping rows with null values

toyonotnull = toyo.dropna()
print("\n Dropping rows with null values:\n\n")
print(toyonotnull)
print("\n ----------------- --------------------- -------------------")

# Identifying Total number of cars that use fuel type "Petrol", "Diesel" or "CNF"

selectivetoyo = toyo[toyo.isin(["Petrol", "Diesel", "CNG"])]

num_o_car = len(selectivetoyo['HP']) - 1

print("\n Identifying Total number of cars that use fuel type 'Petrol', 'Diesel' or 'CNG':\n\n")
print(" ", num_o_car, "number of cars have been identified")
print("\n ----------------- --------------------- -------------------")

# Identifying the mean of the 'KM' column for the cars that run on 'Diesel'

meantoyo = nantoyo[nantoyo.isin(["Diesel"])]
#meantoyo_nonull = meantoyo.replace("nan", 0).astype(int)
mean_o_km = meantoyo['KM'].mean(skipna=True)

print("\n Identifying the mean of the 'KM' column for the cars that run on 'Diesel':\n\n")
print(" ", mean_o_km, "is the mean.")
print("\n ----------------- --------------------- -------------------")

#One hot encoding of adults.csv

print("\n One-hot encoding the relationship column of the 'adult.csv':\n\n")
adult = pd.read_csv("adult.csv")
dummie_adult = pd.get_dummies(data=adult, columns = ['relationship'])
print(dummie_adult)
print("\n ----------------- --------------------- -------------------")

