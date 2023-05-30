import numpy as np
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow("Set Size")

cv.createTrackbar("Height","Set Size",0,1000,nothing)
cv.createTrackbar("Length","Set Size",0,1000,nothing)

while(1):
    k = cv.waitKey(0)
    if k == ord("q"):
        imX=cv.getTrackbarPos("Height","Set Size")
        imY=cv.getTrackbarPos("Length","Set Size")
        image = np.zeros((imX,imY,3), np.uint8)
        cv.destroyWindow("Set Size")
        cv.namedWindow("Paint")
        cv.imshow("Paint", image)
        break
