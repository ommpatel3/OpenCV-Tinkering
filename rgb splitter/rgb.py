'''
import cv2
import numpy

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    
    b,g,r = cv2.split(frame)
    height, width, layers = frame.shape
    zeroImgMatrix = numpy.zeros((height, width), dtype="uint8")

    b = cv2.merge([b, zeroImgMatrix, zeroImgMatrix])
    g = cv2.merge([zeroImgMatrix, g, zeroImgMatrix])
    r = cv2.merge([zeroImgMatrix, zeroImgMatrix,r])

    cv2.imshow('red',r)
    cv2.imshow('green',g)
    cv2.imshow('blue',b)


cap.release    
cv2.destroyAllWindows
'''
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
cv2.namedWindow("green")

while True:
    ret_val, frame = cap.read()
    # split the image into its RGB channels
    height, width, layers = frame.shape
    zeroImgMatrix = np.zeros((height, width), dtype="uint8")


    b,g,r = cv2.split(frame)


    cv2.imshow("green",g)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # if 'q' is pressed then quit
        break
cap.release()
cv2.destroyAllWindows()
