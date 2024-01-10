'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Cryptography and Network Security
Lab 01
Date: XX/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Cryptography and Network Security \n Lab 01 \n Date: XX/08/2023")

print("\n ############# ################ ####################\n")

# Caesar Cipher

def caesar_salad(text, key, modulus):
    
    encrypted_text = ""
    
    for char in text:
        
        if char.isalpha():
            
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + key) % modulus) + ord('a'))
            
            if is_upper:
                
                encrypted_char = encrypted_char.upper()
                
            encrypted_text += encrypted_char
            
        else:
            
            encrypted_text += char
            
    return encrypted_text

def clear_the_plate(encrypted_text, key, modulus):
    
    decrypted_text = ""
    
    for char in encrypted_text:
        
        if char.isalpha():
            
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - key) % modulus) + ord('a'))
            
            if is_upper:
                
                decrypted_char = decrypted_char.upper()
                
            decrypted_text += decrypted_char
            
        else:
            
            decrypted_text += char
            
    return decrypted_text

text = "The name's Bond, James Bond."
text2 = "Hello"
key = 3
mod = 26

print(" --------------\n Caesar Cipher\n --------------", end="\n\n")

I_need_a_salad = caesar_salad(text, key, mod)
print(" Encrypted Text:", I_need_a_salad, end="\n\n")

thank_you_for_the_meal = clear_the_plate(I_need_a_salad, key, mod)
print(" Decrypted Text:", thank_you_for_the_meal, end="\n\n")

# Carefully Crafted By Redzwinger #

