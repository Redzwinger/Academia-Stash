'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 05
Date: 27-09-2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 05 \n Date: 27/09/2023")

print("\n ############# ################ ####################\n")

# Merge Sort using Divide and Conquer

intact = [9,5,7,5,1,8]
Merg = []

#while len(Merg) != len(intact):
broken1 = intact[:1]
broken2 = intact[1:3]
detached1 = intact[3:4]
detached2 = intact[4:]
    
print(broken1, broken2, detached1, detached2)

newbroken2 = []
if broken2[0] > broken2[1]:
    newbroken2[0::] = broken2[1], broken2[0]
    
    if broken1[0] < newbroken2[0] and newbroken2[1]:
        part1 = []
        part1.append(broken1[0])
        part1.append(newbroken2[0])
        part1.append(newbroken2[1])
        print(part1)
        
    elif broken1[0] > newbroken2[0] and broken1[0] < newbroken2[1]:
        part1 = []
        part1.append(newbroken2[0])
        part1.append(broken1[0])
        part1.append(newbroken2[1])
        print(part1)
        
    elif broken1[0] > newbroken2[0] and newbroken2[1]:
        part1 = []
        part1.append(newbroken2[0])
        part1.append(newbroken2[1])
        part1.append(broken1[0])
        print(part1)

elif broken2[0] < broken2[1]:
    
    if broken1[0] < broken2[0] and broken2[1]:
        part1 = []
        part1.append(broken1[0])
        part1.append(broken2[0])
        part1.append(broken2[1])
        print(part1)
        
    elif broken1[0] > broken2[0] and broken1[0] < broken2[1]:
        part1 = []
        part1.append(broken2[0])
        part1.append(broken1[0])
        part1.append(broken2[1])
        print(part1)
        
    elif broken1[0] > broken2[0] and broken2[1]:
        part1 = []
        part1.append(broken2[0])
        part1.append(broken2[1])
        part1.append(broken1[0])
        print(part1)

newdetached2 = []
if detached2[0] > detached2[1]:
    newdetached2[0::] = detached2[1], detached2[0]
    
    if detached1[0] < newdetached2[0] and newdetached2[1]:
        part2 = []
        part2.append(detached1[0])
        part2.append(newdetached2[0])
        part2.append(newdetached2[1])
        print(part2)
        
    elif detached1[0] > newdetached2[0] and detached1[0] < newdetached2[1]:
        part2 = []
        part2.append(newdetached2[0])
        part2.append(detached1[0])
        part2.append(newdetached2[1])
        print(part2)
        
    elif detached1[0] > newdetached2[0] and newdetached2[1]:
        part2 = []
        part2.append(newdetached2[0])
        part2.append(newdetached2[1])
        part2.append(detached1[0])
        print(part2)

elif detached2[0] < detached2[1]:
    
    if detached1[0] < detached2[0] and detached2[1]:
        part2 = []
        part2.append(detached1[0])
        part2.append(detached2[0])
        part2.append(detached2[1])
        print(part2)
        
    elif detached1[0] > detached2[0] and detached1[0] < detached2[1]:
        part2 = []
        part2.append(detached2[0])
        part2.append(detached1[0])
        part2.append(detached2[1])
        print(part2)
        
    elif detached1[0] > detached2[0] and detached2[1]:
        part2 = []
        part2.append(detached2[0])
        part2.append(detached2[1])
        part2.append(detached1[0])
        print(part2)
        
        
            
    
    
    







# Conservatively Crafted By Redzwinger #