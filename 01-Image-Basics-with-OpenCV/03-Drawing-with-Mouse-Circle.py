import cv2
import numpy as np

drawing = False
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):

    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),10,(255,255,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

img = np.zeros((512,512,3),np.uint8)

while True:
    
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
    