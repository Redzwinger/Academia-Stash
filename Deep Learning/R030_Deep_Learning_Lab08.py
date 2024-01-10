'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Deep Learning
Lab 07
Date: 04/10/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Deep Learning \n Lab 07 \n Date: 04/10/2023")

print("\n ############# ################ ####################\n")

# importing stuff
import array
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split as tts
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPool2D, Dropout 
from keras.optimizers import SGD
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

# Loading fashion-mnist pre-shuffled train and test data

(xTrain, yTrain), (xTest, yTest) = tf.keras.datasets.fashion_mnist.load_data()

print(" Shape of Training (X): ",xTrain.shape)

imgRow, imgCol = 28,28

X_train_cnn = xTrain.reshape(xTrain.shape[0],imgRow,imgCol,1)
Y_train_cnn = yTrain

X_test_cnn = xTest.reshape(xTest.shape[0],imgRow,imgCol,1)
Y_test_cnn = yTest

print(" \n X Train CNN Shape: ", X_train_cnn.shape, end="\n")
print(" Y Train CNN Shape: ", Y_train_cnn.shape, end="\n\n")

img_index = 3
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

input_shape = (imgRow, imgCol, 1)

learn_this1 = 0.1
opti1 = SGD(learning_rate= learn_this1)

model_cnn = Sequential()
# Official Order of Layers -- 

model_cnn.add(Conv2D(32, (3,3), activation='relu', kernel_initializer='normal', input_shape=input_shape))
model_cnn.add(MaxPool2D(pool_size=(2, 2), strides=(1, 1), padding='valid'))
model_cnn.add(Dropout(0.25))
model_cnn.add(Flatten())
model_cnn.add(Dense(128,activation='leaky_relu', input_shape=input_shape))
model_cnn.add(Dropout(0.25))
model_cnn.add(Dense(10, activation='softmax', input_shape=input_shape))

model_cnn.compile(optimizer=opti1, loss='categorical_crossentropy', metrics= ['accuracy'])
history1 = model_cnn.fit(X_train_cnn, Y_train_cnn, validation_data=(X_test_cnn, Y_test_cnn), epochs=10, verbose=1)
score1 = model_cnn.evaluate(xTest,yTest)
model_cnn.summary()

print("\n\n For Learning Rate 0.1,", end="\n\n")
print("Test Loss: ", score1[0], end="\n\n")
print("Test Accuracy: ", score1[1], end="\n\n")
#print(plt.style.available)

plt.style.use('seaborn-darkgrid')
#plt.subplot(1,2,1)
plt.plot(history1.history['accuracy'])

#plt.subplot(1,2,2)
plt.plot(history1.history['val_accuracy'])

plt.title('Plot Accuracy [0.1]')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'])
plt.ylim(bottom=0)
plt.ylim(top=1.5)
plt.show()