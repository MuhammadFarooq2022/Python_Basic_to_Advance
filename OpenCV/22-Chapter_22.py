# Face detection in images

import cv2 as cv

face_cascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv.imread("Resources/faces.jpg")
img = cv.resize(img, (450,600))
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

# Draw a rectangle

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv.imshow("image", img)
cv.imwrite("Resources/face.jpg", img)
cv.waitKey(0)
cv.destroyAllWindows()

