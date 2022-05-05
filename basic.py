from turtle import width
import cv2 as cv
from numpy import histogram, quantile

img = cv.imread('Photos/minimalism.jpg')
# cv.imshow('Minimalism', img)

# 1. Convert colour
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


def rescaleFrame(frame, scale=2):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_resized = rescaleFrame(gray)
# cv.imshow('Gray', img_resized)

# 2. Blur
# kernel size is only odd number
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# 3. Edge cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)

# 4. Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('Dilated', dilated)

# 5. Eroding
eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroed', eroded)

# 6. Resize
resized = cv.resize(img, (500, 200), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# 7. Cropping
cropped = img[50:100, 20:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
