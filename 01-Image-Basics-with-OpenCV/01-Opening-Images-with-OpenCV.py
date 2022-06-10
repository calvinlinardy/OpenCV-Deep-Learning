import cv2

img = cv2.imread('/Users/clcx/Documents/GitHub/OpenCv-Deep-Learning/Pierian/DATA/00-puppy.jpg')

while True:

    cv2.imshow('Puppy',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    
    # IF we've waited at least 1 ms AND we've pressed the Esc
    # jad ini artinya nunggu 1 ms DAN pencet Esc, 27 itu Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
