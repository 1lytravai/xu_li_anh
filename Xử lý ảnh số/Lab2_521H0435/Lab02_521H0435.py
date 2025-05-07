import cv2 as cv
import numpy as np

img = cv.imread('lab02_ex.png')
img_2 = cv.imread('lab02_ex.png')
# 1. Split each color channel of the image
b, g, r = cv.split(img)

# 2. Locate the position of each balloon by drawing a rectangle 
# (bounding-box) surrounding each balloon

yellow_ballon_rec = cv.rectangle(img_2, (16, 16), (140, 350), (255, 0, 0), 1)
blue_ballon_rec = cv.rectangle(img_2, (145, 60), (235, 360), (255, 0, 0), 1)
# (145, 60), (240, 360) 
# left: 145 -> right 235
# top: 60 -> bottom: 360
red_ballon_rec = cv.rectangle(img_2, (252, 20), (355, 360), (255, 0, 0), 1)
green_ballon_rec = cv.rectangle(img_2, (375, 60), (475, 360), (255, 0, 0), 1)
orange_ballon_rec = cv.rectangle(img_2, (490, 20), (589, 360), (255, 0, 0), 1)

# cv.imshow("IMAGE", img_2)
# cv.imshow("Located Yellow Ballon", yellow_ballon_rec)
# cv.imshow("Located Blue Ballon", blue_ballon_rec)
# cv.imshow("Located Red Ballon", red_ballon_rec)
# cv.imshow("Located Green Ballon", green_ballon_rec)
# cv.imshow("Located Orange Ballon", orange_ballon_rec)

# 3. Name each balloon by putting a text of color name right above the bounding boxes.
font = cv.FONT_HERSHEY_SIMPLEX
img_2 = cv.putText(img_2, "Yellow", (130, 18), font, 1, (255, 0, 0), 1, cv.LINE_AA)
img_2 = cv.putText(img_2, "Blue", (235, 60), font, 1, (255, 0, 0), 1, cv.LINE_AA)
img_2 = cv.putText(img_2, "Red", (355, 20), font, 1, (255, 0, 0), 1, cv.LINE_AA)
img_2 = cv.putText(img_2, "Green", (475, 60), font, 1, (255, 0, 0), 1, cv.LINE_AA)
img_2 = cv.putText(img_2, "Orange", (589, 20), font, 1, (255, 0, 0), 1, cv.LINE_AA)
# cv.imshow("EX3", img_2)

# 4. Extract the yellow balloon by creating a new image of only one balloon
# img[15:350, 25:140]
# 15:350 -> top to bottom
# 25:140 -> left to right
yellow_ballon = img[16:350, 25:140]
# cv.imshow("Yellow Ballon", yellow_ballon)

# 5. Extract the yellow balloon automatically by using 
# HSV color space to extract only pixels of yellow color

# change to HSV color space
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower_yellow = np.array([25, 50, 70])
higher_yellow = np.array([35, 255, 255])
# create a mask
mask1 = cv.inRange(hsv_img, lower_yellow, higher_yellow)
# Extract original color (yellow)
ex5_img = cv.bitwise_and(img, img, mask=mask1)
# cv.imshow("Ex5 - image", ex5_img)

# 6. Re-paint the yellow balloon by replacing the pixels of yellow by green.
hsv_green = hsv_img.copy()
mask2 = cv.inRange(hsv_green, np.array([36, 50, 70]), np.array([89, 255, 255]))
hsv_green[np.where(mask2)] += np.array(,dtype=np.uint8)    
green_img = 255 - cv.cvtColor(hsv_green, cv.COLOR_HSV2BGR)
# 
cv.imshow("HSV green", green_img)


# 7. Rotate the first balloon an angle of 20 degree


# cv.imshow("image", img)

cv.waitKey(0)
cv.destroyAllWindows()