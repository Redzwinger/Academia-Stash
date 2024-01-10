'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 07
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 07 \n")

print("\n ############# ################ ####################\n")

import random as d20
import hashlib

# Function to convert letters to numbers
def letToNum(letters):
    numero = [ord(x) for x in letters]
    return numero

# Function to convert numbers to letters 
def NumToLet(num):
    sentence = ''.join(chr(x) for x in num)
    return sentence

# Function to generate prime numbers P and Q
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def NovaPrime():
    x = 5555
    y = 9999
    prime_list = []

    while len(prime_list) < 2:
        for i in range(x, y):
            if i == 0 or i == 1:
                continue
            else:
                for j in range(2, int(i/2) + 1):
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
    criteria = (PrimeP - 1) * (PrimeQ - 1)

    E = False

    while E == False:
        maybeE = list(a for a in range(2, criteria - 1))

        for stuff in maybeE:
            possibilyE = d20.choice(maybeE)

            if (possibilyE / criteria != 0):
                pubE = possibilyE
                privD = pow(pubE, -1, criteria)
                return pubE, privD
            else:
                continue

def private_D(PrimeP, PrimeQ, pubE):
    criteria = (PrimeP - 1) * (PrimeQ - 1)
    priv_D = pow(pubE, -1, criteria)
    return priv_D

def cipher(plaintext, pubKey, NNN):
    ciphertext = [pow(text, pubKey, NNN) for text in plaintext]
    return ciphertext

def decipher(ciphertext, privKey, NNN):
    decipheredtext = [pow(text, privKey, NNN) for text in ciphertext]
    return decipheredtext

def custom_hash(plaintext):
    # Create a SHA-256 hash of the plaintext
    sha256_hash = hashlib.sha256()
    sha256_hash.update(plaintext.encode())
    return sha256_hash.digest()

PrimeP, PrimeQ = NovaPrime()
print(" Prime P:", PrimeP,"\n Prime Q:", PrimeQ, end="\n\n")

PublicKeyE, PrivateKeyD = pub_E_priv_D(PrimeP, PrimeQ)
print(" Public Key E:", PublicKeyE, end="\n\n")
print(" Private Key D:", PrivateKeyD, end="\n\n")

test2 = "Hello, I am Achintya Kamath AKA Redzwinger."
print(" Message to be transferred: ", test2, end="\n\n")

NNN = PrimeP * PrimeQ

hash_value = custom_hash(test2)
combined_data = test2.encode() + hash_value
print( "Hash Value: ", hash_value, end="\n\n")

signature = cipher(combined_data, PrivateKeyD, NNN)
print(" Signature Generated: ", signature, end="\n\n")

received_combined_data = decipher(signature, PublicKeyE, NNN)

received_plaintext = received_combined_data[:-32]  # Assuming SHA-256 produces 32-byte hashes
received_hash = received_combined_data[-32:]

received_plaintext_bytes = bytes(received_plaintext)
received_hash_value = custom_hash(received_plaintext_bytes.decode())

if received_hash_value == received_hash:
    print(" MAC is valid. The message is authentic.")
else:
    print(" MAC is invalid. The message may have been tampered with.")
    
# Catastrophically Crafted by Redzwinger #

