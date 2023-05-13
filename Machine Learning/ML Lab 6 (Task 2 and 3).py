'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 18/02/2022
Machine Learning
Lab 6
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Date: 18/02/2022 \n Lab 6 \n Machine Learning: KNN (Custom Function)")

print("\n ############# ################ ####################\n")

# importing stuff

# importing stuff
import numpy as np
import pandas as pd

# Creating a dataframe by reading the .csv
social_advert = pd.read_csv("Social_Network_Ads.csv")

# Exploring the csv using pd functions

print(" Some information about the dataframe: \n\n", social_advert.describe())

print("\n First 10 entries in the dataframe: \n\n", social_advert.head(10))

print("\n", social_advert.size, "is the size of the dataframe.")

# Input Features & Output Features

print("\n The Input features are: Gender, Age, EstimatedSalary.")
print("\n Output features are: Purchased.")

# Number of classes in the output feature

print("\n There are 2 classes of the output feature 'Purchased'.")

# Removing columns not useful with classification

social_advert_classy = social_advert.drop(['User ID'], axis=1)

print("\n Columns unneeded in classification are removed. The dataframe now is, \n\n",social_advert_classy)

# Converting categorical columns into numerical columns

cat_isa_num = []

for c in social_advert_classy.index:

    if social_advert_classy['Gender'][c] == "Female":
        cat_isa_num.append(int(0))

    elif social_advert_classy['Gender'][c] == "Male":
        cat_isa_num.append(int(1))

    else:
        cat_isa_num.append(int(14))

social_advert_classy = social_advert.drop(['Gender'], axis=1)

social_advert_classy['Gender'] = cat_isa_num

print("\n The categorial columns have been converted to numerical as can be seen below, \n\n", social_advert_classy)

# Applying Standard Scalar Transformation

from sklearn.preprocessing import StandardScaler as ss
scaler = ss()
scaler.fit(social_advert_classy)
print("\n The Standard Scaler of the dataframe is, \n\n", scaler.transform(social_advert_classy))

##---------------------------------------------##
##--- Program by Achintya Kamath/Redzwinger ---##
##---------------------------------------------##