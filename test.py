import cv2
import numpy as np
img = cv2.imread("sunglasses.png", -1)
#img = cv2.imread("sunglasses.png")
#img = cv2.resize(img,(300,50))
#img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
for i in range(50):
    for j in range(300):
        if img[i][j][2] == 0:
            print(img[i][j])
cv2.imshow("test",img)
cv2.waitKey(0)
