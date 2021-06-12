import cv2
import numpy as np

def filterBeard(frame,x,y,w,h,nx,ny,nw,nh,path):
    beard = cv2.imread(path,-1)
    beard_h = 20
    beard = cv2.resize(beard,(nw,beard_h))
    for i in range(beard_h):
        for j in range(nw):
            if beard[i][j][3] != 0:
                frame[i+ny+nh-15][nx+j] = beard[i][j]
def filterGasMask(frame,x,y,w,h,nx,ny,nw,nh,path):
    maskGas = cv2.imread(path,-1)
    mask_w = w
    mask_h = y+h-ny
    maskGas = cv2.resize(maskGas,(mask_w,mask_h))
    for i in range(mask_h):
        for j in range(mask_w):
            if maskGas[i][j][3] != 0:
                frame[i+ny][x+j] = maskGas[i][j]