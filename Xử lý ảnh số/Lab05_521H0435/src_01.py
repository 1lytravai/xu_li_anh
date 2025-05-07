import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('ex1_img.png', cv.IMREAD_GRAYSCALE) 
hist = cv.calcHist([img],[0],None,[256],[0,256])  

plt.plot(hist)
# plt.show() # image_01_01_hist.png

image_01_01 = cv.imread('image_01_01_hist.png')
font = cv.FONT_HERSHEY_SIMPLEX
org = (100, 100) 
fontScale = 1
color = (0, 0, 255)   
thickness = 1
image_01_01 = cv.putText(image_01_01, '521H0435', org, font,  
                   fontScale, color, thickness, cv.LINE_AA) 
cv.imwrite('image_01_01.png', image_01_01)

equHist = cv.equalizeHist(img)
equHist = cv.putText(equHist, '521H0435', org, font,  
                   fontScale, color, thickness, cv.LINE_AA) 
cv.imwrite('image_01_02.png', equHist)
