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
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
def Euclides(lst, thing, ter_data):
    for i in range(0, len(lst)):
            eud_dist = 0

            for b in range(0,thing):
                dist = abs(ter_data[b] - lst[i][b])
                eud_dist +=dist

            eud_dist = eud_dist**2

            return eud_dist    
'''

#custom knn function

def knn(lst,lstc,ter_data,k):

    # lst: data            #
    # lstc: Labels         #
    # ter_data: Point used #

    #First we find Euclidean Distance using the tertiary data as ref
    # Euclidiean Distance : sqrt((x-y)**2 + (y-x)**2

    thing = len(ter_data)

    # neighbour and label lists #

    neighbours = []
    label_neigh = []

    # iterating to get order #
    for y in range(0,k):
        near_neigh = None
        smol_dist = None
        
        # finding distance for each i #

        #eud_dist = Euclides(lst,thing,ter_data)
        for i in range(0, len(lst)):
            eud_dist = 0

            for b in range(0,thing):
                dist = (ter_data[b] - lst[i][b])
                eud_dist +=dist

            eud_dist = eud_dist**2

            # assigning neighbour based on the smallest distance #

            if smol_dist == None:
                    smol_dist = eud_dist
                    near_neigh = i
            elif smol_dist > eud_dist:
                    smol_dist = eud_dist
                    near_neigh = i

        # appending neighbour list #

        neighbours.append(lst[near_neigh])
        label_neigh.append(lstc[near_neigh])
        
        lst.remove(lst[near_neigh])
        label_neigh.remove(lstc[near_neigh])

    return label_neigh


'''
def k_nearest_neighbor(point, data, labels, k=3):
    
    # If two different labels are most found, continue to search for 1 more k
    while True:
        neighbor_labels = find_neighbors(point, data, labels, k=k)
        label = most_found(neighbor_labels)
        if label != None:
            break
        k += 1
        if k >= len(data):
            break
            
    return label
'''

# data list #
X = [[-1,1], [0,1], [0,2], [1,-1], [1,0]]

# Labels #
Y = ['N','P','N','N','P']

# Point specified #
ter_data = [1,1]

# K of KNN :P #
# Number of Neighbours to br found #
K = 3

found_it = knn(X,Y,ter_data, K)

print(found_it)
