'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 07
Date: 28/02/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 07 \n Date: 28/02/2024")

print("\n ############# ################ ####################\n")

print(" Task 2-3-4: Exploring PySwarms and Training a neural network using PSO")

print("\n ############# ################ ####################\n")

import numpy as np
import matplotlib.pyplot as plt
import pyswarms as ps
from sklearn.datasets import load_iris

def logits_function(p):

    W1 = p[0:80].reshape((n_inputs,n_hidden))
    b1 = p[80:100].reshape((n_hidden,))
    W2 = p[100:160].reshape((n_hidden,n_classes))
    b2 = p[160:163].reshape((n_classes,))

    # Forward Propagation
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)     
    logits = a1.dot(W2) + b2
    
    return logits

# Forward propagation
def forward_prop(params):

    logits = logits_function(params)

    # Softmax
    exp_scores = np.exp(logits)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

    # Negative Log Likelihood
    corect_logprobs = -np.log(probs[range(num_samples), y])
    loss = np.sum(corect_logprobs) / num_samples

    return loss

def f(x):
    n_particles = x.shape[0]
    j = [forward_prop(x[i]) for i in range(n_particles)]
    
    return np.array(j)


def predict(pos):

    logits = logits_function(pos)
    y_pred = np.argmax(logits, axis=1)
    
    return y_pred

IRIS = load_iris()
X = IRIS.data
y = IRIS.target

n_inputs = 4
n_hidden = 20
n_classes = 3

num_samples = 150

# Initializing the swarm
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}

# Calling instance of PSO
dimensions = (n_inputs * n_hidden) + (n_hidden * n_classes) + n_hidden + n_classes
optimizer = ps.single.GlobalBestPSO(n_particles=100, dimensions=dimensions, options=options)

# Performing optimization
cost, pos = optimizer.optimize(f, iters=1000)

(predict(pos) == y).mean()

# Catatonically Crafted by Redzwinger #