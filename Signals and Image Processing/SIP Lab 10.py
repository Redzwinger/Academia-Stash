'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Batch: B1
Date: 31/03/2022
Signals and Image Processing
Lab 10
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Batch: B1 \n Date: 31/03/2022 \n Lab 10 \n Signals and Image Processing: Video Processing")

print("\n ############# ################ ####################\n")

# importing stuff
import cv2
import numpy as np
import IPython.display as ipd
import moviepy.editor as mpy

#path of the file
path = str("Australia 2023 FP1.mp4")
vidCap = cv2.VideoCapture(path)

frames_count, fps, width, height = vidCap.get(cv2.CAP_PROP_FRAME_COUNT), vidCap.get(cv2.CAP_PROP_FPS), vidCap.get(
    cv2.CAP_PROP_FRAME_WIDTH), vidCap.get(cv2.CAP_PROP_FRAME_HEIGHT)
ret, frame = vidCap.read()

def gaussian_kernel(size, sigma=1):
    size = int(size) // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    normal = 1 / (2.0 * np.pi * sigma**2)
    g =  np.exp(-((x**2 + y**2) / (2.0*sigma**2))) * normal
    return g
 
# read until end of video
while True:
    # capture each frame of the video
    ret, frame = vidCap.read()
    if height >= 800:
        frame = cv2.resize(frame, (0, 0), None, 0.7, 0.7)

    # Converting to GrayScale #
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gauss Blur #
    blur = cv2.GaussianBlur(grey, (3,3), 0)
    '''
    # Sobel Edge Detection
    sobelx = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
    sobely = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
    sobelxy = cv2.Sobel(src=blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=10) # Combined X and Y Sobel Edge Detection
    '''
    # Canny #
    t_lower = 100  # Lower Threshold
    t_upper = 150  # Upper threshold

    edge = cv2.Canny(blur, t_lower, t_upper)
   
    cv2.imshow('Original Video', frame)
    cv2.imshow('Grey Australia 2023 FP1', grey)
    #cv2.imshow('Sobel Australia 2023 FP1', sobelxy)
    #cv2.imshow('Edge Australia 2023 FP1', edge)

    if cv2.waitKey(10) == ord('q'):
        break
vidCap.release()
cv2.destroyAllWindows()

isExit = input("Press Q to Exit")
