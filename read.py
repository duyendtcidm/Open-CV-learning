import cv2 as cv

# img = cv.imread('Photos/mini2.jpg')
# cv.imshow('Minimalism', img)
# cv.waitKey(0)

# Reading video
capture = cv.VideoCapture('Videos/google.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
