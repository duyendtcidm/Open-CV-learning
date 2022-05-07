import cv2 as cv
import numpy as np

img = cv.imread('Photos/mini2.jpg')
# cv.imshow('Minimalism', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Threshold', thresh)

contour, hierachies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contour)} contour(s) found!')

cv.waitKey(0)
