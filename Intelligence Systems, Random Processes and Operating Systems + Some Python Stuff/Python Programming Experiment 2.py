'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B2
Date: 04/08/2022
'''
#1: Create a string "Hello World"

display_this="Hello World!"
print("\n\t*** ", display_this, " ***\n")

#2: Extract different characters of the created string and print

print("\t", display_this[1:5])

#3: Form a new string where the first and the last characters have been exchanged

display_this_too = display_this[-1:] + display_this[1:-1] + display_this[:1]
print("\n\t", display_this_too)

#4: Reverse of a string

print("\n\t", display_this[::-1],)

#5 Checking if a number is even, odd or prime

number = int(input("\n  Please Enter a number to check if its even or odd and to check if its a prime number: "))
check = number%2

if check > 0:
    print(f"\n\tThis is an odd number.")
else:
    print(f"\n\tThis is an even number.")

z = False

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            z = True
            break
    if z:
        print("\n\t",number, "is not a prime number")
    else:
        print("\n\t",number, "is a prime number", end="\n\n")
