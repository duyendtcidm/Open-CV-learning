import cv2 as cv
from cv2 import INTER_AREA

img = cv.imread('Photos/img2.jpg')
cv.imshow('Dubai', img)

# def rescaleFrame(frame, scale = 3):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)

#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def rescaleFrame(frame, scale=0.25):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


cv.waitKey(0)
