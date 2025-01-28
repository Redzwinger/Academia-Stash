
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 10: Estimate depth of objects for the given stereo images
Date: 17th October 2024
'''

import cv2 as cv
import matplotlib.pyplot as plt

'''
Task 1: Estimate depth for the given stereo images
Task 2: Change number of disparities and block size
Task 3: Observe the changes
'''

# Reading the images #
lefty = cv.imread("Computer Vision/left_image.JPG")
righty = cv.imread("Computer Vision/right_image.JPG")

# Converting from BGR to RGB #
lefty = cv.cvtColor(lefty, cv.COLOR_BGR2RGB)
righty = cv.cvtColor(righty, cv.COLOR_BGR2RGB)

# Resizing to same shape #
shL = lefty.shape
re_righty = cv.resize(righty, (shL[1],shL[0]))

# Converting to gray #
lefty_GR = cv.cvtColor(lefty, cv.COLOR_RGB2GRAY)
righty_GR = cv.cvtColor(re_righty, cv.COLOR_RGB2GRAY)

# Plotting all of the images #
plt.subplot(2,2,1)
plt.title("Left Image")
plt.imshow(lefty)
    
plt.subplot(2,2,2)
plt.title("Right Image")
plt.imshow(righty)

plt.subplot(2,2,3)
plt.title("Grayed Left Image")
plt.imshow(lefty_GR, cmap='gray')
    
plt.subplot(2,2,4)
plt.title("Grayed Right Image")
plt.imshow(righty_GR, cmap='gray')
plt.show()

# Invoking Disparity - Difference between horizontal co-ordinates of the images #
stereo = cv.StereoBM_create(numDisparities=16, blockSize=15)
image_depth = stereo.compute(lefty_GR, righty_GR, cv.CV_8UC1)

plt.title("Image Depth - D16, BS15")
plt.imshow(image_depth, cmap='gray')
plt.show()

# Changing things #
stereo = cv.StereoBM_create(numDisparities=32, blockSize=31)
image_depth = stereo.compute(lefty_GR, righty_GR, cv.CV_8UC1)

plt.title("Image Depth - D32, BS31")
plt.imshow(image_depth, cmap='gray')
plt.show()

# Changing things #
stereo = cv.StereoBM_create(numDisparities=32, blockSize=15)
image_depth = stereo.compute(lefty_GR, righty_GR, cv.CV_8UC1)

plt.title("Image Depth - D32, BS15")
plt.imshow(image_depth, cmap='gray')
plt.show()

# Changing things #
stereo = cv.StereoBM_create(numDisparities=32, blockSize=7)
image_depth = stereo.compute(lefty_GR, righty_GR, cv.CV_8UC1)

plt.title("Image Depth - D32, BS7")
plt.imshow(image_depth, cmap='gray')
plt.show()

'''
Conclusion:
1. For the given stereo rectified images, top 16 disparities and block size of 15 are
   considered to calculate the depth of the objects in the given images.
   
2. If the number of disparities are increased from 16 to 32,
   the results show the finer details of the depth.

3. If block size is decreased from 15x15 to 7x7,
   we see that the depth map shows the depth of the smaller objects.

4. If block size is increased to 31x31, depth of larger objects like
   the table lamp are shown in the results.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

