

from google.colab.patches import cv2_imshow
import cv2
import numpy as np

# Load the image
image = cv2.imread('barcode_image.png', cv2.IMREAD_GRAYSCALE)

# Apply thresholding to binarize the image
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours
for contour in contours:
    # Fit a bounding rectangle around the contour
    x, y, w, h = cv2.boundingRect(contour)

    # Draw the bounding rectangle
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Calculate the thickness of each line
    line_thickness = w / 95  # Assuming 95 bars in the barcode

    # Print position and thickness of each line
    print("Position: ({},{}), Thickness: {}".format(x, y, line_thickness))

# Display the result
cv2_imshow(image)