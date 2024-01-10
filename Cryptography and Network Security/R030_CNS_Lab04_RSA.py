'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 04
Date: 24/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 04 \n Date: 24/08/2023")

print("\n ############# ################ ####################\n")

import random as d20

# Function to convert letters to numbers
def letToNum(letters):
    numero = []    

    for x in letters:
        num = ord(x)
        numero.append(num)
    
    return numero

# Function to convert numbers to letters 
def NumToLet(num):
    sentence = str()

    for x in num:
        letter = chr(x)
        sentence = sentence + letter
   
    return sentence

# Function to generate prime numbers P and Q
def NovaPrime():
    x = 5555
    y = 9999
    prime_list = []
    
    while len(prime_list) < 12:
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
    PrimeQ = d20.choice(prime_list)
    
    while PrimeQ == PrimeP:
        PrimeQ = d20.choice(prime_list)
        break
        
    return PrimeP, PrimeQ

def pub_E_priv_D(PrimeP, PrimeQ):
    criteria = (PrimeP-1) * (PrimeQ-1)
    
    E = False

    while E == False:
        maybeE = list(a for a in range(2,criteria-1))
        
        for stuff in maybeE:
            possibilyE = d20.choice(maybeE)
     
            if (possibilyE/criteria != 0):
                pubE = possibilyE            
                priv_D = pow(pubE, -1, criteria)
                return pubE, priv_D
            else:
                continue


def private_D(PrimeP, PrimeQ, pubE):
    criteria = (PrimeP - 1) * (PrimeQ - 1)
    priv_D = pow(pubE, -1, criteria)

    return priv_D

def cipher(plaintext, pubKey, NNN):
    
    ciphertext = []
    for text in plaintext:
        cipherer = pow(text, pubKey, NNN)
        ciphertext.append(cipherer)
        
    return ciphertext

def decipher(ciphertext, privKey, NNN):
    decipheredtext = []

    for text in ciphertext:
        decipherer = pow(text, privKey, NNN)
        decipheredtext.append(decipherer)

    return decipheredtext

PrimeP, PrimeQ = NovaPrime()
print(" Prime P:", PrimeP,"\n Prime Q:", PrimeQ, end="\n\n")

PublicKeyE, PrivateKeyD = pub_E_priv_D(PrimeP, PrimeQ)
print(" Public Key E:", PublicKeyE, end="\n\n")
print(" Private Key D:", PrivateKeyD, end="\n\n")

test2 = str("Hello, I am Achintya Kamath AKA Redzwinger.") 

NNN = PrimeP * PrimeQ

numeroPlain = []
numeroPlain = letToNum(test2)
print(" Plaintext: \n ", test2, "\n\n Plaintext Converted to Numerals: \n ", numeroPlain, end="\n\n")

ciphertext = cipher(numeroPlain, PublicKeyE, NNN)
print(" Ciphertext: \n ", ciphertext, end="\n\n")

decipheredtext = decipher(ciphertext, PrivateKeyD, NNN)
print(" Deciphered Text: \n ", decipheredtext, end="\n\n")

plaint = NumToLet(decipheredtext)
print(" Converting back to plaintext: \n ", plaint, end="\n\n")

# Catastrophically Crafted by Redzwinger #


