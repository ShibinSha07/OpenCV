import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('Photos/park.jpg')
cv.imshow('image',img)

# plt.imshow(img)         #gives reverse of bgr image. ie,rgb
# # plt.show()


# #bgr to gray
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# #bgr to hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# hsv to bgr
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

# #bgr to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("lab",lab)


# lab to bgr
lab_bgr=cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('lab_bgr',lab_bgr)

# #bgr to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show()


# cv.waitKey(0)