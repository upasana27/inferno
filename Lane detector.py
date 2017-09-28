import cv2
import numpy as np
import math
cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read()
#image=cv2.imread(r'C:\Users\SR\Desktop\img\yellow3.jpg')
   
    img_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #for white lanes
    lower_yellow = np.array([0,0,0])
    upper_yellow = np.array([70,20,255])
    mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    kernel_size = 5
    blur = cv2.GaussianBlur(mask,(5,5),0)
    canny_edges =cv2.Canny(blur,300,400);
    lines = cv2.HoughLinesP(canny_edges,1,np.pi/180,1,minLineLength=30, maxLineGap=10)
    max=0
    #print len(lines[0])
    #print lines[0]
    for i in range(0, len(lines[0])):
      #for x1,y1,x2,y2 in lines[0][i]:
         #cv2.line(image,(lines[0][i][0],lines[0][i][2]),(lines[0][i][1],lines[0][i][3]),(0,255,0),2)
        s=math.pow((lines[0][i][0]-lines[0][i][2]),2)+math.pow((lines[0][i][1]-lines[0][i][3]),2)
        l=math.sqrt(s)
        if l>max:
            max=l;
            li=i
    
    print lines[0][li]
    cv2.line(frame,(lines[0][li][0],lines[0][li][1]),(lines[0][li][2],lines[0][li][3]),(0,255,0),2)

    cv2.imshow('mask',frame)
    cv2.waitKey(1)
