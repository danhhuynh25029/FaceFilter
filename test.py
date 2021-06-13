import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from main import *
from tkinter import ttk
from tkinter_custom_button import TkinterCustomButton as ButtonC
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
tmp = 0
count = 0
def shiftImage(event):
    if count % 2 == 0:
        canvas1.itemconfig(button, image=srecord_image)

    else:
        canvas1.itemconfig(button, image=record_image)
    globals()['count'] += 1
def Record():
    global tmp
    record.image = srecord_image
    tmp = 1
def stopRecord():
    global tmp 
    record.image = record_image
    tmp = 0
window = tk.Tk()  #Makes main window
window.wm_title("Tiktok fake")
window.config(background="#2d3436")
window.geometry("600x550")
# create label
label1 = tk.Label(window,borderwidth=0)
#filter
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
# button record

recordImage = cv2.imread("images/record.png",-1)
recordImage = cv2.resize(recordImage,(30,30))
cv2Record = cv2.cvtColor(recordImage, cv2.COLOR_BGR2RGBA)
recordImage = Image.fromarray(cv2Record)
record_image = ImageTk.PhotoImage(image=recordImage)
srecordImage = cv2.imread("images/stoprecord.png",-1)
srecordImage = cv2.resize(srecordImage,(30,30))
scv2Record = cv2.cvtColor(srecordImage, cv2.COLOR_BGR2RGBA)
srecordImage = Image.fromarray(scv2Record)
srecord_image = ImageTk.PhotoImage(image=srecordImage)
#test
blankImage = ImageTk.PhotoImage(file='images/blankButton.png')

canvas1 = tk.Canvas(window, width=100, height=100)
button = canvas1.create_image(30, 30, anchor=tk.NW, image=record_image)
blank = canvas1.create_image(30, 30, anchor=tk.NW, image=blankImage, state=tk.NORMAL)
canvas1.tag_bind(blank, "<Button-1>", shiftImage)
canvas1.place(x=390,y=460)
#0----

