'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Design and Analysis of Algorithms
Lab 01 - Sorting and Searching Algorithms
Date: 19/07/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Design and Analysis of Algorithms \n Lab 01 - Sorting and Searching Algorithms \n Date: 19/07/2023")

print("\n ############# ################ ####################")

#-------------------#
# Sorting Algorithm #
#-------------------#

import random as rnd

def GnomeSort(num_list, list_len):
    gnome_index = 0 #The currrent index location is set as the first element of the given num_list

    while gnome_index < list_len: #Running a loop till the gnome_index reaches the end of the list

        if gnome_index == 0: #If the current index value is 0, i.e the first element, the gnome_index moves one index forwards
            gnome_index = gnome_index + 1

        if num_list[gnome_index] >= num_list[gnome_index - 1]: #If the current element is greater than the previous element, the gnome_index moves forward
            gnome_index = gnome_index + 1

        else: #If the above is not true, the current element is swapped with the previous element and the gnome_index also goes back one step. This continues till the above is true.
            num_list[gnome_index], num_list[gnome_index-1] = num_list[gnome_index-1], num_list[gnome_index]
            gnome_index = gnome_index - 1
            
    return num_list
  
#list_of_num = [71,55,3,4,41,95,82,101,37,62,58,7,13,69,420]
list_of_num = []
list_limit = 25

for r in range(1, list_limit+1):
    list_of_num.append(int(rnd.randint(100,1000)))

print("\n This is the unsorted list that needs to be sorted:\n", list_of_num, '\n\n The above list has', list_limit, 'elements.')
  
sorted_list_of_num = GnomeSort(list_of_num, list_limit)

gnome_sorted = []

for i in sorted_list_of_num:
    gnome_sorted.append(i)

print("\n Sorting using GnomeSort:\n", gnome_sorted)

verific = sorted(list_of_num)

print("\n Verifying using built-in sort function:\n", verific)

#---------------------#
# Searching Algorithm #
#---------------------# 

def BinarySearch(list_of_stuff, search_this, ini, len_of_stuff):

    if ini <= len_of_stuff:
        
        midd = (len_of_stuff+ini) // 2

        if list_of_stuff[midd] == search_this:
            return midd

        elif list_of_stuff[midd] > search_this:
            return BinarySearch(list_of_stuff, search_this, ini, midd-1)

        else:
            return BinarySearch(list_of_stuff, search_this, midd-1, len_of_stuff)
    else:
        return -1 

List_of_stuff = []
maxi = 10

for m in range(1, maxi+1):
    List_of_stuff.append(int(rnd.randint(1,50)))

print("\n Random List of Numbers:\n", List_of_stuff)

find_this = int(input("\n Enter the number you need to search for in the above list: "))

ini = 0
len_of_stuff = len(List_of_stuff)-1

searching = BinarySearch(List_of_stuff, find_this, ini, len_of_stuff)

if searching != -1:
    print("\n The number is present at index", searching)

else:
    print("\n The number is not present in current list.")
    
# Charmingly Crafted By Redzwinger #