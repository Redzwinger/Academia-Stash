'''
Constraint Satisfaction
Achintya Kamath R030
MBA Tech AI B2
'''

import constraint

#Implement a Constraint Satisfaction Problem (CSP) in Python for the following problem
#Find all (x,y) where x ∈ {1,2,3} and 0 <= y < 10, and x + y >= 5

print(f"\n\tThis program implements a Constraint Statifaction Problem.\n\n First it is implemented importing the python-constraint module.\n Next, it is implemented by nested loops.", end="\n")

print(f"\n\t#1 Using python-constraint module...", end="\n\n")

the_thing = constraint.Problem()

the_thing.addVariable('x', [1,2,3])
the_thing.addVariable('y', range(10))

def our_constraint(x, y):
    if x + y >= 5:
        return True

the_thing.addConstraint(our_constraint, ['x','y'])

the_end_thing = the_thing.getSolutions()

length = len(the_end_thing)
print(" (x,y) ∈ { ", end="")

for index, the_end_thing in enumerate(the_end_thing):
    if index == length - 1:
        print(" ({},{})".format(the_end_thing['x'], the_end_thing['y']), end=" ")
    else:
        print(" ({},{}),".format(the_end_thing['x'], the_end_thing['y']), end=" ")
print(" }")

print(f"\n\t#2 Using nested loops...", end="\n\n")

x = [1,2,3]
y = range(10)

ans =[]
a_thing = int

for a in x:
    for b in y:
        a_thing = a + b

        if a_thing >=5:
            ans.append((a,b))
        else:
            continue

ans.sort(reverse=True)

print(" (x,y) ∈ { ", ans, " }", end="\n\n")

