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
img = cv2.imread("images/heart.png",-1)
img = cv2.resize(img,(50,20))
cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
img = Image.fromarray(cv2image)
image = ImageTk.PhotoImage(image=img)
b = tk.Button(image=image,command=filterHeart,height=50,width=50,borderwidth=0)
b.place(x= 20,y = 20)
# devil filter
img1 = cv2.imread("images/devil.png",-1)
img1 = cv2.resize(img1,(50,20))
cv2image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGBA)
img1 = Image.fromarray(cv2image1)
image1 = ImageTk.PhotoImage(image=img1)
b1 = tk.Button(image=image1,command=filterDevil,height=50,width=50,borderwidth=0)
b1.place(x= 90,y = 20)
# mask anonymus
img2 = cv2.imread("images/a1.png",-1)
img2 = cv2.resize(img2,(50,50))
cv2image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGBA)
img2 = Image.fromarray(cv2image2)
image2 = ImageTk.PhotoImage(image=img2)
b2 = tk.Button(image=image2,command=filterAnonymus,height=50,width=50,borderwidth=0)
b2.place(x= 160,y = 20)
# mask bread
img3 = cv2.imread("images/bread.png",-1)
img3 = cv2.resize(img3,(50,50))
cv2image3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGBA)
img3 = Image.fromarray(cv2image3)
image3 = ImageTk.PhotoImage(image=img3)
b3 = tk.Button(image=image3,command=filterBread,height=50,width=50,borderwidth=0)
b3.place(x= 20,y = 90)
# mask Ironman
img4 = cv2.imread("images/iron.png",-1)
img4 = cv2.resize(img4,(50,50))
cv2image4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGBA)
img4 = Image.fromarray(cv2image4)
image4 = ImageTk.PhotoImage(image=img4)
b4 = tk.Button(image=image4,command=filterIron,height=50,width=50,borderwidth=0)
b4.place(x=90,y = 90)
# filter Sun glasses
img5 = cv2.imread("images/sunglasses.png",-1)
img5 = cv2.resize(img5,(50,25))
cv2image5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGBA)
img5 = Image.fromarray(cv2image5)
image5 = ImageTk.PhotoImage(image=img5)
b5 = tk.Button(image=image5,command=filterSunGlasses,height=50,width=50,borderwidth=0)
b5.place(x= 160,y = 90)
#filter Glasses ThugLife
img6 = cv2.imread("images/glasseslife.png",-1)
img6 = cv2.resize(img6,(50,25))
cv2image6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGBA)
img6 = Image.fromarray(cv2image6)
image6 = ImageTk.PhotoImage(image=img6)
b6 = tk.Button(image=image6,command=filterGlassesLife,height=50,width=50,borderwidth=0)
b6.place(x= 20,y = 160)
#filter Glasses 
img7 = cv2.imread("images/glasses.png",-1)
img7 = cv2.resize(img7,(50,30))
cv2image7 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGBA)
img7 = Image.fromarray(cv2image7)
image7 = ImageTk.PhotoImage(image=img7)
b7 = tk.Button(image=image7,command=filterGlasses,height=50,width=50,borderwidth=0)
b7.place(x= 90,y = 160)
# filter GlassesPink
img8 = cv2.imread("images/glassespink.png",-1)
img8 = cv2.resize(img8,(50,30))
cv2image8 = cv2.cvtColor(img8, cv2.COLOR_BGR2RGBA)
img8 = Image.fromarray(cv2image8)
image8 = ImageTk.PhotoImage(image=img8)
b8 = tk.Button(image=image8,command=filterGlassesPink,height=50,width=50,borderwidth=0)
b8.place(x= 160,y = 160)
# filter face Mask
img9 = cv2.imread("images/facemask.png",-1)
img9 = cv2.resize(img9,(50,50))
cv2image9 = cv2.cvtColor(img9, cv2.COLOR_BGR2RGBA)
img9 = Image.fromarray(cv2image9)
image9 = ImageTk.PhotoImage(image=img9)
b9 = tk.Button(image=image9,command=filterFaceMask,height=50,width=50,borderwidth=0)
b9.place(x= 20,y = 230)
# filter Beard
img10 = cv2.imread("images/beard.png",-1)
img10 = cv2.resize(img10,(50,50))
cv2image10 = cv2.cvtColor(img10, cv2.COLOR_BGR2RGBA)
img10 = Image.fromarray(cv2image10)
image10 = ImageTk.PhotoImage(image=img10)
b10 = tk.Button(image=image10,command=filterBeard,height=50,width=50,borderwidth=0)
b10.place(x= 90,y = 230)
# filter MouthColor
img11 = cv2.imread("images/mouth1.png",-1)
img11 = cv2.resize(img11,(50,50))
cv2image11 = cv2.cvtColor(img11, cv2.COLOR_BGR2RGBA)
img11 = Image.fromarray(cv2image11)
image11 = ImageTk.PhotoImage(image=img11)
b11 = tk.Button(image=image11,command=filterMouthColor,height=50,width=50,borderwidth=0)
b11.place(x= 160,y = 230)
cap = cv2.VideoCapture("test.mp4")
def show_frame():
    ret, frame = cap.read()
    if ret == True:
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