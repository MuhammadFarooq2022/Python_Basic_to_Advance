# Setting of Camera or Videos

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

cap.set(10, 100) # 10 is the key to set brightness
cap.set(3, 640) # width key 3
cap.set(4, 480) # height key 4

while (True):
    (ret, frame) = cap.read()
    # To show in player
    if ret == True:
        cv.imshow("frame", frame)
        # To quit with q key
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()