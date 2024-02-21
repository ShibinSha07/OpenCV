import cv2 as cv

img=cv.imread('Photos/park.jpg')
cv.imshow("park",img)
 
#converting into grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge cascade
canny=cv.Canny(blur,125,175)
# canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)

#dilating the images
dilated=cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)

#eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('eroded',eroded)

#resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#cropping
cropped=img[50:200,200:400]
cv.imshow('cropped',cropped)


cv.waitKey(0)