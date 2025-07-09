import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Set camera width (property 3) and height (property 4)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Load Haar cascade classifier for face detection
    faces = cv2.CascadeClassifier("../My_game/faces.xml")
    results = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=6)

    # Draw rectangles around detected faces and apply bitwise AND
    for (x, y, w, h) in results:
        rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), thickness=1)
        img = cv2.bitwise_and(img, rect)

    cv2.imshow("Result", img)

    # Listen for "q" key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
