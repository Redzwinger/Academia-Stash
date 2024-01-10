# importing stuff
import array
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import time

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

dat_input = final_df.iloc[:,0:4] # 150 x 4
dat_output = final_df.iloc[:,4:] # 150 x 3

print("\n\n Taking a look at the Input Data, \n\n", dat_input, "\n\n It's shape is found out to be", dat_input.shape, "\n\n Output Data: ", dat_output, end="\n\n")

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Initialize weights and biases
        self.W1 = np.random.rand(input_size, hidden_size)
        self.b1 = np.random.rand(1, hidden_size)
        self.W2 = np.random.rand(hidden_size, output_size)
        self.b2 = np.random.rand(1, output_size)

    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def train(self, X, y, learning_rate, iterations):
        print(" For Learning Rate 0.01:", end="\n\n")
        for i in range(iterations):
            # Forward propagation
            predictions = self.forward(X)

            # Calculate loss (MSE)
            loss = mean_squared_error(y, predictions)

            # Backpropagation
            delta2 = 2 * (predictions - y) * predictions * (1 - predictions)
            dW2 = np.dot(self.a1.T, delta2)
            db2 = np.sum(delta2, axis=0, keepdims=True)
            delta1 = np.dot(delta2, self.W2.T) * self.a1 * (1 - self.a1)
            dW1 = np.dot(X.T, delta1)
            db1 = np.sum(delta1, axis=0, keepdims=True)

            # Update weights and biases
            self.W1 -= learning_rate * dW1
            self.b1 -= learning_rate * db1
            self.W2 -= learning_rate * dW2
            self.b2 -= learning_rate * db2

            if i % 100 == 0:
                print(f" Iteration {i}, Loss: {loss:.4f}")
                
        words="Training Complete."
        delay = 0.1
        for word in words:
            print(word, end='', flush=True)
            
# Initializing the neural network
input_size = 4
hidden_size = 2
output_size = 3
learning_rate = 0.01
iterations = 5000

nn = NeuralNetwork(input_size, hidden_size, output_size)

# Training the neural network
nn.train(dat_input.values, dat_output.values, learning_rate, iterations)


# NEURAL NETWORK STUFF

'''
def neural_3(dat_input):

    # Setting Seed Value
    np.random.seed(13)

    # Setting Randomized Weights
    layer_1_weight_1 = np.random.rand(4,1)
    layer_1_weight_2 = np.random.rand(4,1)
    layer_1_weight_3 = np.random.rand(4,1)

    layer_1_Output_weight_1 = np.random.rand(2,1)
    layer_1_Output_weight_2 = np.random.rand(2,1)
    layer_1_Output_weight_3 = np.random.rand(2,1)

    print(" Layer Input Weights:\n\n ", )
    print(layer_1_weight_1, layer_1_weight_2, layer_1_weight_3)
    
    print(" Layer Output Weights:\n\n ")
    print(layer_1_Output_weight_1, layer_1_Output_weight_2, layer_1_Output_weight_3)

    # Asigning Biases #
    bias_one = np.random.rand(1)
    bias_two = np.random.rand(1)
    bias_three = np.random.rand(1)
    
    print("\n\n The Biases are : ", end="\n\n")
    print(bias_one, bias_two, bias_three)

    # Beginning the network
    Layer_1_Neuron_1 = np.dot(dat_input, layer_1_weight_1) + bias_one
    Layer_1_Neuron_2 = np.dot(dat_input, layer_1_weight_2) + bias_two
    Layer_1_Neuron_3 = np.dot(dat_input, layer_1_weight_3) + bias_three

    # Activation Function on Layer 1
    Layer_1_Output_1 = sigmoider(Layer_1_Neuron_1)
    Layer_1_Output_2 = sigmoider(Layer_1_Neuron_2)
    Layer_1_Output_3 = sigmoider(Layer_1_Neuron_3)

    Input_after_layer_1 = np.append(Layer_1_Output_1, Layer_1_Output_2, axis=1)
    Input_after_layer_1 = np.append(Input_after_layer_1, Layer_1_Output_3, axis=1)
    print("\n\n Layer Output:\n ", Input_after_layer_1, "\n\n With shape: ", Input_after_layer_1.shape)
'''

def neural_2(dat_input):

    # Setting Seed Value
    np.random.seed(13)

    # Setting Randomized Weights
    layer_1_weight_1 = np.random.rand(4,1)
    layer_1_weight_2 = np.random.rand(4,1)

    layer_1_Output_weight_1 = np.random.rand(2,1)
    layer_1_Output_weight_2 = np.random.rand(2,1)

    print(" Layer Input Weights:\n\n ", )
    print(layer_1_weight_1, layer_1_weight_2)
    
    print(" Layer Output Weights:\n\n ")
    print(layer_1_Output_weight_1, layer_1_Output_weight_2)

    # Asigning Biases #
    bias_one = np.random.rand(1)
    bias_two = np.random.rand(1)

    
    print("\n\n The Biases are : ", end="\n\n")
    print(bias_one, bias_two)

    # Beginning the network
    Layer_1_Neuron_1 = np.dot(dat_input, layer_1_weight_1) + bias_one
    Layer_1_Neuron_2 = np.dot(dat_input, layer_1_weight_2) + bias_two

    # Activation Function on Layer 1
    Layer_1_Output_1 = sigmoider(Layer_1_Neuron_1)
    Layer_1_Output_2 = sigmoider(Layer_1_Neuron_2)

    Input_after_layer_1 = np.append(Layer_1_Output_1, Layer_1_Output_2, axis=1)
    print("\n\n Layer Output:\n ", Input_after_layer_1, "\n\n With shape: ", Input_after_layer_1.shape)
    
    return Input_after_layer_1, Layer_1_Output_1, Layer_1_Output_2

def errorer(out1, out2, final_df):
    thing = False  

Layer1, L1output1, L1output2 = neural_2(dat_input)
Layer2, L2output1, L2output2 = neural_2(Layer1)


