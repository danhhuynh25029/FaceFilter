import cv2
import numpy as np
def filter(frame,x,y,w,h):
    hair = cv2.imread("clown.png") 
    hair = cv2.resize(hair,(int(w*1),int(h*1)))
    for i in range(int(w*1)):
        for j in range(int(h*1)):
            # color RGBA 
            if hair[i][j][2] != 0: # a != 0
                frame[i][x+j] = hair[i][j]            
                
def detectFace(faceCascade,eyeCascade,frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,5)
    for x,y,w,h in faces:
        filter(frame,x,y,w,h)
       # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
       # r_gray = gray[y:y+h,x:x+w]
       # r_color = frame[y:y+h,x:x+w]
       # eyes = eyeCascade.detectMultiScale(r_gray)
       # for ex,ey,ew,eh in eyes:
        #    cv2.rectangle(r_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
def openVideo(cap):
    if cap.isOpened() == False:
        print("error video")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    eyeCascade = cv2.CascadeClassifier("haarcascade_eye.xml")
    while (cap.isOpened()):
        ret,frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame,(250,400))
            detectFace(faceCascade,eyeCascade,frame)
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
