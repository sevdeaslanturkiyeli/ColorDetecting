import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    
    ret,frame = cam.read()
    frame = cv2.flip(frame, 1)
    
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerRed = np.array([0,133,133])
    upperRed = np.array([10,255,255])
    redMask = cv2.inRange(hsvFrame, lowerRed, upperRed)
    
    red = cv2.bitwise_and(frame, frame, mask = redMask)
    
    contours, hierarchy = cv2.findContours(redMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x,y), (x +w , y+h),(0,0,255),3)
                
            M = cv2.moments(redMask)

            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cX, cY), 3, (0, 0, 255), 3)     
    
    cv2.imshow("webcam", frame)
    cv2.imshow("Red Mask", redMask)
    cv2.imshow("Red",red)
    
    key = cv2.waitKey(30)
    if key == 27:
        break

cam.release()
cam.destroyAllWindows()
