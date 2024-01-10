'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 02
Date: 09/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 02 \n Date: 09/08/2023")

print("\n ############# ################ ####################\n")

# importing stuff
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

# Reading and Displaying the .csv
data_stuf = pd.read_csv("Iris.csv")
print("\n\n Iris Data Set:\n\n", data_stuf.head())

# Doing things

species = pd.get_dummies(data_stuf["Species"])
print("\n\n This is the Species Column:\n\n", species)

# Dropping Species Column
data_stuf.drop("Species", axis=1, inplace=True)
print("\n\n After One-Hot Encoding:\n\n", data_stuf.head())

from sklearn.preprocessing import StandardScaler as ss

std_scaler = ss()
data_stuf_skelly = std_scaler.fit_transform(data_stuf)

# This is the difference between fit and transform #

print("\n\n Scaled Data: \n\n", data_stuf_skelly)

# Creating Data Frame

trans_data_stuf = pd.DataFrame(data_stuf_skelly, columns=['SepalLength','CmSepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
print("\n\n Transformed Data: \n\n", trans_data_stuf)

# Final

final_df = pd.concat([trans_data_stuf, species], axis=1)
print("\n\n Final Iris: \n\n", final_df)

'''
Input Features ill Be,
150 x 4
[150 Samples, 4 Columns]

Output will be,
150 x 3
[3 Classes]
'''

# MOAR Processing

dat_input = final_df.iloc[:,0:4]
print("\n\n Taking a look at the Input Data, \n\n", dat_input, "\n\n It's shape is found out to be", dat_input.shape, end="\n\n")

