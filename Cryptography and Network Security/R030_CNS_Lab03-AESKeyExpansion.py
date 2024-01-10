'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 03 (Part One)
Date: 10/08/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 03 \n Date: 10/08/2023")

print("\n ############# ################ ####################\n")

'''
Somethings to keep in mind,
1 word = 4 bytes
1 byte = 8 bits

Here, for AES Key Generation,

4 Words are needed, i.e.,
4 Words = 16 bytes = 128 bits
'''

# Generating a Key to be used in AES Encryption #

# Using given temporary word, t

t = [0xAD20177D, 0x470678DB, 0x31DA48D0, 0x47AB5B7D, 0x6C762D20, 0x52C4F80D, 0xE4133523, 0x8CE29268, 0x0A5E4F61, 0x37C6CD99]

# The Cipher Key to be used is given as (24 75 A2 B3 34 75 56 88 31 E2 12 00 13 AA 54 87) in Hexadecimal

# Initial 128-bit key (16 bytes) as 4 words (32-bit each)
initial_key = [0x2475A2B3, 0x34755688, 0x31E21200, 0x13AA5487]

# AES Key Expansion function
def aes_key_expansion(initial_key, t):
    expanded_key = initial_key.copy()

    for i in range(4, 44):
        
        if i % 4 == 0:
            temp1 = expanded_key[i - 4] ^ t[(i // 4) - 1]
            expanded_key.append(temp1)
            
        else:
            temp = expanded_key[i - 1] ^ expanded_key[i - 4]
            expanded_key.append(temp)

    return expanded_key

# Converting to hexadecimal strings
def convert_to_hex_string_list(int_list):
    return [hex(num) for num in int_list]

# Main 
expanded_key = aes_key_expansion(initial_key, t)
hex_expanded_key = convert_to_hex_string_list(expanded_key)

print("\n Expanded Key (in Decimal):\n")
print(expanded_key)

print("\n Expanded Key (in Hexadecimal):\n")
print(hex_expanded_key)

# Crafted by Redzwinger #

