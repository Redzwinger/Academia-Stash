'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 8: Mean Shift Algorithm
Date: 26th September 2024

Task 1: Crop an object from first frame of the given video
Task 2: Use histogram back projection to determine probability of each pixel of a frame
Task 3: Use probabilities as data samples
Task 4: Use Mean Shift Algorithm to segment the frame
Task 5: Repeat it for all the frames to track the object
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

# A Setup for the Video Buffer #
frames = []
cap = cv2.VideoCapture('Computer Vision/humans.avi')
count = int(0)
# Looping and Iterating through all Frames #
while 1 > 0:
    ret, f = cap.read()
    if f is not None:
        frames.append(f)
        count += 1
    else:
        break

# Checking #
print(f"Number of Frames : {count}")
plt.imshow(frames[100]) # Test View
plt.show()

# Reset the Pointer Again #
cap = cv2.VideoCapture('Humans.avi')
ret, curF = cap.read()

# Selecting a Human to track #
x,y,w,h = 210, 70, 40, 50
cropped = curF[y:y+h, x:x+w]

# Converting to HSV #
hsv_cropped = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)

# Setting up the mask with the limits #
mask = cv2.inRange(hsv_cropped, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
croppedHist = cv2.calcHist([hsv_cropped], [0], mask, [180], [0,180])

# Normalization Step #
croppedNorm = cv2.normalize(croppedHist, croppedHist, 0, 255, cv2.NORM_MINMAX)

# Term Criteria Initialization #
critVals = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# Showing the output #
plt.subplot(1,2,1)
plt.imshow(curF)
plt.title("Original Frame")
plt.subplot(1,2,2)
plt.imshow(cropped)
plt.title("Cropped Image with AOI")
plt.show()

# Reset the Capture Pointer #
cap = cv2.VideoCapture('Humans.avi')
newFrames = []
trackWindow = (x,y,w,h)

# Looping again (fresh) #
for i in range(1, count):
    ret, curF = cap.read()
    hsvFrame = cv2.cvtColor(curF, cv2.COLOR_BGR2HSV)
    searchFrame = cv2.calcBackProject([hsvFrame], [0], croppedNorm, [0,180], 1)
    searchFrame, trackWindow = cv2.meanShift(searchFrame, (x,y,w,h), critVals)
    x,y,w,h = trackWindow # Refresh a new trackWindow
    image = cv2.rectangle(curF, (x,y), (x+w, y+h), (210,120,30), 2)
    newFrames.append(image)

# Plotting the Results #
plt.subplot(2,2,1)
plt.imshow(newFrames[1])
plt.title("Frame 1")
plt.subplot(2,2,2)
plt.title("Frame 5")
plt.imshow(newFrames[5])
plt.subplot(2,2,3)
plt.title("Frame 10")
plt.imshow(newFrames[10])
plt.subplot(2,2,4)
plt.title("Frame 15")
plt.imshow(newFrames[15])
plt.show()

'''
CONCLUSION:
1. Back Projection is used to determine the probabilities of the
    histogram matching between object and each frame of the sequence.
2. These probabilities are used as data points for the Mean Shift algorithm.
3. This algorithm segments out the object from each frame.
4. Therefore, the motion of the object can be tracked from, frame to frame.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

