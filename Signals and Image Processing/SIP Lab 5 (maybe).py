import numpy as np
import matplotlib.pyplot as plt
import cv2

'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Signals and Image Processing
Batch: B1
Date: 17/02/2023
Lab 5
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Signals and Image Processing\n Batch: B1 \n Date: 03/02/2023 \n Lab 5 - Histogram Equalization")

print("\n ############# ################ ####################\n")

# making a function to make and count histograms #

# this function can return two things depending on the "thing" #
# thing = 1: plots the histogram of the image                  #
# thing = 2: just returns the x and y values                   #

def history(img,thing):
    maximum_o_img = np.amax(img) + 1

    x = np.arange(0, maximum_o_img, dtype=int)
    y = np.zeros(maximum_o_img, dtype=int)

    for a in img:
        for h in a:
            y[h] += 1

    # ploting the histogram #
    if thing == 0:
        plt.subplot(2,1,1)
        plt.title("Image")
        plt.imshow(img, cmap='gray')
        plt.subplot(2,1,2)
        plt.xlabel('intensity value')
        plt.ylabel('number of pixels')
        plt.title("Histogram of the Image")
        plt.stem(x,y,linefmt="xkcd:light purple", markerfmt="xkcd:green")
        plt.show()
    else:
        return x and y
    

def Equalizer(img,thing):
    xv, yv = history(img,1)
    difY = np.zeros(256, dtype=int)

    Smax, Smin = int(0), int(255)

    Rmax = np.amin(img)
    Rmin = np.amax(img)

    Sv = []

    for i in xv:
        S = ((Smax - Smin)/(Rmax - Rmin))*(i - Rmin) + Smin
        Sv.append(S)

Image1 = cv2.imread("Fig0316(1)(top_left).tif", 0)
Image2 = cv2.imread("Fig0316(2)(2nd_from_top).tif", 0)
Image3 = cv2.imread("Fig0316(3)(third_from_top).tif", 0)
Image4 = cv2.imread("Fig0316(4)(bottom_left).tif", 0)

history(Image1,0)
history(Image2,0)
history(Image3,0)
history(Image4,0)
