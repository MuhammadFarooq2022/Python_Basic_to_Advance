# Split your video into frames or image sequence

import cv2 as cv
cap = cv.VideoCapture("Resources/Video.mp4")

frameNr = 0

while (True):
    success, frame = cap.read()
    if success:
        cv.imwrite(f"Resources/Frames/frame_{frameNr}.jpg", frame)
    else:
        break
    frameNr = frameNr+1
cap.release()