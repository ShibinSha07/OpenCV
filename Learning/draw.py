import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow("blank",blank)
#           1.paint the image
# blank[:]=0,255,0       #for selecting full screen
# blank[200:300,300:400]=0,255,0
# cv.imshow('green',blank)

# #           2.draw rectangle
# # cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)  #giving coordinates
# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=2) #giving coordinates as comparison of that frame
# # cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=cv.FILLED)  #fill rectangle with a color
# # cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)  #fill rectangle with a color
# cv.imshow('rectangle',blank)

# #           3.draw a circle
# cv.circle(blank,(250,250),50,(0,0,255),thickness=3)
# cv.imshow('circle',blank)

# #           4.draw a line
# cv.line(blank,(0,0),(250,250),(255,255,255),thickness=2)
# cv.imshow("line",blank)

#           5.write text
cv.putText(blank,"Hello, I'm ShibinSha... ",(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
cv.imshow('text',blank)

cv.waitKey(0)