'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 02
Date: 16/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 02 \n Date: 16/08/2023")

print("\n Task 3")

print("\n ############# ################ ####################\n")

# importing stuff
import array
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

data_stuf = pd.read_csv("Iris.csv")

species = pd.get_dummies(data_stuf["Species"])
data_stuf.drop("Species", axis=1, inplace=True)

from sklearn.preprocessing import StandardScaler as ss

std_scaler = ss()
data_stuf_skelly = std_scaler.fit_transform(data_stuf)

trans_data_stuf = pd.DataFrame(data_stuf_skelly, columns=['SepalLength','CmSepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])

final_df = pd.concat([trans_data_stuf, species], axis=1)
dat_input = final_df.iloc[:,0:4]

# Setting a differnt Seed Value
np.random.seed(89)

# Weights

weight_h_one = np.random.rand(4,1)
weight_h_two = np.random.rand(4,1)
weight_o_one = np.random.rand(2,1)
weight_o_two = np.random.rand(2,1)
weight_o_three = np.random.rand(2,1)

bias_one = np.random.rand(1)
bias_two = np.random.rand(1)

def sigmoider(thing):
    return 1/(1+np.exp(-thing))

Z2_1 = np.dot(dat_input, weight_h_one) + bias_one
Z2_2 = np.dot(dat_input, weight_h_two) + bias_two

H2_1 = sigmoider(Z2_1)
H2_2 = sigmoider(Z2_2)

HiddenLayer_Two = np.append(H2_1, H2_2, axis=1)

Z3_1 = np.dot(HiddenLayer_Two, weight_o_one)
Z3_2 = np.dot(HiddenLayer_Two, weight_o_two)
Z3_3 = np.dot(HiddenLayer_Two, weight_o_three)

O3_1 = sigmoider(Z3_1)
O3_2 = sigmoider(Z3_2)
O3_3 = sigmoider(Z3_3)

print("\n\n Layer 3 - Neuron 1:\n", O3_1)
print("\n\n Layer 3 - Neuron 2:\n", O3_2)
print("\n\n Layer 3 - Neuron 3:\n", O3_3)

# Output Layer
HiddenLayer_Three = np.append(O3_1, O3_2, axis=1)
HiddenLayer_Three = np.append(HiddenLayer_Three, O3_3, axis=1)

# Calculating Error #

# OneHot Encoding the target columns
targetOne = np.array(final_df.iloc[:,4])
targetOne.reshape((-1,1))

targetTwo = np.array(final_df.iloc[:,5])
targetTwo.reshape((-1,1))

targetThree = np.array(final_df.iloc[:,6])
targetThree.reshape((-1,1))

# Applying the Error Function
E1 = targetOne - O3_1
E2 = targetTwo - O3_2
E3 = targetThree - O3_3

# Total Error
RogueError = np.multiply(E1,E1) + np.multiply(E2,E2) + np.multiply(E3,E3) # Squaring
TotError = np.sum(RogueError)

print("\n The Total Error is :", TotError, "\n")

# Hand-Crafted By Redzwinger #
