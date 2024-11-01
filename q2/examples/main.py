import cv2
import numpy as np

# Create a black image
image = np.zeros((500, 500, 3), dtype="uint8")

# Define the top-left and bottom-right coordinates of the rectangle
top_left = (100, 100)
bottom_right = (300, 300)

# Define the color (in BGR format) and thickness of the rectangle
color = (255, 0, 0)   # Blue color
thickness = 2         # Thickness of 2 pixels

# Draw the rectangle
cv2.rectangle(image, top_left, bottom_right, color, thickness)

# Display the image with the rectangle
cv2.imshow("Rectangle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
