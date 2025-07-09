import cv2
import numpy as np

img = cv2.imread("C://for_cv.png")

# Convert image to LAB color space and back to BGR, then to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Split image into R, G, B channels
r, g, b = cv2.split(img)
# Work with individual channels here if needed

# Merge channels back into a single image
img = cv2.merge([r, g, b])

cv2.imshow("result", img)
cv2.waitKey(0)

