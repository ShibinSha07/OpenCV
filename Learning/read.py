import cv2 as cv

# img=cv.imread('Photos/cat.jpg')

# cv.imshow('Cat',img)

# cv.waitKey(0)

cap=cv.VideoCapture(0)
# cap=cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame=cap.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break

cap.release()
cv.destroyAllWindows()

