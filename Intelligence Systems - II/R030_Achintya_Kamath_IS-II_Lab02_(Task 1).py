'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Intelligence Systems - II
Lab 02
Date: 20/12/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Intelligence Systems - II \n Lab 02 \n Date: 20/12/2023")

print("\n ############# ################ ####################\n")

print(" Task 1\n")

print(" ############# ################ ####################\n")

from pgmpy.base import *

GRAPH = DAG()
nody = ['A', 'B', 'C', 'D']

GRAPH.add_nodes_from(nodes=nody)

GRAPH.add_edges_from(ebunch=[('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])

print(f" G is a {GRAPH}\n with {GRAPH.nodes} nodes\n and {GRAPH.edges} edges.", end="\n\n")

# active_trail_nodes() #
print(" --------------------- \n\n active_trail_nodes() \n\n ---------------------")

for i in nody:
    prn = GRAPH.active_trail_nodes(i)
    print(f" The node '{i}' has the following active trail nodes: {prn}")
    
# get_ancestral_graph() #
print("\n --------------------- \n\n get_ancestral_graph() \n\n ---------------------")

for a in nody:
    pr = GRAPH.get_ancestral_graph(a)
    print(f" Node '{a}': {pr}")
    
# get_children() #
print("\n --------------------- \n\n get_children() \n\n ---------------------")

for c in nody:
    go = GRAPH.get_children(c)
    print(f" Node '{c}' has the child nodes {go}")
    
# get_independencies() #
print("\n --------------------- \n\n get_independencies() \n\n ---------------------")

for ind in nody:
    indie = GRAPH.get_independencies(ind)
    print(f" Node '{ind}' has the following independencies: {indie}")
    
# get_leaves() and get_parents() #
print("\n ------------------------------- \n\n get_leaves() and get_parents() \n\n -------------------------------")

leaf = GRAPH.get_leaves()
print(f" The Graph has the following leaves and parents, \n Leaves: {leaf}\n\n Parents: ")

for p in nody:
    par = GRAPH.get_parents(p)
    print(f" Node '{p}': {par}")
    
# get_roots() #
print("\n --------------------- \n\n get_roots() \n\n ---------------------")
root = GRAPH.get_roots()
print(f" The Graph has the following roots: {root}")

# to_graphviz() #
print("\n --------------------- \n\n to_graphviz() \n\n ---------------------")

print(" Pygraphviz doesn't work :)\n")

# Catestrophically Crafted by Redzwinger #

    