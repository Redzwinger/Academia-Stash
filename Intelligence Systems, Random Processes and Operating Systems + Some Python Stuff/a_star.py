'''
A* Search
Achintya Kamath R030
MBA Tech AI B2
'''

import time
from collections import deque

print(f"\n\tThis program serves the purpose of showcasing the functioning of the A* / A-Star Search Algorithm", end="\n\n ")

class Search:

    def __init__(self, distance_betw_nodes):
        self.distance_betw_nodes = distance_betw_nodes

    def get_neighbors(self, v):
        return self.distance_betw_nodes[v]

    def h(self, n):
        Hueristic_val = {'A':21, 'B':14, 'C':18, 'D':18, 'E':5, 'F':8, 'Z':0}

        return Hueristic_val[n]

    def as_search(self, node_start, goal_node):
        open_list = set([node_start])
        closed_list = set([])

        thing = {}

        thing[node_start] = 0

        parents = {}
        parents[node_start] = node_start

        while len(open_list) > 0:
            n = None
            
            for v in open_list:
                if n == None or thing[v] + self.h(v) < thing[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            if n == goal_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(node_start)

                reconst_path.reverse()

                print('\n The Path is: {}'.format(reconst_path))
                print('\n The Current Open List is- ', open_list)
                print('\n The Current Close List is- ', closed_list, end="\n\n")
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    thing[m] = thing[n] + weight

                else:
                    if thing[m] > thing[n] + weight:
                        thing[m] = thing[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print('A Path does not exist for the current entered data.')
        return None

successor_nodes={'A':['B','C','D'], 'B':'E', 'C':['E', 'F'], \
'D':'F', 'E':'Z', 'F':'Z'}

distance_betw = {'A':[('B',9),('C',9),('D',9)], 'B':[('E',11)],'C':[('E',17),('F',12)], \
                   'D':[('F', 14)], 'E':[('Z',5)], 'F':[('Z',9)]}

total_distance = 9+11+5

search = Search(distance_betw)
search.as_search('A', 'Z')

print(' The total distance covered is: ',total_distance, end="\n\n" )
