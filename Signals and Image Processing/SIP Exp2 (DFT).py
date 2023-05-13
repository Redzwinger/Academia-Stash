'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Signals and Image Processing
Batch: B1
Date: 22/02/2023
Lab 2 (DFT)
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Signals and Image Processing\n Batch: B1 \n Date: 22/02/2023 \n Lab 2 (DFT)")

print("\n ############# ################ ####################\n")

import numpy as np
import cmath

global pi
pi = np.pi

global sin
sin = np.sin

global cos
cos = np.cos

# taking values of x(n) as input #
xn_in = (input("Please enter the space seperated values of x(n): ").split())

xn_dat = [round(float(i)) for i in xn_in]

print("\n", xn_dat)

def DFT(xn):

    twiddler = []

    for y in range(0, len(xn)):
        commie = []

        for d in xn:
            twiddle = (-2j*y*d)/len(xn)

            twiddling = int(cos(twiddle))
            mor_twiddling = int(sin(twiddle))

            commie.append(-1/len(xn)*complex(twiddling,mor_twiddling))

        twiddler.append(commie)

    return twiddler

def IDFT(xn):
    
    twiddler = []

    for y in range(0, len(xn)):
        commie = []

        for d in xn:
            twiddle = (-2j*y*d)/len(xn)

            twiddling = int(cos(twiddle))
            mor_twiddling = int(sin(twiddle))

            commie.append(-1/len(xn)*complex(twiddling,mor_twiddling))

        twiddler.append(commie)

    return twiddler

twiddling_em_matrix = DFT(xn_dat)

some_more_twiddling_em_matrix = IDFT(twiddling_em_matrix)

print(f"\n The Twiddle Factor Matrix of N for DFT = {len(xn_dat)}\n")

for blah in twiddling_em_matrix:
    print(blah)

print(f"\n The Twiddle Factor Matrix of N for IDFT = {len(xn_dat)}\n")

for blah in some_more_twiddling_em_matrix:
    print(blah)
