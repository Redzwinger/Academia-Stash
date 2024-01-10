'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 06
Date: 05/10/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 06 \n Date: 05/10/2023")

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

def signature(message, privKey, NNN):
    message_num = letToNum(message)
    signature = []

    for num in message_num:
        sig = pow(num, privKey, NNN)
        signature.append(sig)

    return signature

def verify(signature, pubKey, NNN):
    verified_message_num = []

    for sig in signature:
        num = pow(sig, pubKey, NNN)
        verified_message_num.append(num)

    verified_message = NumToLet(verified_message_num)
    return verified_message

PrimeP, PrimeQ = NovaPrime()
print(" Prime P:", PrimeP,"\n Prime Q:", PrimeQ, end="\n\n")

PublicKeyE, PrivateKeyD = pub_E_priv_D(PrimeP, PrimeQ)
print(" Public Key E:", PublicKeyE, end="\n\n")
print(" Private Key D:", PrivateKeyD, end="\n\n")

test2 = str("Hello, I am Achintya Kamath AKA Redzwinger.") 

NNN = PrimeP * PrimeQ

signature = signature(test2, PrivateKeyD, NNN)

# Verify the signature using the public key
verified_message = verify(signature, PublicKeyE, NNN)

print("Original Message: \n", test2, "\n")
print("Digital Signature: \n", signature, "\n")
print("Verified Message: \n", verified_message, "\n")

# Catastrophically Crafted by Redzwinger #

