
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 7: Gabor Filter
Date: 17th September 2024

Task 1: Generate a Gabor filter
Task 2: Vary parameters and observe the effects
Task 3: Apply Gabor filters on the given hidden image to extract original image
Task 4: Apply Gabor filters on image, Brick to identify edges in different directions
'''

# Important Imports #
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Gabor Settings #
kSize = int(25) # Size of the Filter
sigma = int(5) # Standard Deviation
theta = int(np.pi / 2) # Orientation of the Normal to the Plane
lamda = int(20) # Wavelength of the sinusoidal factor
gamma = float(0.5) # Aspect Ratio
phi = int(0) # This is the offset 

# Kernel Initialization #
kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
kernel = kernel / kernel.sum()

# Plotting the Kernel #
plt.imshow(kernel, cmap='grey')
plt.show()
print("Our Kernel Looks like : \n", kernel, "\n")

def testingKernels():
    # Gabor Settings I Guess #
    kSize = int(101) # Size of the Filter
    sigma = int(5) # Standard Deviation
    theta = int(0) # Orientation of the Normal to the Plane
    lamda = int(10) # Wavelength of the sinusoidal factor
    gamma = float(0.5) # Aspect Ratio
    phi = int(0) # This is the offset 

    # Kernel Initialization #
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)

    # Plotting the Kernel #
    plt.subplot(2,3,1)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 1: Normal")
    sigma = int(10)
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    plt.subplot(2,3,2)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 2: Sigma Increase")
    kSize = int(15)
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    plt.subplot(2,3,3)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 3: Decrease KSize")
    theta = int(45)
    kSize = int(101)
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    plt.subplot(2,3,4)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 4: Increase Theta")
    lamda = int(20)
    theta = int(0)
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    plt.subplot(2,3,5)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 5: Increase Lambda")
    gamma = float(0.8)
    kernel = cv2.getGaborKernel((kSize, kSize), sigma, theta, lamda, gamma, phi, ktype=cv2.CV_32F)
    plt.subplot(2,3,6)
    plt.imshow(kernel, cmap='grey')
    plt.title("Kernel 6: Increased Gamma")
    plt.show()

testingKernels()

# Part - Two #
curImg = cv2.imread("Computer Vision/Hidden.jpg",0)
plt.subplot(1,2,1)
plt.imshow(curImg, cmap='gray')
plt.title("Hidden Image")

# We will use the above kernel to convolve the image #
plt.subplot(1,2,2)
filtImg = cv2.filter2D(curImg, -1, kernel)
plt.imshow(filtImg, cmap='gray')
plt.title("Filtered Image")
plt.show()

'''
CONCLUSION (One):
    1. Gabor Filter with kSize = 101, SD = 5, angle = 0, 
       orientation = 10, ellipticity = 0.5, phi = 0 is generated.
    2. If Standard Deviation is increased, the number of strips increases.
    3. If Orientation is increased, the filter rotates by that angle with respect to vertical axis.
    4. If Wavelength is reduced, then the number of peaks increases.
    5. Gamma which represents the ellipticity, if reduced, the filter becomes more circular

CONCLUSION (Two):
    1. Hidden image has a lot of vertical lines.
    2. By Applying Gabor Filter, with orientation = 90, lambda at 10
       standard deviation to 2, theta is 90 degrees, and kSize as 25,
       ellipticity as 0.5, the Filtered image shows few vertical weak edges.
    3. To reduce the vertical edges, the standard deviation is increased from 2 to 5
       and wavelength is increased from 10 to 20.
    4. The filtered image shows improved version of the hidden image.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

