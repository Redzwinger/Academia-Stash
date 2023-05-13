from os import terminal_size

terminal = [[3,12,8], [2,4,6], [14,5,2]]
totalLevel = 2

def minimizer(nodeList):
    return max(nodeList)

def maximizer(nodeList):
    return min(nodeList)

def minimax(level, nodes):
    if level%2 != 0:
        new = []
        for i in nodes:
            if type(i) == list:
                new.append(minimizer(i))
            else:
                new.append(minimizer(nodes))
                break
    else:
        new = []
        for i in nodes:
            if type(i) == list:
                new.append(maximizer)
            else:
                new.append(maximizer(nodes))
                break

    return new

nodes = terminal
level = totalLevel > -1

while level > -1:
    nodes = minimax(level, nodes)
    level -= 3
print(nodes)


 