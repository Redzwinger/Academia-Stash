'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Software Engineering
Lab 10-b
Date: 12/03/2024
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Software Engineering \n Lab 10-b \n Date: 19/03/2024")

print("\n ############# ################ ####################\n")

# Variable for Cyclometric #
cyclo = int(0) # Default #

# Input Stage #
x = int(input(" ENTER THE 1st NUMBER:  "))
y = int(input(" ENTER THE 2nd NUMBER:  "))
z = int(input(" ENTER THE 3rd NUMBER:  "))
# Input Takes 1 of Cyclo #
cyclo += 1
minVal, midVal, maxVal = int(), int(), int() # Initialization

# First IF will be checked #
cyclo += 1
if x < y and x < z:
    # Second If will also be Tested #
    cyclo += 1
    if y < z:
        minVal,midVal,maxVal = x,y,z
    else:
        cyclo += 1
        minVal,midVal,maxVal = x,z,y
elif y < x and y < z:
    cyclo += 1 # Because it Checked
    cyclo += 1 # For the First IF condition #
    if x < z:
        minVal,midVal,maxVal = y,x,z
    else:
        cyclo += 1
        minVal,midVal,maxVal = y,z,x
else:
    cyclo += 2 # For If and Elif #
    cyclo += 1 # For first IF
    if x < y:
        minVal,midVal,maxVal = z,x,y
    else:
        cyclo += 1
        minVal,midVal,maxVal = z,y,x

# Printing #
print (" THE NUMBERS IN ASCENDING ORDER IS ..... \n", minVal,midVal,maxVal )
print(f"\n Cyclometric Complexity is : {cyclo}")


