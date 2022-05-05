import cv2 as cv
import numpy as np

img = cv.imread('Photos/mini2.jpg')
# cv.imshow('Minimalism', img)

# 1. Translation: shift img to left or right, up or down
# -x -> left
# -y -> up
# x -> right
# y -> down


def translate(img, x, y):
    tranMat = np.float32([[1, 0, x], [0, 1, y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, tranMat, dimentions)


translated = translate(img, 100, 100)
# cv.imshow('Translate', translated)


# 2. Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.2)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


# angle < 0 -> follow clockwise
# angle > 0 -> counter clockwise
rotated = rotate(img, -30)
# cv.imshow('Rotated', rotated)

# 3. Flipping
# You can flip by horizion(1), vertical(0), hor&ver(-1)
flip = cv.flip(img, 0)
cv.imshow('Flipped', flip)
cv.waitKey(0)
