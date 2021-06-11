import cv2
import numpy as np
def filterGasMask(frame,x,y,w,h,nx,ny,nw,nh):
    maskGas = cv2.imread("images/facemask.png",-1)
    mask_w = w
    mask_h = y+h-ny
    maskGas = cv2.resize(maskGas,(mask_w,mask_h))
    for i in range(mask_h):
        for j in range(mask_w):
            if maskGas[i][j][3] != 0:
                frame[i+ny][x+j] = maskGas[i][j]
def filterMask(frame,x,y,w,h):
    anonymus = cv2.imread("images/iron.png",-1)
    anonymus = cv2.resize(anonymus,(w,h))
    for i in range(h):
        for j in range(w):
            if anonymus[i][j][3] != 0:
                frame[y+i][x+j] = anonymus[i][j]
    #rint(w,y)
def filterGlass(frame,ex,ey,ew,eh,x,y,w,h):
    glass = cv2.imread("images/sunglasses.png",-1)
    #glass = cv2.cvtColor(glass,cv2.COLOR_BGR2BGRA)
    glass = cv2.resize(glass,(w,50))
    for i in range(50):
        for j in range(w):
            # need repair
            if glass[i][j][3] != 0:
                frame[i+ey+y][x+j] = glass[i][j]                
    #cv2.circle(frame,(w//2+x,h//2+y),10,(0,255,0),2)
    
def filterHeart(frame,x,y,w,h):
    hair = cv2.imread("images/devil.png",-1)
    hair = cv2.resize(hair,(w,100))
    for i in range(100):
        for j in range(w):
            # color RGBA
            #print(i,j)
            if hair[i][j][2] != 0: # a != 0
                frame[y-50+i][x+j] = hair[i][j]            
                
def detectFace(faceCascade,eyeCascade,frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        # filter Heart
        filterHeart(frame,x,y,w,h)
        # anonymus mask
        #filterMask(frame,x,y,w,h)
        # draw rect
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        r_gray = gray[y:y+h,x:x+w]
        r_color = frame[y:y+h,x:x+w]
        eyes = eyeCascade.detectMultiScale(r_gray)
        for ex,ey,ew,eh in eyes:
            #filterGlass(frame,ex,ey,ew,eh,x,y,w,h)
            #cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #cv2.circle(r_color,(ex+ew//2,ey+eh//2),20,(0,255,0),2)
            #print(ex,ey,x,y)
            break
def detectNose(faceCascade,noseCascade,frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,6)
    noses = noseCascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        #for nx,ny,nw,nh in noses:
            #filterGasMask(frame,x,y,w,h,nx,ny,nw,nh)
            #cv2.rectangle(frame,(nx,ny),(nx+nw,ny+nh),(0,255,0),2)
def openVideo(cap):
    if cap.isOpened() == False:
        print("error video")
    # face detect
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # eye detect
    eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    # nose detect
    noseCascade = cv2.CascadeClassifier("haarcascade_mcs_nose.xml")
    while (cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame,(230,400))
            # convert to BGRA
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
            # face and eye  detect 
            detectFace(faceCascade,eyeCascade,frame)
            # nose detect
            #detectNose(faceCascade,noseCascade,frame)
            # convert to BGR
            frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
            cv2.imshow("test",frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    # read video
    cap = cv2.VideoCapture("test.mp4")
    openVideo(cap)
