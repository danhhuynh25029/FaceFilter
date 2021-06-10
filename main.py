import cv2
import numpy as np
def filterMask(fram,x,y,w,h):
    pass
def filterGlass(frame,ex,ey,ew,eh,x,y,w,h):
    glass = cv2.imread("sunglasses.png")
    #glass = cv2.cvtColor(glass,cv2.COLOR_BGR2BGRA)
    glass = cv2.resize(glass,(w,50))
    for i in range(50):
        for j in range(w):
            if glass[i][j][2] != 0:
                frame[i+ey+y][x+j] = glass[i][j]                
    #cv2.circle(frame,(w//2+x,h//2+y),10,(0,255,0),2)
    
def filterHeart(frame,x,y,w,h):
    hair = cv2.imread("heart.png")
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
        #filterHeart(frame,x,y,w,h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        r_gray = gray[y:y+h,x:x+w]
        r_color = frame[y:y+h,x:x+w]
        eyes = eyeCascade.detectMultiScale(r_gray)
        for ex,ey,ew,eh in eyes:
            filterGlass(frame,ex,ey,ew,eh,x,y,w,h)
            #cv2.circle(frame,(x+ex+ew//2,y+ey+eh//2),20,(0,255,0),2)
            break
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
