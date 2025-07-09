import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)

# Set camera width (property 3) and height (property 4)
cap.set(3, 1920)
cap.set(4, 1080)

while True:
    success, img = cap.read()
    # success: True/False if frame was read; img: the video frame itself

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Example: draw a circle (uncomment if needed)
    # cv2.circle(img_gray, (250, 300), 60, (0, 0, 255), thickness=5)

    img_canny = cv2.Canny(img_gray, 10, 15)

    cv2.imshow("Result", img_canny)

    # Listen for "q" key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
