# -*- coding: utf-8 -*-


import cv2
import numpy as np
import serial
import time

cap=cv2.VideoCapture(0)
cv2.namedWindow('linefollower')
cv2.namesWindow('frame')

While True:
        ret,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
        lower_black=np.array([0,0,0])
        upper_black=np.array([180,255,30])
        black_mask=cv2.inRange(hsv,lower_black,upper_black)
        hist=np.sum(black_mask,axis=0)
        max_black=np.argmax(hist)
        if max_black>150:
          m='R'
          ser.write(m.encode('utf-8'))
        elif max_black<100:
          m='L'
          ser.write(m.encode('utf-8'))
        else
          m='S'
          ser.write(m.encode('utf-8'))
        display_str=[]
        display_str.append("THROTTLE:{:.2F]".format(max_black))
        display_str.append("DIRECTION:{:.2F]".format(m))
        cv2.imshow('frame',frame)
        cv2.imshow('linefollower',black_mask)

        print(max_black)
        if cv2.waitKey(1) & 0xFF=ord('q'):
          break
