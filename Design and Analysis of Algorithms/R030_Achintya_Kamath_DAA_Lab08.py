'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 08
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 08")

print("\n ############# ################ ####################\n")

class Graphy:
    
    # Default Stuff #
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []
        self.ini = 1
        
    # Adding Edges to the Graph #
    def add_edges(self, u, v, w):
        self.graph.append([u,v,w])
        #self.G.add_edge(u, v)
    
    # Printing the distances #
    def printstuff(self, disty):
        for v in range(self.V):
            print(" Vertex",v,"is at a distance of", disty[v], "from the Source Vertex.")
            
    # Main Bellman-Ford Algorithm #
    def Belly(self, sour, struc):
        
        # Initializing all weights as Infinity #
        disty = [float("Inf")] * self.V
        disty[sour] = 0
        
        # Starting to relax the edges V-1 times #
        for thing in range(self.V - 1):
            
            # Updating distance value and parent index of the adjacent vertices of the current vertex. #
            for u, v, w in self.graph:
                if disty[u] != float("Inf") and disty[u] + w < disty[v]:
                    disty[v] = disty[u] + w
                    self.ini +=1
                    
        for u, v, w, in self.graph:
            if disty[u] != float("Inf") and disty[u] + w < disty[v]:
                print(" ** WARNING ** This Graph contains a negative weight cycle.")
                return
        
        self.printstuff(disty)


g = Graphy(5) 

# Adding Edges and their weights to the Nodes/Vertices #
g.add_edges(0, 1, -1) # A-B
g.add_edges(0, 2, 4) # A-C
g.add_edges(1, 2, 3) # B-C
g.add_edges(1, 3, 1) # B-D
g.add_edges(1, 4, 2) # B-E
g.add_edges(3, 1, 1) # D-B
g.add_edges(3, 2, 5) # D-C
g.add_edges(4, 3, -3) # E-D

# Making a dictionary of the graph nodes and edges for plotting purposes #
struc = {0: [(0, 1), (0, 2)], 1: [(1, 2), (1, 3), (1, 4)], 3: [(3, 1), (3, 2)], 4: [(4, 3)]}

# Bellman-Ford Function with Source Vertex as 'A' or '0' #
g.Belly(0, struc)

# Charmingly Crafted By Redzwinger #

