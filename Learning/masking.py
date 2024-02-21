import cv2 as cv
import numpy as np

img=cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

# mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('mask',mask)

# masked=cv.bitwise_and(img,img,mask=mask)
# cv.imshow("masked image",masked)

circle=cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
wrd_shape=cv.bitwise_and(rectangle,circle)

masked_wrd=cv.bitwise_and(img,img,mask=wrd_shape)
cv.imshow("masked image",masked_wrd)

cv.waitKey(0)