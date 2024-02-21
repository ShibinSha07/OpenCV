import cv2 as cv

import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('image',img)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur=cv.blur(gray,(5,5))
cv.imshow('blur',blur)

# canny=cv.Canny(img,125,175)
canny=cv.Canny(blur,125,175)
cv.imshow('canny edges',canny)

ret, thresh=cv.threshold(gray,125,175,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours,hierachies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
# contours,hierachies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))


cv.drawContours(blank,contours,-1,(0,255,0),1)
cv.imshow('blank',blank)


cv.waitKey(0)