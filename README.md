# College-Dump
[Updated: 25/03/2024]

a dump for all the stuff done during the semesters. 

I'm putting them up here to have manageable copies, instead of random files all over the place, plus it looks good ;)

NOTE (10/01/2024): Now also maintaining a local Git, using Git integration for Visual Studio. (finally! after years of using VS IDE)


'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Computer Vision Experiment 2 : To highlight Edges using DoG (Difference of Gaussian) and LoG (Laplacian of Gaussian).
25th July 20224
'''

from cgitb import grey
from telnetlib import GA
import cv2 as cv
from skimage import data
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt

def DoG(rawImage):

    greyImage = rgb2gray(rawImage)

    '''
    The image is in RGB format. Which means it has 3 channels/matrices (Red, Green, Blue). The grey image is a single channel/matrix. The grey image is obtained by taking the average of the 3 channels.)
    '''

    print("Shape of Original Image: ", rawImage.shape, "\nShape of Grey Image: ", greyImage.shape)

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(rawImage)

    plt.subplot(1, 2, 2)
    plt.title("Grey Image")
    plt.imshow(greyImage, cmap='grey')
    plt.show()

    '''
    cmap is set to grey so as to represent the lowest intensity value as black and the highest intensity value as white. This is because the with respect to the screen, the lowest intensity value will be green and the highest intensity value will be red. 
    '''

    # Applying Gaussian Blurs of varying deviations to the Grey Image #
    sigmaOne = cv.GaussianBlur(greyImage, (31, 31), 1) # Standard Deviation = 1, Filter Size = 31x31
    sigmaTwo = cv.GaussianBlur(greyImage, (31, 31), 2) # Standard Deviation = 2, Filter Size = 31x31
    sigmaThree = cv.GaussianBlur(greyImage, (31, 31), 3) # Standard Deviation = 3, Filter Size = 31x31
    sigmaFour = cv.GaussianBlur(greyImage, (31, 31), 4) # Standard Deviation = 4, Filter Size = 31x31
    sigmaSeven = cv.GaussianBlur(greyImage, (31, 31), 7) # Standard Deviation = 7, Filter Size = 31x31

    plt.subplot(2, 3, 1)
    plt.title("Original Greyscale Image.")
    plt.imshow(greyImage, cmap='gray')

    plt.subplot(2, 3, 2)
    plt.title("Sigma = 1")
    plt.imshow(sigmaOne, cmap='gray')

    plt.subplot(2, 3, 3)
    plt.title("Sigma = 2")
    plt.imshow(sigmaTwo, cmap='gray')

    plt.subplot(2, 3, 4)
    plt.title("Sigma = 3")
    plt.imshow(sigmaThree, cmap='gray')

    plt.subplot(2, 3, 5)
    plt.title("Sigma = 4")
    plt.imshow(sigmaFour, cmap='gray')

    plt.subplot(2, 3, 6)
    plt.title("Sigma = 7")
    plt.imshow(sigmaSeven, cmap='gray')

    plt.show()

    # Now, Finding the Difference of Gaussians #

    Doggy_One_Seven = sigmaOne - sigmaSeven
    Doggy_Two_Seven = sigmaTwo - sigmaSeven
    Doggy_Three_Seven = sigmaThree - sigmaSeven
    Doggy_Four_Seven = sigmaFour - sigmaSeven

    max_max_max = np.max(Doggy_One_Seven)
    threshold = max_max_max * 0.05

    Doggy_One_Seven[np.abs(Doggy_One_Seven) > threshold] = 255
    Doggy_Two_Seven[np.abs(Doggy_Two_Seven) > threshold] = 255
    Doggy_Three_Seven[np.abs(Doggy_Three_Seven) > threshold] = 255
    Doggy_Four_Seven[np.abs(Doggy_Four_Seven) > threshold] = 255

    plt.subplot(2, 2, 1)
    plt.title("DoG of Sigma=1 and Sigma=7.")
    plt.imshow(Doggy_One_Seven, cmap='gray')

    plt.subplot(2, 2, 2)
    plt.title("DoG of Sigma=2 and Sigma=7.")
    plt.imshow(Doggy_Two_Seven, cmap='gray')

    plt.subplot(2, 2, 3)
    plt.title("DoG of Sigma=3 and Sigma=7.")
    plt.imshow(Doggy_Three_Seven, cmap='gray')

    plt.subplot(2, 2, 4)
    plt.title("DoG of Sigma=4 and Sigma=7.")
    plt.imshow(Doggy_Four_Seven, cmap='gray')

    plt.show()

def LoG():
    
    rawImg = cv.imread(r"C:\Achintya\Achintya's Stuff\Gitty Things\Academia Stash\Academia-Stash\Computer Vision\dhoni.jpg", cv.IMREAD_COLOR)
    colorImg = cv.cvtColor(rawImg, cv.COLOR_BGR2RGB)
    
    # Converting from BGR to RGB #
    
    GaussyImg = cv.GaussianBlur(colorImg, (3, 3), 1)
    grayImg = cv.cvtColor(GaussyImg, cv.COLOR_RGB2GRAY)
    
    # Ploting the Things #
    
    plt.subplot(1, 2, 1)
    plt.imshow(colorImg)
    plt.title("Original Image")
    
    plt.subplot(1, 2, 2)
    plt.imshow(grayImg, cmap='gray')
    plt.title("Grey Image")
    
    plt.show()
    
    laplaceImage = cv.Laplacian(grayImg, cv.CV_16S, ksize=3)
    thresholded_laplaceImage = laplaceImage
    max_max_max = np.max(laplaceImage)
    threshold = max_max_max * 0.5
    
    laplaceImage[np.abs(laplaceImage) > threshold] = 255
    
    plt.subplot(1, 3, 1)
    plt.imshow(grayImg, cmap='gray')
    plt.title("Gray Image")
    
    plt.subplot(1, 3, 2)
    plt.imshow(laplaceImage, cmap='gray')
    plt.title("Laplacian Image")
    
    plt.subplot(1, 3, 3)
    plt.imshow(thresholded_laplaceImage, cmap='gray')
    plt.title("Laplacian Thresholded Image")

    
ImageOne = data.astronaut()
#DoG(ImageOne)
LoG()

Conclusion:
Difference of Gaussians is a technique used to highlight the edges of the given image of the astronaut.
For DoG with Sigma=1 and Sigma=7, fine details of the image are highlighted.
For Dog with Sigma=4 and Sigma=7, fine details disappear and only the outline of the astronaut are visible.

For Sigma=1, filtered image has blurred fine details.
For Sigma=7, filtered image has removed fine details.

Therefore, Difference of Gaussian shows fine details of the image.

For Sigma=4, filtered image has coarse/sparse detais.
For Sigma=4, filtered image has removed fine details.

Therefore the Difference of Gaussian is zero.

Talking about thresholding, for a threshold 0.2, only scattered spots are visible. Whereas at a threshold of 0.05 a thin outline is visible for Sigma=7.