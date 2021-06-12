import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from main import *
#load xml
# face detect
faceCascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")
# eye detect
eyeCascade = cv2.CascadeClassifier("xml/haarcascade_eye.xml")
# nose detect
noseCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_nose.xml")
# mouth detect
mouthCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_mouth.xml")
#Set up GUI
d,f = 1000,1000
window = tk.Tk()  #Makes main window
window.wm_title("Tiktok fake")
window.config(background="#FFFFFF")
window.geometry("600x500")
def filterHeart():
    global d,f
    d,f = 0,0
def filterDevil():
    global d,f
    d,f = 0,1
def filterAnonymus():
    global d,f
    d,f = 0,2
def filterBread():
    global d,f
    d,f = 0,3
def filterIron():
    global d,f
    d,f = 0,4
def filterSunGlasses():
    global d,f
    d,f = 0,5
def filterGlassesLife():
    global d,f
    d,f = 0,6
def filterGlasses():
    global d,f
    d,f = 0,7
def filterGlassesPink():
    global d,f
    d,f = 0,8
def filterFaceMask():
    global d,f
    d,f = 1,0
def filterBeard():
    global d,f
    d,f = 1,1
def filterMouthColor():
    global d,f
    d,f = 2,0
# heart filter
b = tk.Button(text="heart",command=filterHeart,height=2,width=3)
b.place(x= 20,y = 20)
# heart filter
b1 = tk.Button(text="devil",command=filterDevil,height=2,width=3)
b1.place(x= 90,y = 20)
# mask anonymus
b2 = tk.Button(text="ano",command=filterAnonymus,height=2,width=3)
b2.place(x= 160,y = 20)
# mask bread
b3 = tk.Button(text="bread",command=filterBread,height=2,width=3)
b3.place(x= 20,y = 90)
# mask Ironman
b4 = tk.Button(text="iron",command=filterIron,height=2,width=3)
b4.place(x= 90,y = 90)
# filter Sun glasses
b5 = tk.Button(text="Sun",command=filterSunGlasses,height=2,width=3)
b5.place(x= 160,y = 90)
#filter Glasses ThugLife
b6 = tk.Button(text="life",command=filterGlassesLife,height=2,width=3)
b6.place(x= 20,y = 160)
#filter Glasses 
b7 = tk.Button(text="glasses",command=filterGlasses,height=2,width=3)
b7.place(x= 90,y = 160)
# filter GlassesPink
b8 = tk.Button(text="Pink",command=filterGlassesPink,height=2,width=3)
b8.place(x= 160,y = 160)
# filter face Mask
b9 = tk.Button(text="fMask",command=filterFaceMask,height=2,width=3)
b9.place(x= 20,y = 230)
# filter Beard
b10 = tk.Button(text="Beard",command=filterBeard,height=2,width=3)
b10.place(x= 90,y = 230)
# filter MouthColor
b11 = tk.Button(text="Color",command=filterMouthColor,height=2,width=3)
b11.place(x= 160,y = 230)
cap = cv2.VideoCapture("test.mp4")
def show_frame():
    _, frame = cap.read()
    frame = cv2.resize(frame,(230,400))
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
    frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    image = ImageTk.PhotoImage(image=img)
    label1 = tk.Label(image=image)
    label1["text"] = "test"
    label1.image = image
    label1.place(x=300, y=20)
    label1.after(10,show_frame)
show_frame()  #Display 2
window.mainloop()  #Starts GUI