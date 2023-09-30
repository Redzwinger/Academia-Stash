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

print("\n Task 1 & 2")

print("\n ############# ################ ####################\n")

# importing stuff
import array
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

'''
Creating a single layer neural network
'''

# Setting Seed Value

np.random.seed(1433)

# Setting Randomized Weights

# 4 Input Nodes
weight_h_one = np.random.rand(4,1)
weight_h_two = np.random.rand(4,1)

# 2 Hidden Nodes
weight_o_one = np.random.rand(2,1)
weight_o_two = np.random.rand(2,1)
weight_o_three = np.random.rand(2,1)

print(" The Weights are :\n\n ", )
print(weight_h_one, weight_h_two, weight_o_one, weight_o_two, weight_o_three)

# Now Asigning Biases #
bias_one = np.random.rand(1)
bias_two = np.random.rand(1)
print("\n\n The Biases are : ", end="\n\n")
print(bias_one, bias_two)

# Sigmoid Function #
def sigmoid(someThing):
    with tf.GradientTape() as tape_sig:
        f = (1 / 1 + (tf.math.exp(-someThing)))
    sigma_grad = tape_sig.gradient(f, someThing)
    return sigma_grad.numpy()

'''
Testing Sigmoid

test = sigmoid(tf.Variable(0,0, trainable=True))
print("\n\n Sigmoid is, \n\n", test)
'''

def sigmoider(thing):
    return 1/(1+np.exp(-thing))

print("\n\n Dot Product of Input and Hidden Weight:\n\n", np.dot(dat_input, weight_h_one))
print("\n With bias:\n", bias_one)

# Doing the thing - Input to hidden layer
Z2_1 = np.dot(dat_input, weight_h_one) + bias_one
Z2_2 = np.dot(dat_input, weight_h_two) + bias_two

'''
Here, basically
Z2_1 is layer 2 Neuron 1
Z2_2 is layer 2 Neuron 2

Z = sum(input x weights) + bias
'''

# Activation Function on Layer 2
H2_1 = sigmoider(Z2_1)
H2_2 = sigmoider(Z2_2)

'''
These are the Hidden Layers,
Hidden Layer 1: H2_1 
Hidden Layer 2: H2_2
'''

'''
Appending it to one singular entity from the existing two.
150 x 2 (dot) 2 x 1
2 x 1 is the Input for Neural Layer 3

Which is the reason for (dot) giving 150 x 1 (for one)
Ultimately resulting in, 
150 x 2
'''

HiddenLayer_Two = np.append(H2_1, H2_2, axis=1)
print("\n\n Hidden Layer:\n", HiddenLayer_Two, "\n\n With shape: ", HiddenLayer_Two.shape)

# Working Layer 3
Z3_1 = np.dot(HiddenLayer_Two, weight_o_one)
Z3_2 = np.dot(HiddenLayer_Two, weight_o_two)
Z3_3 = np.dot(HiddenLayer_Two, weight_o_three)

# Activating Layer 3
O3_1 = sigmoider(Z3_1)
O3_2 = sigmoider(Z3_2)
O3_3 = sigmoider(Z3_3)

print("\n\n Layer 3 - Neuron 1:\n", O3_1)
print("\n\n Layer 3 - Neuron 2:\n", O3_2)
print("\n\n Layer 3 - Neuron 3:\n", O3_3)

# Output Layer
HiddenLayer_Three = np.append(O3_1, O3_2, axis=1)
HiddenLayer_Three = np.append(HiddenLayer_Three, O3_3, axis=1)
print("\n\n Output Layer:\n", HiddenLayer_Three, "\n\n With shape: ", HiddenLayer_Three.shape)

'''
This is the output layer 3,
consisting of columns [1,2,3], which are nothing but the three classes.
These are the confidence values for the respective classes.
'''

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
