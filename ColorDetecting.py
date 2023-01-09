import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    
    ret,frame = cam.read()
    frame = cv2.flip(frame, 1)
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerRed = np.array([0,145,145])
    upperRed = np.array([10,255,255])
    redMask = cv2.inRange(hsvFrame, lowerRed, upperRed)
    
    red = cv2.bitwise_and(frame, frame, mask = redMask)
    
    cv2.imshow("webcam", frame)
    cv2.imshow("Red Mask", redMask)
    cv2.imshow("Red",red)
    
    key = cv2.waitKey(30)
    if key == 27:
        break

cam.release()
cam.destroyAllWindows()