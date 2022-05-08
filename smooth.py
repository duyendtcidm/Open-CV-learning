import cv2 as cv
import numpy as np

img = cv.imread('Photos/mini2.jpg')

# blur

# Averaging
average = cv.blur(img, (3, 3))
# Gaussian Blur (less blur than average methos)
gauss = cv.GaussianBlur(img, (3, 3), 0)
# Median blur
medium = cv.medianBlur(img, 3)
# Bilater blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)

cv.waitKey(0)
