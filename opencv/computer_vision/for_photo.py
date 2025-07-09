import cv2  # pip install opencv-python
import numpy as np  # pip install numpy; (np) is an alias for convenience

# Read an image from disk
img = cv2.imread("C://for_cv.png")

# Resize the image to half its original size
new_img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

# Apply Gaussian blur (image, kernel size, sigmaX)
img_blur = cv2.GaussianBlur(img, (9, 9), 5)

# Convert the image to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges using the Canny algorithm
# (image, threshold1, threshold2) — better to use after converting to grayscale
img_canny = cv2.Canny(img_gray, 100, 100)

# Create a kernel matrix for dilation/erosion
kernel = np.ones((5, 5), np.uint8)

# Dilate the edges (adds thickness)
img_dilate = cv2.dilate(img_canny, kernel, iterations=0)

# Erode the edges (reduces thickness)
img_erode = cv2.erode(img_canny, kernel, iterations=0)

# Display the final result
cv2.imshow("Result", img_erode)
# To display a cropped region: cv2.imshow("Result", new_img[0:100, 0:100])

cv2.waitKey(0)  # Wait for a key press (required to keep window open)

# Print the image shape: (height, width, number of channels)
print(img.shape)
