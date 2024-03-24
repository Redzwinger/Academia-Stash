'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Software Engineering
Lab 10-A
Date: 12/03/2024
'''

# Info about me and the practical
from math import e


print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Software Engineering \n Lab 10-A \n Date: 12/03/2024")

print("\n ############# ################ ####################\n")

print(" Task 1: Black Box Testing.")

print("\n ############# ################ ####################\n")

# Topic: FIA Super License #

'''
Parent Class:
'''

def Eligibility(points, age, seasons, name):
    
    if (points>= 40) and (age >= 18) and (age < 50) and (seasons >= 3):
        print(f"{name} is eligible.")
    
    elif(points == 39) and (age >= 18) and (age <= 50) and (seasons >= 3):
        print(f"{name}'s eligiblity is under review.")
    
    elif(points>= 40) and (age >= 48) and (age < 50) and (seasons >= 3):
        print(f"{name}'s eligiblity is under review.")

    elif(points>= 40) and (age >= 48) and (age < 50) and (seasons == 2):
        print(f"{name}'s eligiblity is under review.")
	
    elif(points>= 40) and (age >= 18) and (age <= 50) and (seasons <= 2):
        print(f"{name} is not eligible.")
	
    elif(points < 40) and (age >= 18) and (age <= 50) and (seasons >=3):
        print(f"{name} is not eligible.")
        
    elif(points < 40) and (age < 18) and (seasons >=3):
        print(f"{name} is not eligible.")
        
    elif(points < 40) and (age < 18) and (seasons >=3):
        print(f"{name} is not eligible.")

name = input(" Please enter the name of the driver: ")
points, age, seasons = input(" Please enter their points, age, and seasons: ").split()

Eligibility(int(points), int(age), int(seasons), name)

# Carefully Crafted By Redzwinger #