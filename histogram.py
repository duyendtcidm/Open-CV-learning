import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/minimalism.jpg')
cv.imshow('Minimalism', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 2. Try with mask
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//4, img.shape[0]//4), 100, 255, -1)
# mask = cv.bitwise_and(gray, gray, mask=circle)
mask = cv.bitwise_and(img, img, mask=circle)


cv.imshow('Mask', mask)

# Grayscale histograms
# gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])


# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# 3.Color histogram
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()


cv.waitKey(0)
