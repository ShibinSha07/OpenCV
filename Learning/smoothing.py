import cv2 as cv

img=cv.imread('Photos/cats.jpg')
cv.imshow('img',img)

#       1.avg blur
blur=cv.blur(img,(3,3))
cv.imshow('blur',blur)

#       2.Gaussian blur
gauss=cv.blur(img,(3,3),0)
cv.imshow('gaussian img',gauss)

#       3.Median blur
median=cv.medianBlur(img,3)
cv.imshow('median_blur',median)


#       4.bilateral blur        most usd and good one
bilateral=cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral_img',bilateral)

cv.waitKey(0)