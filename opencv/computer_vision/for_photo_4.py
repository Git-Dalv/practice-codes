import cv2
import numpy as np

photo = cv2.imread("C://for_cv.png")

# Create a blank (single-channel) image for the mask
img = np.zeros(photo.shape[:2], dtype="uint8")

# Draw a filled circle on the mask
circle = cv2.circle(img.copy(), (100, 500), 180, 255, -1)

# Draw a filled rectangle on the mask
square = cv2.rectangle(img.copy(), (25, 25), (250, 350), 255, -1)

# Bitwise AND to combine the two shapes (intersection)
mask = cv2.bitwise_and(square, circle)

# Apply the combined mask to the original photo
result = cv2.bitwise_and(photo, photo, mask=mask)
# Bitwise operation for applying the mask

cv2.imshow("Result", result)
cv2.waitKey(0)