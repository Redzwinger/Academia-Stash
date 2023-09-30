'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 02
Date: XX/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 02 \n Date: XX/08/2023")

print("\n ############# ################ ####################")

import random as dice
import cryptography as cy

# Generating a Key for DES Encryption

# Function for splitting a continuous string into 4 bits
def circular_shift(bin_str, shift):
    return bin_str[shift:] + bin_str[:shift]

# Function for key generation
def keyGen(iniKey):
    print(f"\n The randomly generated 64-Bit Key is:\n {iniKey}", end="\n\n")
    
    # Converting to Binary
    iniKey = format(iniKey, '064b')  # Ensure the key is 64 bits long
    
    print(f" The Key before Permutation Choice 1 Table:\n {iniKey}", end="\n\n")
    
    # Permutation Choice 1 Table
    PerChoiceTOne = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]

    # Applying Permutation Choice 1 Table
    PerKeyOne = ''.join(iniKey[i - 1] for i in PerChoiceTOne)
    
    print(f" {len(PerKeyOne)} Bits Key after Permutation Choice 1 Table:\n {PerKeyOne}", end="\n\n")
    
    # Splitting the key into two halves
    leftbits, rightbits = PerKeyOne[:28], PerKeyOne[28:]

    print(f" Splitting the Key into two halves,\n\n Left Half: {leftbits}\n Right Half is: {rightbits}", end="\n\n")

    # Shift Table
    schwifty = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    roundNumber = 1

    while roundNumber <= 16:
        # Performing circular shifting on both halves
        leftbits = circular_shift(leftbits, schwifty[roundNumber - 1])
        rightbits = circular_shift(rightbits, schwifty[roundNumber - 1])
        
        print(f" After circular shifting in round {roundNumber}:\n Left Half: {leftbits}\n Right Half is: {rightbits}", end="\n\n")
        
        roundNumber += 1

    # Concatenating and applying Permutation Choice 2 (PC-2) table to get the final subkey
    concatenated_key = leftbits + rightbits
    PerChoiceTtwo = [14, 17, 11, 24, 1, 5, 3, 28,
                     15, 6, 21, 10, 23, 19, 12, 4]
    
    final_key = ''.join(concatenated_key[i - 1] for i in PerChoiceTtwo)
    
    print(f" Final subkey after Permutation Choice 2 Table:\n {final_key}\n")

iKey = dice.getrandbits(64)  # Generates a 64 Bit Integer
keyGen(iKey)

# Contemplatively Crafted By Redzwinger #

