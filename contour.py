import cv2 as cv
import numpy as np

img = cv.imread('Photos/mini2.jpg')
# cv.imshow('Minimalism', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

contours, hierachies = cv.findContours(
    thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours draw', blank)

cv.waitKey(0)
