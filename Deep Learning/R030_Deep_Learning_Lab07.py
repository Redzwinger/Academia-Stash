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
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

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

# Sigmoid Function
def sigmoider(thing):
    return 1/(1+np.exp(-thing))

# Train Test Split
x_train, x_test, y_train, y_test = tts(dat_input, dat_output, test_size=0.33, random_state=42)

learn_this1 = 0.1

opti1 = SGD(learning_rate= learn_this1)

model1 = Sequential()
model1.add(Dense(32,activation='relu', input_shape=(4,)))
model1.add(Dense(32, activation='relu'))
model1.add(Dense(16, activation='relu'))
model1.add(Dense(3, activation='softmax'))

model1.compile(optimizer=opti1, loss='categorical_crossentropy', metrics= ['accuracy'])

history1 = model1.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, verbose=0)
score1 = model1.evaluate(x_test,y_test)

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

learn_this2 = 0.01

opti2 = SGD(learning_rate= learn_this2)

model2 = Sequential()
model2.add(Dense(32,activation='relu', input_shape=(4,)))
model2.add(Dense(32, activation='relu'))
model2.add(Dense(16, activation='relu'))
model2.add(Dense(3, activation='softmax'))

model2.compile(optimizer=opti2, loss='categorical_crossentropy', metrics= ['accuracy'])

history2 = model2.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, verbose=0)
score2 = model2.evaluate(x_test,y_test)

print("\n\n For Learning Rate 0.01,", end="\n\n")
print("Test Loss: ", score2[0], end="\n\n")
print("Test Accuracy: ", score2[1], end="\n\n")
#print(plt.style.available)

plt.style.use('seaborn-darkgrid')
#plt.subplot(1,2,1)
plt.plot(history2.history['accuracy'])

#plt.subplot(1,2,2)
plt.plot(history2.history['val_accuracy'])

plt.title('Plot Accuracy [0.01]')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'])
plt.ylim(bottom=0)
plt.ylim(top=1.5)
plt.show()

learn_this3 = 0.001

opti3 = SGD(learning_rate= learn_this3)

model3 = Sequential()
model3.add(Dense(32,activation='relu', input_shape=(4,)))
model3.add(Dense(32, activation='relu'))
model3.add(Dense(16, activation='relu'))
model3.add(Dense(3, activation='softmax'))

model3.compile(optimizer=opti3, loss='categorical_crossentropy', metrics= ['accuracy'])

history3 = model3.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, verbose=0)
score3 = model3.evaluate(x_test,y_test)

print("\n\n For Learning Rate 0.001,", end="\n\n")
print("Test Loss: ", score3[0], end="\n\n")
print("Test Accuracy: ", score3[1], end="\n\n")
#print(plt.style.available)

plt.style.use('seaborn-darkgrid')
#plt.subplot(1,2,1)
plt.plot(history3.history['accuracy'])

#plt.subplot(1,2,2)
plt.plot(history3.history['val_accuracy'])

plt.title('Plot Accuracy [0.001]')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'])
plt.ylim(bottom=0)
plt.ylim(top=1.5)
plt.show()

learn_this4 = 0.0001

opti4 = SGD(learning_rate= learn_this4)

model4 = Sequential()
model4.add(Dense(32,activation='relu', input_shape=(4,)))
model4.add(Dense(32, activation='relu'))
model4.add(Dense(16, activation='relu'))
model4.add(Dense(3, activation='softmax'))

model4.compile(optimizer=opti4, loss='categorical_crossentropy', metrics= ['accuracy'])

history4 = model4.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, verbose=0)
score4 = model4.evaluate(x_test,y_test)

print("\n\n For Learning Rate 0.0001,", end="\n\n")
print("Test Loss: ", score4[0], end="\n\n")
print("Test Accuracy: ", score4[1], end="\n\n")
#print(plt.style.available)

plt.style.use('seaborn-darkgrid')
#plt.subplot(1,2,1)
plt.plot(history4.history['accuracy'])

#plt.subplot(1,2,2)
plt.plot(history4.history['val_accuracy'])

plt.title('Plot Accuracy [0.0001]')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend(['train', 'test'])
plt.ylim(bottom=0)
plt.ylim(top=1.5)
plt.show()

learn_thisBest = 0.1

opti5 = SGD(learning_rate= learn_thisBest, momentum=0)

model5 = Sequential()
model5.add(Dense(32,activation='relu', input_shape=(4,)))
model5.add(Dense(32, activation='relu'))
model5.add(Dense(16, activation='relu'))
model5.add(Dense(3, activation='softmax'))

model5.compile(optimizer=opti5, loss='categorical_crossentropy', metrics= ['accuracy'])

history5 = model5.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=100, verbose=0)
score1 = model5.evaluate(x_test,y_test)

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