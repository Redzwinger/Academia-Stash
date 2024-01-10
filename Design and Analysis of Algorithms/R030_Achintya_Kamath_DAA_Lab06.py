'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 06
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 06")

print("\n ############# ################ ####################\n")

def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    return min(left_min, right_min), max(left_max, right_max)

arr_example = [8, 12, 4, 17, 25, 1, 6, 10]
min_element, max_element = find_min_max(arr_example)
print(" Minimum element:", min_element)
print(" Maximum element:", max_element)

# Charmingly Crafted By Redzwinger #


