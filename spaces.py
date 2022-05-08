import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/img2.jpg')
cv.imshow('Large image', img)

# convert BGR->RGB
plt.imshow(img)
plt.show()

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# BGR TO HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# BGR to L*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)

# cv.waitKey(0)
