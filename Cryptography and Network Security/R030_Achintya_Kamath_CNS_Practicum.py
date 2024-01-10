'''
Omkar Iyer [R022], Achintya Kamath [R030], Rishabh Lalvani [R035]
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Practicum - Encryption using SHA 512
'''

# Info
print("\n ############# ################ ####################\n")

print(" Omkar Iyer [R022], Achintya Kamath [R030], Rishabh Lalvani [R035] \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Practicum - Encryption using SHA 512")

print("\n ############# ################ ####################\n")

import hashlib

# SHA-512 Function
def SHAAAAAAAAA(text):
    sha512 = hashlib.sha512()
    sha512.update(text.encode('utf-8'))
    return sha512.hexdigest()

# Encryption Function
def encrypt(text, key):
    hashy = SHAAAAAAAAA(key)
    cry = ""
    
    for i in range(len(text)):
        char = text[i]
        key_char = hashy[i % len(hashy)]
        
        cry_char = chr(ord(char) + ord(key_char))
        cry += cry_char
        
    return cry

# Decryption Function
def decrypt(cry, key):
    hashy = SHAAAAAAAAA(key)
    decry = ""
    
    for i in range(len(cry)):
        char = cry[i]
        key_char = hashy[i % len(hashy)]
        
        decry_char = chr(ord(char) - ord(key_char))
        decry += decry_char
        
    return decry

# Text to be encrypted 
test = "I hope this is simple enough for you kids -____-"
key = "THIS_IS_A_SECRET_KEY_DONT_SAY_IT_OUT_LOUD"

encrypt = encrypt(test, key)
decrypt = decrypt(encrypt, key)

print(" Original message:", test, end="\n\n")
print(" Encrypted message:", encrypt, end="\n\n")
print(" Decrypted message:", decrypt, end="\n\n")

