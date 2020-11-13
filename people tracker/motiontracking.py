import numpy as np
import cv2

###########VIDEO ANALYSIS FUNCTION
def videostart():
    cap= cv2.VideoCapture("C:\\Users\\Om School\\Programs\\opencv\\people tracker\\vtest.avi")

    while (cap.isOpened):

        ret,frame1 = cap.read()
        ret,frame2 = cap.read()

        diff=cv2.absdiff(frame1, frame2)
        gray=cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray, (9,9), 0)
        _, thresh=cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated=cv2.dilate(thresh, None, iterations=2)
        contours, _=cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            (x,y,w,h)=cv2.boundingRect(contour)
            
            if h>40 and w<100 and cv2.contourArea(contour)>500:
                cv2.circle(frame1, ((int)(x+w/2),(int)(y+h/2)), 2, (0,0,255), 2)

                if x+w/2>(coords[0][0]) and x+w/2<(coords[1][0]) and y+h/2>(coords[0][1]) and y+h/2<(coords[1][1]):
                    cv2.rectangle(frame1,(x,y),(x+w, y+h),(0,0,255),5)
                    cv2.putText(frame1,"Trespassing Detected",(10,70),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
                else:
                    cv2.rectangle(frame1,(x,y),(x+w, y+h),(0,255,0),2)
        
        cv2.drawContours(frame1, contours, -1, (255,0,0), 1)
        ##
        cv2.rectangle(frame1,(coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]), (0,0,255), 2)
        ##       
        
        cv2.imshow("frame",frame1)

        frame1=frame2
        ret, frame2=cap.read()

        if cv2.waitKey(40) == 27:
            break

    cv2.destroyAllWindows
    cap.release()
##################################

########MOUSE CALLBACK FUNCTION
def points(event,x,y,flags,param):
    global coords
    if event == cv2.EVENT_LBUTTONDOWN:
        coords=[[x,y]]
    elif event == cv2.EVENT_LBUTTONUP:
        coords.append([x,y])
        print(coords)
        cv2.rectangle(img, (coords[0][0], coords[0][1]), (coords[1][0], coords[1][1]), (0,0,255), 2)
        videostart()
#################################        

coords= []
img = img = cv2.imread('C:\\Users\\Om School\\Programs\\opencv\\people tracker\\image.png',-1)
cv2.namedWindow('image')
cv2.putText(img,"SELECT RESTRICTED AREA",(10,70),cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)
cv2.putText(img,"*drag from top-left to bottom right",(10,90),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
cv2.setMouseCallback('image',points)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()


    





