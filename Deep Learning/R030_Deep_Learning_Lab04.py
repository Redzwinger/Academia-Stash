'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 04
Date: 30/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 04 \n Date: 30/08/2023")

print("\n ############# ################ ####################\n")


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

        # Initializing weights and biases
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
        print(" For Learning Rate", learning_rate, ":", end="\n\n")
        loss_history = []
        accuracy_history = []

        for i in range(iterations):
            # Forward propagation
            predictions = self.forward(X)

            # Loss (MSE)
            loss = mean_squared_error(y, predictions)

            # Back propagation
            delta2 = (2 * (predictions - y) * predictions * (1 - predictions))
            dW2 = np.dot(self.a1.T, delta2)
            db2 = np.sum(delta2, axis=0, keepdims=True)
            delta1 = np.dot(delta2, self.W2.T) * self.a1 * (1 - self.a1)
            dW1 = np.dot(X.T, delta1)
            db1 = np.sum(delta1, axis=0, keepdims=True)

            # Updating weights and biases
            self.W1 -= learning_rate * dW1
            self.b1 -= learning_rate * db1
            self.W2 -= learning_rate * dW2
            self.b2 -= learning_rate * db2

            # Calculating accuracy
            correct_predictions = np.sum(np.argmax(predictions, axis=1) == np.argmax(y, axis=1))
            accuracy = correct_predictions / y.shape[0]

            # Appending loss and accuracy to the history
            loss_history.append(loss)
            accuracy_history.append(accuracy)
                   
# Initializing the neural network
input_size = 4
hidden_size = 2
output_size = 3

nn = NeuralNetwork(input_size, hidden_size, output_size)

iterations1 = 5100
iterations1_5 = 600

learning_rate1 = 0.01
learning_rate2 = 0.1
learning_rate3 = 0.2
learning_rate4 = 0.3
learning_rate5 = 0.4
learning_rate6 = 0.5

nn.train(dat_input.values, dat_output.values, learning_rate1, iterations1)
nn.train(dat_input.values, dat_output.values, learning_rate2, iterations1)
nn.train(dat_input.values, dat_output.values, learning_rate3, iterations1)
nn.train(dat_input.values, dat_output.values, learning_rate4, iterations1)
nn.train(dat_input.values, dat_output.values, learning_rate5, iterations1)
nn.train(dat_input.values, dat_output.values, learning_rate6, iterations1)

nn.train(dat_input.values, dat_output.values, learning_rate1, iterations1_5)
nn.train(dat_input.values, dat_output.values, learning_rate2, iterations1_5)
nn.train(dat_input.values, dat_output.values, learning_rate3, iterations1_5)
nn.train(dat_input.values, dat_output.values, learning_rate4, iterations1_5)
nn.train(dat_input.values, dat_output.values, learning_rate5, iterations1_5)
nn.train(dat_input.values, dat_output.values, learning_rate6, iterations1_5)

losses = []
accuracies = []

learning_rates = [learning_rate1, learning_rate2, learning_rate3, learning_rate4, learning_rate5, learning_rate6]

for learning_rate in learning_rates:
    loss_history, accuracy_history = nn.train(dat_input.values, dat_output.values, learning_rate, iterations1)
    losses.append(loss_history)
    accuracies.append(accuracy_history)

# Plot MSE loss for different learning rates
plt.figure()
for i, lr in enumerate(learning_rates):
    plt.plot(losses[i], label=f'LR={lr}')
plt.xlabel('Iterations')
plt.ylabel('MSE Loss')
plt.legend()
plt.title('MSE Loss for Different Learning Rates')
plt.show()

# Plot accuracy for different learning rates
plt.figure()
for i, lr in enumerate(learning_rates):
    plt.legend()
    plt.plot(accuracies[i], label=f'LR={lr}')
plt.xlabel('Iterations')
plt.ylabel('Accuracy')
plt.title(f"Accurracy")
plt.legend()
plt.show()

# Curiously Crafted by Redzwinger #