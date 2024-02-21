import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('image',img)

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x=>left
# -y=>up
# x=>right
# y=>down

translated_img=translate(img,100,100)
cv.imshow('translated',translated_img)


#Rotation
def rotate(img,angle,center=None):
    (height,width)=img.shape[:2]
    if center==None:
        center=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(center,angle,1)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated_img=rotate(img,45)
cv.imshow('rotated_img',rotated_img)
# +angle=>counter clockwise
# -angle=>clockwise

#Resizing
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# shrinking==>cv.INTER_AREA
# enlarging==>cv.INTER_LINEAR  or cv.INTER_CUBIC(more clarty)
cv.imshow('resize',resized)

#Flipping
flipped=cv.flip(img,-1)
# -1==>both vertical and horzontal flipping
# 0==>vertical flipping
# 1==>horizontal flipping
cv.imshow('flipped',flipped)

#Cropping
cropped=img[200:400,300:400]
cv.imshow('cropped',cropped)


cv.waitKey(0)
