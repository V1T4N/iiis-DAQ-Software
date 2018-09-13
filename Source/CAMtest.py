#-*- coding:utf-8 -*-
import cv2



for i in range(9):

    cap = cv2.VideoCapture(i)
    ret, frame = cap.read()
    if(ret == 1):
        print("device" ,i ,"is connected")

cap.release()
cv2.destroyAllWindows()