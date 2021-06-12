import cv2
import numpy as np

def filterGlass(frame,ex,ey,ew,eh,x,y,w,h,path):
    glass = cv2.imread(path,-1)
    #glass = cv2.cvtColor(glass,cv2.COLOR_BGR2BGRA)
    glass = cv2.resize(glass,(w,50))
    for i in range(50):
        for j in range(w):
            # need repair
            if glass[i][j][3] != 0:
                frame[i+ey+y][x+j] = glass[i][j]     