import cv2
import numpy as np

def filterMask(frame,x,y,w,h,path):
    anonymus = cv2.imread(path,-1)
    anonymus = cv2.resize(anonymus,(w,h))
    for i in range(h):
        for j in range(w):
            if anonymus[i][j][3] != 0:
                frame[y+i][x+j] = anonymus[i][j]
def filterHeart(frame,x,y,w,h,path):
    hair = cv2.imread(path,-1)
    hair = cv2.resize(hair,(w,100))
    for i in range(100):
        for j in range(w):
            # color RGBA
            #print(i,j)
            if hair[i][j][2] != 0: # a != 0
                frame[y-50+i][x+j] = hair[i][j]