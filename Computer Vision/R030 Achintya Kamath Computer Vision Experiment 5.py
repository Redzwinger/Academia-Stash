
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 5: Determine SIFT descriptors of the given image
Date: 5th September 2024

Task 1: Determine SIFT descriptor of the given image
Task 2: scale, rotate and crop the given image. Determine SIFT descriptors
Task 3: Match SIFT descriptors of original and modified images
Task 4: Observe the matching points
'''

import cv2
import matplotlib.pyplot as plt
import imutils
import numpy as np
import os

image1 = cv2.imread('Computer Vision/card1.JPG')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
plt.imshow(image1)
plt.show()

sift = cv2.SIFT_create(contrastThreshold = 0.2)
k1, d1 = sift.detectAndCompute(image1, None)

print(d1.shape)

image1_c = image1.copy()
image1_c = cv2.drawKeypoints(image1, k1, image1_c)
plt.imshow(image1_c)
plt.show()

image2 = cv2.resize(image1,(100,50))
k2, d2 = sift.detectAndCompute(image2, None)
image2_c = image2.copy()
image2_c = cv2.drawKeypoints(image2, k2, image2_c)
plt.imshow(image2_c)
plt.show()

image3 = imutils.rotate(image1, 10)
k3, d3 = sift.detectAndCompute(image3, None)
image3_c = image3.copy()
image3_c = cv2.drawKeypoints(image3, k3, image3_c)
plt.imshow(image3_c)
plt.show()

image4 = image1[100:,25:100]
k4, d4 = sift.detectAndCompute(image4, None)
image4_c = image4.copy()
image4_c = cv2.drawKeypoints(image4, k4, image4_c)
plt.imshow(image4_c)
plt.show()

print(d2.shape)

bf = cv2.BFMatcher()
m1_2 = bf.match(d1, d2)
m1_3 = bf.match(d1, d3)
m1_4 = bf.match(d1, d4)

m1_2 = sorted(m1_2, key=lambda val: val.distance)
m1_3 = sorted(m1_3, key=lambda val: val.distance)
m1_4 = sorted(m1_4, key=lambda val: val.distance)

out1_2 = cv2.drawMatches(image1, k1, image2, k2, m1_2[:5], None)
plt.imshow(out1_2)
plt.show()

out1_3 = cv2.drawMatches(image1, k1, image3, k3, m1_3[:5], None)
plt.imshow(out1_3)
plt.show()

out1_4 = cv2.drawMatches(image4, k1, image4, k4, m1_4[:5], None)
plt.imshow(out1_4)
plt.show()

'''
Conclusion:
    SIFT is used to identify the location of the key points 
    and to determine the descriptor of key point for the given image.

    It identifies 31 key points with length 128.

    The original image is modified to generate, resized, rotate, cropped images.

    SIFT descriptors are determined for all the 3 modified image. 
    Brute Force matcher is used to match key points of original image and all the 3 images.

    Top 5 matches with minimum euclidean distance show correct matches except 1 false match.

    Default contrast threshold is 0.03 and if the contrast
    threshold is increased to 0.2 false match disappears.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

