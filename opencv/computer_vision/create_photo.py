import cv2
import numpy as np

# Create a blank image using a NumPy matrix
photo = np.zeros((450, 450, 3), dtype="uint8")

# You can also fill a region with color using slicing:
# photo[110:150, 110:200] = (110, 210, 155)
# Note: OpenCV uses BGR color format, not RGB!

# Draw a filled rectangle
# (image, top-left corner, bottom-right corner, color (BGR), thickness or cv2.FILLED)
cv2.rectangle(photo, (0, 0), (100, 100), (110, 210, 155), thickness=cv2.FILLED)

# Draw a line
# (image, start_point, end_point, color (BGR), thickness)
cv2.line(
    photo,
    (0, photo.shape[0] // 2),
    (photo.shape[1] // 2, photo.shape[0] // 2),
    (255, 0, 0),
    thickness=5,
)

# Draw a circle
# (image, center, radius, color (BGR), thickness)
cv2.circle(
    photo,
    (photo.shape[1] // 2, photo.shape[0] // 2),
    50,
    (222, 221, 220),
    thickness=2,
)

# Add text to the image
# (image, text, org (bottom-left corner), font, fontScale, color, thickness)
cv2.putText(photo, "itsText", (100, 150), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), thickness=2)

# Show the result
cv2.imshow("Ready", photo)
cv2.waitKey(0)
