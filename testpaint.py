import numpy as np
import cv2 as cv

def nothing(x):
    pass

cv.namedWindow("Set Size")

cv.createTrackbar("Height","Set Size",1,1000,nothing)
cv.createTrackbar("Length","Set Size",1,1000,nothing)
while(1):
    k = cv.waitKey(0)
    if k == ord("q"):
        #imX=cv.getTrackbarPos("Height","Set Size")
        #imY=cv.getTrackbarPos("Length","Set Size")
        imX=300
        imY=300
        image = np.zeros((imX,imY,3), np.uint8)
        cv.destroyWindow("Set Size")
        cv.namedWindow("Paint")
        cv.imshow("Paint", image)
        break

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow("Color")

cv.createTrackbar("R","Color",0,255,nothing)
cv.createTrackbar("G","Color",0,255,nothing)
cv.createTrackbar("B","Color",0,255,nothing)

r=0
g=0
b=0

draw=False

def draw_color(event,x,y,flags,param):
    global draw
    if event == cv.EVENT_LBUTTONDOWN:
        draw=True

    elif event == cv.EVENT_LBUTTONUP:
        draw=False
        image[y][x]=[b,g,r]

    if event == cv.EVENT_MOUSEMOVE:
        if draw == True:
            image[y][x]=[b,g,r]
cv.setMouseCallback("Paint", draw_color)

while(1):
    k = cv.waitKey(1)
    if k == ord("q"):
        break
    cv.imshow("Paint", image)
    cv.imshow("Color", img)
    r=cv.getTrackbarPos("R","Color")
    g=cv.getTrackbarPos("G","Color")
    b=cv.getTrackbarPos("B","Color")
    img[:] = [b,g,r]
    
