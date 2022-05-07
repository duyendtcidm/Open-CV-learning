from turtle import width
import cv2 as cv
from cv2 import INTER_AREA

img = cv.imread('Photos/img2.jpg')
# cv.imshow('Dubai', img)


def rescaleFrame(frame, scale):
    # Work for image, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img_resized = rescaleFrame(img, 0.2)
cv.imshow('Dubai', img_resized)
cv.waitKey(0)

capture = cv.VideoCapture('Videos/google.mp4')


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)

#     # Display origin video
#     # cv.imshow('Video', frame)
#     cv.imshow('Video', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
