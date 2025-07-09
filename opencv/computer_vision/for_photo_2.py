import cv2
import numpy as np

img = cv2.imread("C://for_cv.png")
new_img = np.zeros(img.shape, dtype="uint8")

# Function to rotate an image by a given angle (in degrees)
def rotate(img, angle):
    height, width = img.shape[:2]
    center = (width // 2, height // 2)  # Find the image center
    matrix = cv2.getRotationMatrix2D(center, angle, 1)  # Create rotation matrix (no scaling)
    return cv2.warpAffine(img, matrix, (width, height))  # Apply rotation

# Function to move (translate) an image by x, y pixels
def move(img, x, y):
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img, matrix, (img.shape[1], img.shape[0]))

# Example: rotate the image 360 degrees (full rotation)
img = rotate(img, 360)

# Example: move image by (0,0) (no shift, just for demonstration)
img = move(img, 0, 0)

"""
Finding contours workflow:
- Convert to grayscale for easier processing
- Apply Gaussian blur to reduce noise
- Detect edges (Canny)
- Find contours
- Draw contours on a blank image
"""
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)
img = cv2.Canny(img, 100, 140)

# Find contours
# contours, hierarchy = cv2.findContours(image, mode, method)
# mode: contour retrieval mode; method: contour approximation method
contours, hierarchy = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# Draw contours on a new image
cv2.drawContours(new_img, contours, -1, (230, 144, 204), 1)

"""
contours: List of all found contours. Each contour is a list of (x, y) points.
hierarchy: Describes the relationships between contours (such as nested contours).
"""

cv2.imshow("result", new_img)
cv2.waitKey(0)
