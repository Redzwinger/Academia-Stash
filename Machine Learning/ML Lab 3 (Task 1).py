import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import seaborn as sns

'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 24/12/2022
Practical 3
B1_P1_030
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Practical 3 \n Machine Learning: Data Visualization Techniques")

print("\n ############# ################ ####################\n")

fig = plt.figure()
fig.set_figheight(5)
fig.set_figwidth(10)

#Plot a scatter plot for X (random numbers from 0 to 10) and Y (random numbers from 11 to 21). Save the scatter plot
X = []
Y = []

for i in range(9):
    one = random.randint(1, 10)
    two = random.randint(11, 20)
    X.append(one)
    Y.append(two)

print(" 1. Plot a scatter plot for X (random numbers from 0 to 10) and Y (random numbers from 11 to 21).\n Save the scatter plot.\n")
print(" X:", X,"\n Y:", Y, "\n\n Scatter Plot of X and Y:")

plt.subplot(1,2,1)
plt.title("Scatter Plot",fontsize=15,color="red")
plt.scatter(X,Y, color="xkcd:lime green")

#Create a subplot with different markers and different line colors.
variantX = []
variantY = []

for i in range(9):
    uno = random.randint(1,10)
    due = random.randint(11,20)
    variantX.append(uno)
    variantY.append(due)

print("\n 2. Create a subplot with different markers and different line colors.\n")
print(" Variant X:",variantX,"\n Variant Y:",variantY,"\n\n Scatter Plot of Variant X and Variant Y:")

plt.subplot(1,2,2)
plt.title("Variant Scatter Plot",fontsize=15,color="green")
plt.scatter(variantX,variantY,color="xkcd:blood red")
plt.show()

print("\n ############# ################ ####################\n")

#Plot a bar plot for below X and Y values.
# X= [2,8,10] Y= [11,16,9]

print(" 3. Plot a bar plot for below X and Y values. \n\n X= [2,8,10] \n Y= [11,16,9]\n")
print(" Bar Plot of X and Y:")

xy_df = pd.DataFrame({'Index': ['One', 'Two', 'Three'], 'X': [2,8,10], 'Y': [11,16,9]})

xy_df = xy_df.melt(id_vars='Index')

plotone = sns.barplot(data=xy_df, x='Index', y='value', hue='variable')

for p in plotone.containers:
    plotone.bar_label(p, fmt='%.1f', label_type='edge')

plt.show()

print("\n ############# ################ ####################\n")

#Plot a box plot for the values given below and state your inference.
# A= [3,4,5,7,9,8,12,13,7,8,19,90,12,15]

print(" 4. Plot a box plot for the values given below and state your inference.\n\n")
print(" A=[3,4,5,7,9,8,12,13,7,8,19,90,12,15]\n")
print(" Box Plot of X:")

fig = plt.figure()
fig.set_figheight(3)
fig.set_figwidth(9)

xdf = pd.DataFrame({'X': [3,4,5,7,9,8,12,13,7,8,19,90,12,15]})

sns.set_style('whitegrid')
sns.boxplot(x=xdf['X'])
plt.xticks(X)
plt.show()