'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 09
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 09")

print("\n ############# ################ ####################\n")

def is_safe(graph, vertex, color, c):
    for neighbor in graph[vertex]:
        if c == color[neighbor]:
            return False
    return True

def graph_coloring_util(graph, m, color, v):
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, v, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = 0

    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    if graph_coloring_util(graph, m, color, 0):
        print(" Graph can be colored with at most", m, "colors.")
        print(" Vertex colors:", color)
    else:
        print(" Graph cannot be colored with at most", m, "colors.")

if __name__ == "__main__":
    graph = [
        [1, 2, 3],  # Neighbors of vertex 0
        [0, 2, 3],  # Neighbors of vertex 1
        [2, 1, 3],  # Neighbors of vertex 2
        [0, 1, 2],  # Neighbors of vertex 3
    ]
    m = 3  # Number of colors
    graph_coloring(graph, m)

# Charmingly Crafted By Redzwinger #

