import cv2 as cv
import numpy as np

# img = cv.imread('Photos/mini2.jpg')
# cv.imshow('Minimalism', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1.Paint the image a certain colour
# blank[100:250, 300:450] = 255, 100, 255
# cv.imshow('Green', blank)

# 2. Draw a regtangle
# cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=2)
# cv.imshow('Regtangle', blank)

# 3. Draw circle
# cv.circle(blank, (200, 300), 40, (255, 0, 0), thickness=3)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (100, 200),
#         (blank.shape[1]//2, blank.shape[0]//2), (255, 200, 240), thickness=2)


# 5.Write text
cv.putText(blank, 'Delora - Duyen Dinh', (50, 230),
           cv.FONT_HERSHEY_SIMPLEX, 1.2, (255, 20, 240), 2)
cv.imshow('Write text', blank)

cv.waitKey(0)
