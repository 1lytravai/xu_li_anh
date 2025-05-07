import cv2
import numpy as np
from google.colab.patches import cv2_imshow

# Function to detect lane lines
def detect_lane_lines(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform edge detection using Canny
    edges = cv2.Canny(blur, 50, 150)
    
    height, width = frame.shape[:2]
    mask = np.zeros_like(edges)
    roi_vertices = np.array([[(0, height), (width / 2, height / 2), (width, height)]], dtype=np.int32)
    cv2.fillPoly(mask, roi_vertices, 255)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    lines = cv2.HoughLinesP(masked_edges, 2, np.pi/180, 100, minLineLength=50, maxLineGap=100)
    
    line_image = np.zeros_like(frame)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    result = cv2.addWeighted(frame, 0.8, line_image, 1, 0)
    
    return result

cap = cv2.VideoCapture("Lab10_test2.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("video_01_01.avi", fourcc, fps, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    processed_frame = detect_lane_lines(frame)
    
    out.write(processed_frame)
    
    cv2_imshow(processed_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
