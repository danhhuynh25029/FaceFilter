import cv2
import numpy as np

def filterMouthColor(frame,x,y,w,h,path):
    color = cv2.imread(path,-1)
    color_h = 170
    color = cv2.resize(color,(w,color_h))
    for i in range(color_h):
        for j in range(w):
            if color[i][j][3] !=  0:
                frame[y+i-10][x+j] = color[i][j]