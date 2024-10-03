
'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 9: Using GMM to track movement of an object for a given video.
Date: 3rd October 2024
'''

from turtle import back
import cv2 as cv
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from skimage.color import rgb2gray
import numpy as np
import pickle
import os

file_path = 'Computer Vision/background.pickle'

'''
Task 1: Use GMM to generate background in the given video. Use K=3 Gaussian
'''

cap = cv.VideoCapture("Computer Vision/traffic.avi")
ret, f = cap.read()

print("Original Frame Size: ", f.shape)
f = cv.resize(f, (95,95))
print("Frame Size After Resizing: ", f.shape)

# print(ret)
# plt.imshow(f)
# plt.show()

frames = []
frame_count = 0

while True:
    ret, f = cap.read()
    if f is not None:
        f = cv.resize(f, (95,95))
        frames.append(f)
        frame_count = frame_count + 1
        
    else:
        break
    
print("\nTotal number of frames:", frame_count)

frames = np.array(frames)
n = 100

plt.title(f"Frame {n}")
plt.imshow(frames[n])
plt.show()

frame_shape = frames[0].shape
#print(f"Frame Shape:", frame_shape)

row, col, cha = frame_shape

gmm = GaussianMixture(n_components=3)
background = np.zeros((frame_shape))

if os.path.exists(file_path):
    with open(file_path, "rb") as file:
        background = pickle.load(file)
        
else:
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                x = frames[:,i,j,k]
                x = x.reshape(frame_count, 1)
                gmm.fit(x)
                means = gmm.means_
                weights = gmm.weights_
            
                idx = np.argmax(weights)
            
                background[i][j][k] = int(means[idx][0])
            
    with open(file_path, 'wb') as file:
        pickle.dump(background, file)
            
            
'''
Task 2: Apply back ground subtraction to determine foreground of the video
 &
Task 3: change the value of K and observe the effect
'''

background = background/np.max(background)

plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(frames[1])
plt.title("Frame 1")

plt.subplot(3,2,2)
frame1 = frames[1]
foreground = rgb2gray(frame1) - rgb2gray(background)
plt.imshow(foreground, cmap='gray')
plt.title("Foreground For Frame 1")

plt.subplot(3,2,3)
plt.imshow(frames[60])
plt.title("Frame 60")

plt.subplot(3,2,4)
frame1 = frames[60]
foreground = rgb2gray(frame1) - rgb2gray(background)
plt.imshow(foreground, cmap='gray')
plt.title("Foreground For Frame 60")

plt.subplot(3,2,5)
plt.imshow(frames[115])
plt.title("Frame 115")

plt.subplot(3,2,6)
frame1 = frames[115]
foreground = rgb2gray(frame1) - rgb2gray(background)
plt.imshow(foreground, cmap='gray')
plt.title("Foreground For Frame 115")

plt.show()

'''
Conclusion:
1. For the given video, at each pixel location, Gaussian Mixture Model of Gaussian=3 is used to generate background frames.
2. To track moving objects such as cars, background subtraction is used.
3. Results show that Frame 1, 60 and 115, depict only moving cars with no background.
4. If number of gaussian is increased from 3 to 5, accuracy of segmenting moving objects like cars improves.
5. However the computational complexity increases, with the increase in number of gaussian curves.
'''

# Calmly Crafted By Achintya Kamath/Redzwinger #

