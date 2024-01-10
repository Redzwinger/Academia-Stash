'''
Achintya Kamath [R030], Omkar Iyer [R022], Divyam Gupta [R021]
MBA Tech Artificial Intelligence
Subject: Computer Networks
Assignment 1
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Achintya Kamath [R030], Omkar Iyer [R022], Divyam Gupta [R021] \n Program: MBA Tech Artificial Intelligence \n Subject: Computer Networks \n Assignment 1")

print("\n ############# ################ ####################\n")

import random as d20

def inpu_gen():
	MSG = d20.randint(0,127)
	MSG = bin(MSG)
	MSG = MSG[2:]
	MSG = str(MSG)
	return MSG

def Redundant(msg_len):

	# Using the formula 2 ^ r >= m + r + 1 to calculate the number of redundant bits.
	for bits in range(msg_len):
		if(2**bits >= msg_len + bits + 1):
			return bits
		
def PowerPosition(inp, bits):

	# Placing bits at the positions which correspond to the power of 2.
	even_pari = 0
	odd_pari = 1
	inp_len = len(inp)
	bitmap = ''

	# If the position is a power of 2 insert '0'
	for i in range(1, inp_len + bits+1):
		if(i == 2**even_pari):
			bitmap = bitmap + '0'
			even_pari += 1
		else:
			bitmap = bitmap + inp[-1 * odd_pari]
			odd_pari += 1

	# reversing the array (m + r+1 ... 1)
	return bitmap[::-1]

def ParityBitsome(inp, bits):
	n = len(inp)

	# Finding rth parity bit
	for r in range(bits):
		tp = 0
		for j in range(1, n + 1):

			if(j & (2**r) == (2**r)):
				tp = tp ^ int(inp[-1 * j])

		# (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
		inp = inp[:n-(2**r)] + str(tp) + inp[n-(2**r)+1:]
	return inp

def Errorer(inp, bits):
	n = len(inp)
	error = 0

	# Calculating parity bits again
	for i in range(bits):
		tp = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				tp = tp ^ int(inp[-1 * j])

		# Creating binary by appending parity bits together.
		error = error + tp*(10**i)

	return int(str(error), 2)

def d20_to_get_error(bitmap, switches):
    bits = len(bitmap)
    bitmap = list(bitmap)
    
    replacements = d20.sample(range(0,bits),switches)
    
    for index in replacements:
        bitmap[index] = d20.choice(["0", "1"])
	
    return ("".join(bitmap))

# Data to be transmitted
MSG = inpu_gen()
msg_len = len(MSG)

# Calculating Redundant Bits
red_bits = Redundant(msg_len)

# Determining positions of the Redundant Bits
POS = PowerPosition(MSG, red_bits)

# Next, determining the parity bits
PAR_POS = ParityBitsome(POS, red_bits)

print(" Original Message:", MSG, end="\n\n")

print(" Transmitted as:", PAR_POS, end="\n\n") 

# Simulating Error by switching random bits
Error_Pari_POS = d20_to_get_error(PAR_POS, 6)
print(" Suppose there is an error:", Error_Pari_POS, end="\n\n")

FIX_IT = Errorer(Error_Pari_POS, red_bits)

if(FIX_IT==0):
	print(" There is no error in the received message.")
else:
	print(" WARNING! An error has been detected.\n Error is situated at", len(Error_Pari_POS)-FIX_IT+1 ,"positions from the left.", end="\n\n")
	
# Catastrophically Crafted by Redzwinger/Achintya Kamath
