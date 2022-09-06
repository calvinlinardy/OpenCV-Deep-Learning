import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(200,19,43),-1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,pt1=(x-20,y-20),pt2=(x+20,y+20),color=(255,255,43),thickness=-1)

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

img = np.zeros((512,512,3),np.uint8)

while True:
    
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
    