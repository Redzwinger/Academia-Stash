'''
1. Given an integer k, perform the following task using if-else statements

    a.Print whether k is negative or positive

    b.Print whether k is even or odd

    c.Print whether k is multiple of three
'''

k = int(input("Enter value of K: "))

#Positive or Negative
if k >0:
    print(k, "is a positive number")
elif k == 0:
    print(k, "is neither negative nor positive")
else:
    print(k, "is negative.")

#Even or Odd
if k%2 == 0:
    print(k, "is an even number")
else:
    print(k, "is an odd number")

#Multiple of 3
if k%3 == 0:
    print(k, "is a multiple of 3\n")
else:
    print(k, "is not a multiple of 3\n")

"""
2. For an examination conducted in a university, grade the marks obtained by the students as High, Medium, Low based on the following criteria

    i) High: 75< Marks<=100

    ii) Medium: 50<Marks<=75
    
    iii) Low: Marks<=50
"""

marks= input("Enter your marks between 1 to 100: ")
marks=int(marks)
if marks<=50:
  print("Grade: Low :(\n")
elif 50<marks<=75:
  print("Grade: Medium :)\n")
elif 75<marks<=100:
  print("Grade: High :D\n")
else:
    print("Grade: N/A x_x\n")

"""
3. Geeta and Seeta are playing a number game, where for every iteration a random number (1 to 50) will be generated first for Geeta and then for Seeta. Input the number of iterations to be played from the user. They get points as follows:

    i.For every even number, 2 point

    ii.For every odd number, 3 points

    iii.For every square number (even or odd), 4 points

Print the points obtained by Geeta and Seeta
"""

import random as rng

iterations = int(input("Please Input the Number Of Iterations to be done: "))
geeta, seeta = int(), int()

for i in range(iterations):
    a1 = int(rng.randrange(1,51))
    a2 = int(rng.randrange(1,51))

    if a1 in [4,9,16,25,36,49]:
        geeta +=4
    else:
        if a1 % 2 == 0:
            geeta +=2
        else:
            geeta +=2

    if a2 in [4,9,16,25,36,49]:
        seeta +=4
    else:
        if a2 % 2 == 0:
            seeta +=2
        else:
            seeta +=2

print("\nTotal Points")
print(f"Geeta's Points : {geeta}")
print(f"Seeta's Points : {seeta}")


