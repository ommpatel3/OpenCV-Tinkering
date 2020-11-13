import cv2
import numpy 


def nothing(x):
    pass

vidimg=input ("1 for image, 0 for video  ")

if vidimg=='0':
    cap=cv2.VideoCapture(0)

cv2.namedWindow("Tracking")

#making sliders
cv2.createTrackbar("lowerhue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("lowersat", "Tracking", 0, 255, nothing)
cv2.createTrackbar("lowervalue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("upperhue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("uppersat", "Tracking", 255, 255, nothing)
cv2.createTrackbar("uppervalue", "Tracking", 255, 255, nothing)

while True:

    if vidimg=='0':
        _, img = cap.read()
    else:
        img=cv2.imread('photo.jpeg')#opening image

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)    

    #getting sliderbar inputs
    lowhue = cv2.getTrackbarPos("lowerhue", "Tracking")
    lowsat = cv2.getTrackbarPos("lowersat", "Tracking")
    lowval = cv2.getTrackbarPos("lowervalue", "Tracking")
    hihue = cv2.getTrackbarPos("upperhue", "Tracking")
    hisat = cv2.getTrackbarPos("uppersat", "Tracking")
    hival = cv2.getTrackbarPos("uppervalue", "Tracking")

    #setting upper/lower bounds for colour detection
    lowerbound = numpy.array([lowhue,lowsat,lowval])
    upperbound = numpy.array([hihue,hisat,hival])

    #making mask hwith blue parts transparent
    mask = cv2.inRange(hsv,lowerbound,upperbound,)

    #overlaying mask
    result = cv2.bitwise_and(img,img,mask=mask)

    #showing images
    cv2.imshow('image',img)
    cv2.imshow('result',result)
    cv2.imshow('mask',mask)
    
    #close when esc is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release    
cv2.destroyAllWindows

