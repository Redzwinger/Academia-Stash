
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Signals and Image Processing
Batch: B1
Lab 3
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Subject: Signals and Image Processing \n Lab 3 - Spatial Resolution")

print("\n ############# ################ ####################\n")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL

# reading the original image

image = cv2.imread("cameraman.png")

'''
cv2.imshow("Orignal Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

# finding the array size of the image #

size_o_im = np.shape(image)

print(size_o_im, "is the shape of the image")

# Downscaling the Image #

downscaled_image = image[::2,::2]

plt.imshow(downscaled_image)
plt.show()