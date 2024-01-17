
##--Meticulously Crafted by Redzwinger--##
##---(Please do not steal my work <3)---##

# Code 1 #
'''
T = int(input()) #number of test cases

for i in T:
    N = int(input()) #size of array
    A = list(map(int,input().split())) #array
'''   
# Code 2 #
'''
n, q = map(int, input().split()) #family members and queries

tree_edge = [[] for i in range(n+1)] #storing tree_edges

for i in range(n-1):
    a, b = map(int, input().split())
    tree_edge[a].append(b)
    tree_edge[b].append(a)

tree_size = [None] * (n+1)
thing = [(1, 0)]

while thing:
    node, depth = thing.pop()
    tree_size[node] = depth

    for c in tree_edge[node]:
        if tree_size[c] is None:
            thing.append((c, depth+1))

# Processing queries
for i in range(q):
    a, b = map(int, input().split())

    depth_a = tree_size[a]
    depth_b = tree_size[b]

    if depth_a < depth_b:
        a, b = b, a
        depth_a, depth_b = depth_b, depth_a

    age_differ = 20 * (depth_a + depth_b) - 2 * 20 * depth_b
    print(age_differ)
'''

n, q = map(int, input().split()) #family members and queries
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# Computing depths and parents of all nodes
depths = [None] * (n+1)
parents = [None] * (n+1)
stack = [(1, 0, None)]
while stack:
    node, depth, parent = stack.pop()
    depths[node] = depth
    parents[node] = parent
    for child in tree[node]:
        if depths[child] is None:
            stack.append((child, depth+1, node))

# Processing queries
for i in range(q):
    a, b = map(int, input().split())
    depth_a = depths[a]
    depth_b = depths[b]
    parent_a = a
    parent_b = b
    while depth_a > depth_b:
        parent_a = parents[parent_a]
        depth_a -= 1
    while depth_b > depth_a:
        parent_b = parents[parent_b]
        depth_b -= 1
    while parent_a != parent_b:
        parent_a = parents[parent_a]
        parent_b = parents[parent_b]
    age_diff = 20 * (depths[a] + depths[b] - 2 * depths[parent_a])
    print(age_diff)





    # Reading input
n, q = map(int, input().split())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# Computing depths of all nodes
depths = [None] * (n+1)
stack = [(1, 0)]
while stack:
    node, depth = stack.pop()
    depths[node] = depth
    for child in tree[node]:
        if depths[child] is None:
            stack.append((child, depth+1))

# Processing queries
for i in range(q):
    a, b = map(int, input().split())
    depth_a = depths[a]
    depth_b = depths[b]
    if depth_a < depth_b:
        a, b = b, a
        depth_a, depth_b = depth_b, depth_a
    diff = depth_a - depth_b
    age_diff = 20 * diff
    while diff > 0:
        a = tree[a][0]
        diff -= 1
    while a != b:
        a = tree[a][0]
        b = tree[b][0]
        age_diff -= 40
    print(age_diff)

