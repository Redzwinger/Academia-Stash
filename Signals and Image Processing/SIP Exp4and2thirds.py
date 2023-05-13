import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Signals and Image Processing
Batch: B1
Date: 03/02/2023
Lab 4 Part 2
'''

# Info about me and the practical

print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Signals and Image Processing\n Batch: B1 \n Date: 03/02/2023 \n Lab 4 Part 2")

print("\n ############# ################ ####################\n")

'''
code for Jupyter notebook 
import cv2
import numpy as np
import matplotlib as plt
image = cv2.imread(PATH OF THE IMAGE)
#upload the image in Jupyter notebook

cv2.imshow(name on the window, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

#using local machine (not Jupyter notebook)

#full path version
#foto = cv2.imread("D:\Achintya\Achintya's College Stuff\Subjects\Sem 4\Signal and Image Processing\Lab\images\DIP3E_Original_Images_CH03\Fig0333(a)(test_pattern_blurring_orig).tif", 0)

foto = cv2.imread("bad eye test (low res).tif", 0)
plt.figure(figsize=(10,5))
cv2.imshow("bad eye test (low res)", foto)
cv2.waitKey(0)
cv2.destroyAllWindows()

# appyling low pass filtering on the image
# using an averaging filter
# with a 3 x 3 mask, ie, multipying by 1/9

def lowpassfiltering(anotherImage):

    row, col = anotherImage.shape
    maskedimage = np.zeros([row,col], dtype=int)

    b = int(input("Please enter the size of the mask: "))
    a = b//2

    for i in range(a,row-a):
        for j in range(a, col-a):
            maskedimage[i,j] = np.sum(anotherImage[i-a:i+a+1,j-a:j+a+1])//b**2

    return maskedimage

masks = int(input("Please enter the number of masks to compare: "))

plt.figure(figsize=(10,5))
mask = [15,35,45] 
for i in range(masks):

    new_foto = lowpassfiltering(foto)

    plt.subplot(1, masks, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.title("mask size {}".format(mask[i]))
    plt.imshow(new_foto, cmap="gray")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
plt.show()
