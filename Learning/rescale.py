import cv2 as cv

img=cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat',img)


def rescaleFrame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


# def changeRes(width,heigth):
#     # only for live videos
#     live.set(3,width)
#     live.set(4,heigth)

# live=cv.VideoCapture(0)
capture=cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)
    resized_vid=rescaleFrame(frame)
    # resized_vid=changeRes(300,300)
    cv.imshow('resized_video',resized_vid)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

resized_cat=rescaleFrame(img)
cv.imshow('resized_cat',resized_cat)


cv.waitKey(0)