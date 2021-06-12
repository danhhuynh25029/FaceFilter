import cv2
import numpy as np
from filterNose import *
from filterFace import *
from filterEye import *
from filterMouth import *
def detectFace(faceCascade,eyeCascade,frame,f):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        # filter Heart
        if f == 0:
            filterHeart(frame,x,y,w,h,"images/heart.png")
        if f == 1:
            filterHeart(frame,x,y,w,h,"images/devil.png")
        # anonymus mask
        if f == 2:
            filterMask(frame,x,y,w,h,"images/a1.png")
        if f == 3:
            filterMask(frame,x,y,w,h,"images/bread.png")
        if f == 4:
            filterMask(frame,x,y,w,h,"images/iron.png")
        # draw rect
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        r_gray = gray[y:y+h,x:x+w]
        r_color = frame[y:y+h,x:x+w]
        eyes = eyeCascade.detectMultiScale(r_gray)
        for ex,ey,ew,eh in eyes:
            if f == 5:
                filterGlass(frame,ex,ey,ew,eh,x,y,w,h,"images/sunglasses.png")
            if f == 6:
                filterGlass(frame,ex,ey,ew,eh,x,y,w,h,"images/glasseslife.png")
            if f == 7:
                filterGlass(frame,ex,ey,ew,eh,x,y,w,h,"images/glasses.png")
            if f == 8:
                filterGlass(frame,ex,ey,ew,eh,x,y,w,h,"images/glassespink.png")
            #cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            #cv2.circle(r_color,(ex+ew//2,ey+eh//2),20,(0,255,0),2)
            #print(ex,ey,x,y)
            break
def detectMouth(mouthCascade,frame,f):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mouths = mouthCascade.detectMultiScale(gray,1.7,11)
    for x,y,w,h in mouths:
        filterMouthColor(frame,x,y,w,h,"images/mouth1.png")
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
def detectNose(faceCascade,noseCascade,frame,f):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,6)
    noses = noseCascade.detectMultiScale(gray,1.3,6)
    for x,y,w,h in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        for nx,ny,nw,nh in noses:
            if f == 0:
                filterGasMask(frame,x,y,w,h,nx,ny,nw,nh,"images/facemask.png")
            if f == 1:
                filterBeard(frame,x,y,w,h,nx,ny,nw,nh,"images/beard.png")
            #cv2.rectangle(frame,(nx,ny),(nx+nw,ny+nh),(0,255,0),2)
def openVideo(cap,d,f):
    if cap.isOpened() == False:
        print("error video")
    # face detect
    faceCascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")
    # eye detect
    eyeCascade = cv2.CascadeClassifier("xml/haarcascade_eye.xml")
    # nose detect
    noseCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_nose.xml")
    # mouse detect
    mouthCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_mouth.xml")
    while (cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame,(230,400))
            # convert to BGRA
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
            # face and eye  detect
            if d == 0:
                detectFace(faceCascade,eyeCascade,frame,f)
            # nose detect
            if d == 1:
                detectNose(faceCascade,noseCascade,frame,f)
            # mouth detect
            if d == 2:
                detectMouth(mouthCascade,frame,f)
            # convert to BGR
            frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
            cv2.imshow("test",frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
def run():
    cap = cv2.VideoCapture("test.mp4")
    openVideo(cap,0,4)
if __name__ == "__main__":
    # read video
    # cap = cv2.VideoCapture("test.mp4")
    # openVideo(cap,0,4)
    run()