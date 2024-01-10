'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 05
Date: 13/09/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 05 \n Date: 13/09/2023")

print("\n ############# ################ ####################\n")

import keras
from keras.api._v2.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

# Loading fashion-mnist pre-shuffled train and test data

(xTrain, yTrain), (xTest, yTest) = tf.keras.datasets.fashion_mnist.load_data()

print(" Shape of Training (X): ",xTrain.shape)

fashion_mnist_labels = ["T-shirt/top", 
                        "Trouser", 
                        "Pullover", 
                        "Dress", 
                        "Coat", 
                        "Sandal", 
                        "Shirt", 
                        "Sneaker", 
                        "Bag", 
                        "Ankle Boot"]

imgRow, imgCol = 28,28

# MLP Protocol

xTrain_mlp = xTrain.reshape(xTrain.shape[0], imgRow*imgCol)
yTrain_mlp = yTrain

xTest_mlp = xTest.reshape(xTest.shape[0], imgRow*imgCol)
yTest_mlp = yTest

# Shape of MLP

print(" \n MLP Shape (X): ", xTrain_mlp.shape, end="\n")
print(" MLP Shape (Y): ", yTrain_mlp.shape, end="\n\n")

X_train_cnn = xTrain.reshape(xTrain.shape[0],imgRow,imgCol,1)
Y_train_cnn = yTrain

X_test_cnn = xTest.reshape(xTest.shape[0],imgRow,imgCol,1)
Y_test_cnn = yTest

print(" \n X Train CNN Shape: ", X_train_cnn.shape, end="\n")
print(" Y Train CNN Shape: ", Y_train_cnn.shape, end="\n\n")

img_index = 13
label_index = yTrain[img_index]
print(f" Label Index, Y = {label_index}", end="\n\n")

plt.imshow(xTrain[img_index])
plt.show()

X_train_cnn = X_train_cnn.astype('float32')
X_test_cnn = X_test_cnn.astype('float32')
X_train_cnn /= 255
X_test_cnn /= 255

num_classes = 10
Y_train_cnn = keras.utils.to_categorical(Y_train_cnn,num_classes)
Y_test_cnn = keras.utils.to_categorical(Y_test_cnn,num_classes)

print(" ", Y_train_cnn[:5,:], end="\n\n")

learn_this1 = 0.1
opti = SGD(learning_rate= learn_this1)

model = Sequential()
model.add(Dense(128, activation='relu', input_shape=(imgRow*imgCol,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(optimizer=opti, loss='categorical_crossentropy', metrics= ['accuracy'])

history1 = model.fit(xTrain_mlp, Y_train_cnn, validation_data=(xTest_mlp, Y_test_cnn), epochs=100, verbose=1)
score1 = model.evaluate(xTest_mlp,Y_test_cnn)

history = model.fit(X_train_cnn, Y_train_cnn, epochs=10, validation_data=(X_test_cnn, Y_test_cnn))

# Charmingly Crafted By Redzwinger #