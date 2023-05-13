import cv2
import numpy as np
import matplotlib.pyplot as plt

#obtaining the negative of an image

img = cv2.imread("bad eye test (low res).tif")

negative = (np.amax(img) - img)

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img, cmap = 'gray')

plt.subplot(1, 2, 2)
plt.title("Negative Image")
plt.imshow(negative, cmap = 'gray')

plt.show()

#obatining the tresholding of an image

 