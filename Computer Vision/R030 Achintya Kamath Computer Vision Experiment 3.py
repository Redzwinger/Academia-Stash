
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 3 : To determine the Histogram of Gradients (HoG) of the given image and use it to detect objects in the given image.
1st August 2024

Task 1: Determine HoG of the given image.
Task 2: Change brightness and repeat task 1. Observe the effect on HoG due to change in brightness
Task 3: Use SVM detector to detect people
'''

# Tasks 1 and 2 #

# Importing things #
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from skimage.io import imread
from skimage.transform import resize # Used to resize the image to make it into multiples of 8 or 64
from skimage.feature import hog
from skimage import exposure # Used to rescale the image without changing HOG

def HistogramOfGradients(pix, ori):
    RAWimage = imread("./Computer Vision/cat.png") # Reading the image using skimage.io.imread

    # Checking the shape #
    print("\n Original Image Shape: ", RAWimage.shape)

    # Plotting the original image #
    plt.title("Original Raw Image")
    plt.imshow(RAWimage)
    plt.show()

    darkenedImage = cv.convertScaleAbs(RAWimage, beta=-100)
    Resizedimage = resize(RAWimage, (128*5.8, 64*7.7)) 
    darkenedImage = resize(darkenedImage, (128*5.8, 64*7.7)) 
    # Resizing to closest to the original size. This is done to enhance the HoG features. #

    print("\n Resized Image Shape: ", Resizedimage.shape, darkenedImage.shape)

    plt.subplot(1, 2, 1)
    plt.title("Original Resized Image")
    plt.imshow(Resizedimage)

    plt.subplot(1, 2, 2)
    plt.title("Darkened Resized Image")
    plt.imshow(darkenedImage)
    plt.show()

    # Applying HoG Filter to the image #
    filteredImage, HOGim_normal = hog(Resizedimage, orientations=ori, pixels_per_cell=pix, cells_per_block=(2, 2), visualize=True, channel_axis=(-1))

    darkenedFilteredImage, HOGim_dark = hog(darkenedImage, orientations=ori, pixels_per_cell=pix, cells_per_block=(2, 2), visualize=True, channel_axis=(-1))

    print("\n Shape of the Histogram Vector: ", filteredImage.shape, darkenedFilteredImage.shape)

    plt.subplot(1, 2, 1)
    plt.title("HoG Normal")
    plt.imshow(HOGim_normal, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title("HoG Darkened")
    plt.imshow(HOGim_dark, cmap='gray')
    plt.show()

    # Finding percentiles #
    p2_1, p90_1 = np.percentile(HOGim_normal, (2,90))
    p2_2, p90_2 = np.percentile(HOGim_dark, (2,90))

    # Rescaling the images using Exposure #
    HOG_normal_re = exposure.rescale_intensity(HOGim_normal, in_range=(p2_1, p90_1))
    HOG_dark_re = exposure.rescale_intensity(HOGim_dark, in_range=(p2_2, p90_2))
    
    #Ploting Rescaled HOG images #
    
    plt.subplot(1, 2, 1)
    plt.title("HoG Normal")
    plt.imshow(HOG_normal_re, cmap='gray')

    plt.subplot(1, 2, 2)
    plt.title("HoG Darkened")
    plt.imshow(HOG_dark_re, cmap='gray')
    plt.show()

    # Ploting Everything #
    plt.subplot(1, 4, 1)
    plt.title("Original Image")
    plt.imshow(Resizedimage)

    plt.subplot(1, 4, 2)
    plt.title("Darkened Image")
    plt.imshow(darkenedImage)

    plt.subplot(1, 4, 3)
    plt.title("HoG Normal")
    plt.imshow(HOG_normal_re, cmap='gray')

    plt.subplot(1, 4, 4)
    plt.title("HoG Darkened")
    plt.imshow(HOG_dark_re, cmap='gray')
    plt.show()

# Task 3 #

def SVM_Detector():
    # Function to detect people using HoG and SVM (Pre-trained)
    
    RAWimage = imread("./Computer Vision/people9.jpg") # Reading the image using imread
    
    HOg = cv.HOGDescriptor()
    HOg.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
    
    if RAWimage.shape[1] > 400:
        (rows, cols) = RAWimage.shape[:2]
        ratio = cols / float(rows)
        
        image = cv.resize(RAWimage, (400, int(400 * ratio)))
        
        GRAYim = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
        rect, weights = HOg.detectMultiScale(GRAYim, winStride=(4, 4), padding=(8, 8), scale=1.1)
    
        for i, (x, y, w, h) in enumerate(rect):
            if weights[i] < 0.4:
                continue
            else:
                cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()   

if __name__ == "__main__":
    # Default Orientation is 9 #
    orientations = 9
    # Default Pixel Size is 8x8 #
    pix_size = (8,8)
    # HoG #
    HistogramOfGradients(pix_size, orientations)
    # SVM Detector #
    SVM_Detector()

'''
Conclusion 1:
The Histogram of Gradients of the original image and the dark image are found and it is observed that the HoG of both the images are similar. This is because the HoG normalizes all of the features. This is one of the advantages of HoG, i.e., it is invariant to change in brightness.

For number of pixels per cell = 8x8,
Length of the HoG Descriptor is 196560.

For number of pixels per cell = 16x16,
Length of the HoG Descriptor is reducing to 46980.

Therefore, smaller the cell size, larger the HoG Descriptor Vector.

Conclusion 2:
For the given image, the default SVM Detector, which is pretrained model is used.
For winStride=(4, 4), padding=(8, 8), scale=1.1, the SVM Detector detects people with weights of 0.4
If scale is reduced from 1.1 to 1.05, we see that the detector uses more layers of image parameters to detect people. This results in more number of rectangles around people.
Number of rectangles can be reduced by tuning the threshold variable.
'''

# Cautiously Crafted By Achintya Kamath/Redzwinger #

