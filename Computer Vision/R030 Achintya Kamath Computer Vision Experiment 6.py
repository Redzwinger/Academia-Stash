
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 6: Homography
Date: 12th September 2024
'''

from ctypes.wintypes import RGB
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from skimage import data
from skimage.color import rgb2gray

def Homography(ori_img, skew_img):

    # Checking the shape #
    print("\n Original Image Shape: ", ori_img.shape, "\n Skewed Image Shape: ", skew_img.shape)

    # Plotting the original images #
    plt.subplot(1,2,1)
    plt.title("Original Image - Color")
    plt.imshow(ori_img)
    
    plt.subplot(1,2,2)
    plt.title("Skewed Image - Color")
    plt.imshow(skew_img)

    plt.show()
    
    ori_gray = cv.cvtColor(ori_img, cv.COLOR_BGR2GRAY)
    skew_gray = cv.cvtColor(skew_img, cv.COLOR_BGR2GRAY)
    
    print("\n Original Gray Image Shape: ", ori_gray.shape, "\n Skewed Gray Image Shape: ", skew_gray.shape)
    
    plt.subplot(1,2,1)
    plt.title("Original Image - Gray")
    plt.imshow(ori_gray, cmap="gray")
    
    plt.subplot(1,2,2)
    plt.title("Skewed Image - Gray")
    plt.imshow(skew_gray, cmap="gray")

    plt.show()
    
    [row, col] = ori_gray.shape
    
    orb = cv.ORB_create(500) # Keypoint Detector
    
    k1, d1 = orb.detectAndCompute(ori_gray, None) # Getting the Keypoints and The Descriptors
    k2, d2 = orb.detectAndCompute(skew_gray, None)
    
    #print("\n Shape of Keypoints: ", k1, "\n Shape of Descriptors: ", d1.shape)
    
    #Brute Force Matching
    m = cv.BFMatcher(cv.NORM_HAMMING)
    matches = m.match(d2,d1)
    matches = sorted(matches, key=lambda x:x.distance)
    
    print("\n Matched Points: ", len(matches))
    
    good_matches = int(len(matches)*0.1)
    matches = matches[:good_matches]
    
    print("\n Number of Good Matches: ", good_matches)
    
    points1 = np.zeros((good_matches, 2))
    points2 = np.zeros((good_matches, 2))
    
    for i in range(good_matches):
        # Populating P2 Matrix with P1 Matches
        points2[i:] = k2[matches[i].queryIdx].pt
        points1[i:] = k1[matches[i].trainIdx].pt
    
    print("\n Shape of Points: P1 - ", points1.shape, " P2 - ", points2.shape)
    
    # Making a H-Matrix
    H, mask = cv.findHomography(points2, points1, cv.RANSAC)
    
    # Aligning the image by warping
    aligned_img = cv.warpPerspective(skew_img, H, (col, row))
    
    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.imshow(ori_img)
    
    plt.subplot(1,3,2)
    plt.title("Skewed Image")
    plt.imshow(skew_img)
    
    plt.subplot(1,3,3)
    plt.title("Re-aligned Image")
    plt.imshow(aligned_img)

    plt.show()

if __name__ == "__main__":
    ori_img = cv.imread("./Computer Vision/straight.jpg")
    skew_img = cv.imread("./Computer Vision/straight_not.jpg")
    
    Homography(ori_img, skew_img)
    

'''
Conclusion:
ORB Detector is used to determine the keypoints and their corresponding descriptors for the reference image and the image to be aligned.
Brute Force Matcher is used to match the keypoints.
Homography matrix is generated using the locations of keypoints of 2 images.
Homography matrix shows the mathematical relation between the keypoints of the two images. 

Homography matrix is used to warp the image to be aligned, after which the aligned image shows that the reference image and the warped image are similar.

For the above process 500 number of keypoints were used and the top 10% percentage of strongest matches were considered for the generation of the H-matrix.

The same algorithm was applied to the other images as well.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