# heart filter
img = cv2.imread("images/heart.png",-1)
img = cv2.resize(img,(50,20))
cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
img = Image.fromarray(cv2image)
image = ImageTk.PhotoImage(image=img)
b = ButtonC(image=image,command=filterHeart,height=50,width=50,borderwidth=0)
b.place(x=20+ 20,y =25+ 20)
# devil filter
img1 = cv2.imread("images/devil.png",-1)
img1 = cv2.resize(img1,(50,20))
cv2image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGBA)
img1 = Image.fromarray(cv2image1)
image1 = ImageTk.PhotoImage(image=img1)
b1 = ButtonC(image=image1,command=filterDevil,height=50,width=50,borderwidth=0)
b1.place(x=20+ 90,y =25+ 20)
# mask anonymus
img2 = cv2.imread("images/a1.png",-1)
img2 = cv2.resize(img2,(50,30))
cv2image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGBA)
img2 = Image.fromarray(cv2image2)
image2 = ImageTk.PhotoImage(image=img2)
b2 = ButtonC(image=image2,command=filterAnonymus,height=50,width=50,borderwidth=0)
b2.place(x=20+ 160,y =25+ 20)
# mask bread
img3 = cv2.imread("images/bread.png",-1)
img3 = cv2.resize(img3,(50,30))
cv2image3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGBA)
img3 = Image.fromarray(cv2image3)
image3 = ImageTk.PhotoImage(image=img3)
b3 = ButtonC(image=image3,command=filterBread,height=50,width=50,borderwidth=0)
b3.place(x=20+ 20,y =25+ 90)
# mask Ironman
img4 = cv2.imread("images/iron.png",-1)
img4 = cv2.resize(img4,(50,30))
cv2image4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGBA)
img4 = Image.fromarray(cv2image4)
image4 = ImageTk.PhotoImage(image=img4)
b4 = ButtonC(image=image4,command=filterIron,height=50,width=50,borderwidth=0)
b4.place(x=20+90,y =25+ 90)
# filter Sun glasses
img5 = cv2.imread("images/sunglasses.png",-1)
img5 = cv2.resize(img5,(50,25))
cv2image5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGBA)
img5 = Image.fromarray(cv2image5)
image5 = ImageTk.PhotoImage(image=img5)
b5 = ButtonC(image=image5,command=filterSunGlasses,height=50,width=50,borderwidth=0)
b5.place(x=20+ 160,y =25+ 90)
#filter Glasses ThugLife
img6 = cv2.imread("images/glasseslife.png",-1)
img6 = cv2.resize(img6,(50,25))
cv2image6 = cv2.cvtColor(img6, cv2.COLOR_BGR2RGBA)
img6 = Image.fromarray(cv2image6)
image6 = ImageTk.PhotoImage(image=img6)
b6 = ButtonC(image=image6,command=filterGlassesLife,height=50,width=50,borderwidth=0)
b6.place(x=20+ 20,y =25+ 160)
#filter Glasses 
img7 = cv2.imread("images/glasses.png",-1)
img7 = cv2.resize(img7,(50,30))
cv2image7 = cv2.cvtColor(img7, cv2.COLOR_BGR2RGBA)
img7 = Image.fromarray(cv2image7)
image7 = ImageTk.PhotoImage(image=img7)
b7 = ButtonC(image=image7,command=filterGlasses,height=50,width=50,borderwidth=0)
b7.place(x=20+ 90,y =25+ 160)
# filter GlassesPink
img8 = cv2.imread("images/glassespink.png",-1)
img8 = cv2.resize(img8,(50,30))
cv2image8 = cv2.cvtColor(img8, cv2.COLOR_BGR2RGBA)
img8 = Image.fromarray(cv2image8)
image8 = ImageTk.PhotoImage(image=img8)
b8 = ButtonC(image=image8,command=filterGlassesPink,height=50,width=50,borderwidth=0)
b8.place(x=20+ 160,y =25+ 160)
# filter face Mask
img9 = cv2.imread("images/facemask.png",-1)
img9 = cv2.resize(img9,(50,30))
cv2image9 = cv2.cvtColor(img9, cv2.COLOR_BGR2RGBA)
img9 = Image.fromarray(cv2image9)
image9 = ImageTk.PhotoImage(image=img9)
b9 = ButtonC(image=image9,command=filterFaceMask,height=50,width=50,borderwidth=0)
b9.place(x=20+ 20,y =25+ 230)
# filter Beard
img10 = cv2.imread("images/beard.png",-1)
img10 = cv2.resize(img10,(50,30))
cv2image10 = cv2.cvtColor(img10, cv2.COLOR_BGR2RGBA)
img10 = Image.fromarray(cv2image10)
image10 = ImageTk.PhotoImage(image=img10)
b10 = ButtonC(image=image10,command=filterBeard,height=50,width=50,borderwidth=0)
b10.place(x=20+ 90,y =25+ 230)
# filter MouthColor
img11 = cv2.imread("images/mouth1.png",-1)
img11 = cv2.resize(img11,(50,30))
cv2image11 = cv2.cvtColor(img11, cv2.COLOR_BGR2RGBA)
img11 = Image.fromarray(cv2image11)
image11 = ImageTk.PhotoImage(image=img11)
b11 = ButtonC(image=image11,command=filterMouthColor,height=50,width=50,borderwidth=0)
b11.place(x=20+ 160,y =25+ 230)
cap = cv2.VideoCapture("test.mp4")
cap.set(cv2.CAP_PROP_FPS, 60) 
def show_frame():
    ret, frame = cap.read()
    if ret == True:
        # if ret == True:
        print(count)
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
        # label1 = tk.Label(image=image)
        label1.image = image
        label1.configure(image=image)
        label1.place(x=300, y=20+20)
        label1.after(100,show_frame)
show_frame()  #Display 2
window.mainloop()  #Starts GUI