import cv2 as cv
from cv2 import rectangle
from cv2 import circle
from cv2 import bitwise_or
from cv2 import bitwise_not
from cv2 import bitwise_xor
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (20, 20), (300, 250), (230, 0, 150), -1)
circle = cv.circle(blank.copy(), (200, 160), 160, (200, 0, 150), -1)

# cv.imshow('Blank with rec and cir', blank)
# cv.imshow('rec and cir', rectangle)
# cv.imshow('cir', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
# cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

# Bitwise XOR

bitwise_xor = cv.bitwise_xor(restangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)


cv.waitKey(0)
