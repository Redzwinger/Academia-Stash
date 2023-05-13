'''
Best First Search
Achintya Kamath R030
MBA Tech AI B2
'''

import time

startTime=time.time()

distance_of_the_nodes={'A':21, 'B':14, 'C':18, 'D':18, 'E':5, 'F':8, 'Z':0}

successor_nodes={'A':['B','C','D'], 'B':'E', 'C':['E', 'F'], \
'D':'F', 'E':'Z', 'F':'Z'}

distance_betw_the_nodes={'A':[('B',9),('C',9),('D',9)], 'B':[('E',11)],'C':[('E',17),('F',12)], \
                   'D':[('F', 14)], 'E':[('Z',5)], 'F':[('Z',9)]}

print(f"\n\tThis program serves the purpose of showcasing the functioning of a Best First Search Algorithm", end="\n\n ")

node_start, node_goal= input('Please enter the start node and goal node to calculate the distance covered and the path taken in each step: ').split()

def explore(current):

  a_thing=[]

  for node in successor_nodes[current]:

    a_thing. append((node, distance_of_the_nodes[node]))
    return(a_thing)

open=[(node_start, distance_of_the_nodes[node_start])]
close=[]

distance_covered=0

while open:

  current=open[0][0] 
  print("\n The current node is:", current)

  if current==node_goal:

    print("\n The Goal Node has been reached!, The total distance covered is:",distance_covered, end="\n\n ")
    close.append(open[0]) 
    open.pop(0)
    break

  else:

    close.append(open[0])
    open.pop(0)
    open.extend(explore(current))
    open=sorted(open, key=lambda x: x[1])

    distance=[item[1] for item in distance_betw_the_nodes[current] if item[0]==open[0][0]]

    distance_covered=distance_covered = distance[0]

    print('\n Current OpenList: ', open)
    print('\n Current CloseList: ', close)

    endTIme=time.time()
