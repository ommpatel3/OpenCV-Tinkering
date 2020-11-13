import numpy as np
import cv2
import sys

detectorface= cv2.CascadeClassifier(sys.path[0]+'//haarcascade_frontalface_default.xml')
detectoreye= cv2.CascadeClassifier(sys.path[0]+'//haarcascade_eye.xml')
cap = cv2.VideoCapture(0)


while(True):
    ret, img = cap.read()

    facex1 = 10
    facex2 = 20
    facey1 = 10
    facey2 = 20

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detectorface.detectMultiScale(gray, 1.3, 5)
    eyes = detectoreye.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        facex1 = x
        facex2 = x+h
        facey1 = y
        facey2 = y+h
        print (facex1, facex2, facey1, facey2)

    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow('frame',img)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv2.destroyAllWindows()