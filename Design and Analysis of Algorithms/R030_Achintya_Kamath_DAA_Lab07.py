'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 07
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 07")

print("\n ############# ################ ####################\n")

import sys

def find_min_cost_path_forward(graph, stages, s, t):
    n = len(stages)
    min_cost = [sys.maxsize] * n
    parent = [-1] * n
    
    min_cost[0] = 0
    parent[0] = -1
    
    for i in range(1, n):
        for j in range(i):
            for u, v, cost in graph:
                if v == stages[i] and u == stages[j]:
                    if min_cost[j] + cost < min_cost[i]:
                        min_cost[i] = min_cost[j] + cost
                        parent[i] = j
    
    path = []
    index = stages.index(t)
    while index != -1:
        path.append(stages[index])
        index = parent[index]
    
    path.reverse()
    
    return min_cost[n-1], path

graph = [(1, 2, 2), (1, 3, 5), (2, 4, 7), (2, 5, 3), (3, 5, 2), (3, 6, 6), (4, 7, 1), (5, 7, 8), (6, 7, 4)]
stages = [1, 2, 3, 4, 5, 6, 7]
source = 1
sink = 7

min_cost, path = find_min_cost_path_forward(graph, stages, source, sink)
print(" Minimum cost:", min_cost)
print(" Minimum cost path:", path)

# Charmingly Crafted By Redzwinger #

