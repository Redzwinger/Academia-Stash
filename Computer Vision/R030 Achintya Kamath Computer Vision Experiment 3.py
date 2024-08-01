
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

# Importing things #
import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv
from skimage.io import imread
from skimage.transform import resize # Used to resize the image to make it into multiples of 8 or 64
from skimage.feature import hog
from skimage import exposure # Used to rescale the image without changing HOG


