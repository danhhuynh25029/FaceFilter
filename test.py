import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk
from main import *
from tkinter import ttk
from tkinter_custom_button import TkinterCustomButton as ButtonC
import datetime
import os
#load xml
# face detect
faceCascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")
# eye detect
eyeCascade = cv2.CascadeClassifier("xml/haarcascade_eye.xml")
# nose detect
noseCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_nose.xml")
# mouth detect
mouthCascade = cv2.CascadeClassifier("xml/haarcascade_mcs_mouth.xml")
frame_width = 230
frame_height = 400
# choose video or image
video = True
camera = False
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
#time = datetime.datetime.now()
count = 1
out = cv2.VideoWriter()
#Set up GUI
d,f = 1000,1000
tmp = False
Record = False
def Snapshot(event):
    global tmp
    tmp = True
def shiftImage(event):
    global count ,Record
    count += 1
    if count % 2 == 0 and count != 0:
        Record = True
        canvas1.itemconfig(button, image=srecord_image)
    else:
        Record = False
        canvas1.itemconfig(button, image=record_image)
window = tk.Tk()  #Makes main window
window.wm_title("Tiktok fake")
window.config(background="#2d3436")
window.geometry("600x550")
# create label
label1 = tk.Label(window,borderwidth=0)
# recored video
# out = cv2.VideoWriter('outpy'+str(time)+str(count)+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
# camera 
#nameImage = str(time)+".jpg"
#nameVideo = str(time)+".avi"
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
def clearFilter():
    global d,f
    d,f = -1,-1
def setImage():
    global image,video
    image = True
    video = False
def setVideo():
    global image,video
    image = True
    video = False
# option
# def Cam():
#     global tmp
#     tmp = False
# def Video():
#     global tmp
#     tmp = True
# button record
recordImage = cv2.imread("images/record.png",-1)
recordImage = cv2.resize(recordImage,(50,50))
cv2Record = cv2.cvtColor(recordImage, cv2.COLOR_BGR2RGBA)
recordImage = Image.fromarray(cv2Record)
record_image = ImageTk.PhotoImage(image=recordImage)
srecordImage = cv2.imread("images/stoprecord.png",-1)
srecordImage = cv2.resize(srecordImage,(50,50))
scv2Record = cv2.cvtColor(srecordImage, cv2.COLOR_BGR2RGBA)
srecordImage = Image.fromarray(scv2Record)
srecord_image = ImageTk.PhotoImage(image=srecordImage)
    # Video is ready
if video == True:
    # snapshot
    camera = cv2.imread("images/Camera_Icon.jpg",-1)
    cameraImage =cv2.resize(camera,(50,50))
    cv2Camera = cv2.cvtColor(cameraImage,cv2.COLOR_BGR2BGRA)
    cameraImage = Image.fromarray(cv2Camera)
    camera = ImageTk.PhotoImage(image=cameraImage)
    #record button
    blank =  cv2.imread("images/blankButton.png",-1)
    blank = cv2.resize(blank,(50,50))
    cv2blank = cv2.cvtColor(blank,cv2.COLOR_BGR2RGBA)
    blank_img = Image.fromarray(cv2blank)
    blankImage = ImageTk.PhotoImage(image=blank_img)
    canvas1 = tk.Canvas(window, width=50, height=50)
    button = canvas1.create_image(0, 0, anchor=tk.NW, image=record_image)
    blank = canvas1.create_image(0, 0, anchor=tk.NW, image=blankImage, state=tk.NORMAL)
    canvas1.tag_bind(blank, "<Button-1>", shiftImage)
    canvas1.place(x=480,y=460)
    #0----
    # snapshot button
    canvas2 = tk.Canvas(window, width=50, height=50)
    button = canvas2.create_image(0, 0, anchor=tk.NW, image=camera)
    blank = canvas2.create_image(0, 0, anchor=tk.NW, image=blankImage, state=tk.NORMAL)
    canvas2.tag_bind(blank, "<Button-1>", Snapshot)
    canvas2.place(x=300,y=460)
if camera == True:
    pass
print(video)
# button Image
#buttonImage = ButtonC(text="image",command=setImage,height=30,width=50,borderwidth=0)
#buttonImage.place(x=40,y=5)
#button video
#buttonVideo = ButtonC(text="video",command=setVideo,height=30,width=50,borderwidth=0)
#buttonVideo.place(x=20+90,y=5)
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
image3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGBA)
img3 = Image.fromarray(image3)
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
# clear filter
img12 = cv2.imread("images/white.png",-1)
img12 = cv2.resize(img12,(50,50))
cv2image12 = cv2.cvtColor(img12, cv2.COLOR_BGR2RGBA)
img12 = Image.fromarray(cv2image12)
image12 = ImageTk.PhotoImage(image=img12)
b12 = ButtonC(text="clear",command=clearFilter,height=50,width=50,borderwidth=0)
b12.place(x=20+20,y =25+ 300)
# read video
cap = cv2.VideoCapture("test.mp4")
cap.set(cv2.CAP_PROP_FPS, 60) 
def show_frame():
    global out,tmp,Record,time,video
    ret, frame = cap.read()
    time = datetime.datetime.now()
    if video == False:
        return 0
    # Name : d-m-y-h-f
    nameImage = time.strftime("%d")+"-"+time.strftime("%m")+"-"+time.strftime("%Y")+"-"+time.strftime("%H")+"-"+time.strftime("%f")+".jpg"
    nameVideo = time.strftime("%d")+"-"+time.strftime("%m")+"-"+time.strftime("%Y")+"-"+time.strftime("%H")+"-"+time.strftime("%f")+".avi"
    #print(nameImage)
    if ret == True:
        # if ret == True:
        # print(count)
        # print(tmp)
        # print(Record)
        frame = cv2.resize(frame,(230,400))
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2BGRA)
        # face and eye  detect
        if d == 0:
            detectFace(faceCascade,eyeCascade,frame,f)
        # nose detect
        elif d == 1:
            detectNose(faceCascade,noseCascade,frame,f)
        # mouth detect
        elif d == 2:
            detectMouth(mouthCascade,frame,f)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2BGR)
        if tmp == True:
            #print(os.path.dirname(__file__))
            #print(os.path.dirname(os.path.abspath(__file__))+os.sep+nameImage) 
            #cv2.imwrite(os.path.dirname(os.path.abspath(__file__))+os.sep+nameImage,frame)
            cv2.imwrite(nameImage,frame)
            tmp = False
        if Record == True:
            out = cv2.VideoWriter(nameVideo,cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
            Record = False
        if count % 2 == 0 and count != 0:
            out.write(frame)
        # elif count > 2 and count % 2 != 0:
        #     out = cv2.VideoWriter('outpy'+str(time)+str(count)+'.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        image = ImageTk.PhotoImage(image=img)
        # label1 = tk.Label(image=image)
        label1.image = image
        label1.configure(image=image)
        label1.place(x=300, y=20+20)
        label1.after(100,show_frame)

if video == True:
    show_frame()  #Display 2
window.mainloop()  #Starts GUI
