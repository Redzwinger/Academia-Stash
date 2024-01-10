'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 05
Date: 14/09/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 05 \n Date: 14/09/2023")

print("\n ############# ################ ####################\n")

print(" Task 2: Man-In-The-Middle \n")

print(" ############# ################ ####################\n")

import random as d20

# Function to generate prime numbers P and Q
def NovaPrime():
    x = 0
    y = 100
    prime_list = []
    
    #while len(prime_list) < 12:
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
                
    PrimeP = d20.choice(prime_list)
    return PrimeP

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def RootPrime(modulo):    
    roots = []
    # Generating list with numbers leading up to the Prime Number
    Till_Prime = set(num for num in range (1, modulo) if gcd(num, modulo) == 1) 

    # Finding the primitive roots within the previously generated list
    for g in range(1, modulo):
        Actual_Root = set(pow(g, powers) % modulo for powers in range (1, modulo))
                
        if Till_Prime == Actual_Root:
            roots.append(g)   
    
    PrimRoot = d20.choice(roots)  
    return PrimRoot

def PreKeyGen(primeN, g):
    RandomX = d20.choice(range(1,100))
    A = (g**RandomX) % primeN
        
    RandomY = d20.choice(range(1,100))
    B = (g**RandomY) % primeN
    
    DecoyA, DecoyB = Middle_Man(primeN, g)
    
    KeyOne = KeyGen(primeN, DecoyB, RandomX)
    KeyTwo = KeyGen(primeN, DecoyA, RandomY)
    
    InterceptedKeyOne = KeyGen(primeN, B, RandomX)
    InterceptedKeyTwo = KeyGen(primeN, A, RandomY)

    return KeyOne, KeyTwo, InterceptedKeyOne, InterceptedKeyTwo

def KeyGen(AB, g, Rnd):
    Key= (g**Rnd) % AB
    return Key

def Middle_Man(RealN, RealG):
    MidX = d20.choice(range(1,100))
    MidY = d20.choice(range(1,100))
    
    MidA = (RealG**MidX) % (RealN)
    MidB = (RealG**MidY) % (RealN)
    
    return MidA, MidB
 
N = NovaPrime()
print(" Prime P:", N, end="\n")

G = RootPrime(N)
print(" Primitive Root G:", G, end="\n\n")

KeyOne, KeyTwo, ActualKeyOne, ActualKeyTwo = PreKeyGen(N, G)

print(" Symmetric Key 1:", KeyOne, end="\n")
print(" Symmetric Key 2:", KeyTwo, end="\n\n")

print(" Intercepted Symmetric Key 1:", ActualKeyOne, end="\n")
print(" Intercepted Symmetric Key 2:", ActualKeyTwo, end="\n\n")

# Cautiously Crafted By Redzwinger #

