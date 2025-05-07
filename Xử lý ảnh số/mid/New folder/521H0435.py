import cv2
import numpy as np

def is_circle(contour):
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)
    if perimeter == 0:
        return False
    circularity = 4 * np.pi * (area / (perimeter * perimeter))
    return  0.7 < circularity < 1.3

def detect_and_classify_sign(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detected_signs = []

    for contour in contours:
        if cv2.contourArea(contour) > 500:
            if is_circle(contour):
                x, y, w, h = cv2.boundingRect(contour)
                if 50 < w < 350 and 50 < h < 350:  # Dieu chinh kich thuoc
                    roi = img[y:y+h, x:x+w]
                    resized_roi = cv2.resize(roi, (100, 100))
                    detected_signs.append((x, y, w, h, resized_roi))
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imwrite("output_detected_signs.jpg", img)
    return img, detected_signs

def classify_sign(sign_image):
    hsv = cv2.cvtColor(sign_image, cv2.COLOR_BGR2HSV)

    # Red color detection
    red_mask1 = cv2.inRange(hsv, (0, 50, 50), (10, 255, 255))
    red_mask2 = cv2.inRange(hsv, (160, 50, 50), (180, 255, 255))
    red_mask = cv2.bitwise_or(red_mask1, red_mask2)
    red_area = cv2.countNonZero(red_mask)
    total_area = sign_image.shape[0] * sign_image.shape[1]
    red_ratio = red_area / total_area

    # Blue color detection
    blue_mask = cv2.inRange(hsv, (100, 50, 50), (140, 255, 255))
    blue_area = cv2.countNonZero(blue_mask)
    blue_ratio = blue_area / total_area

    # White color detection
    white_lower = (0, 0, 200)
    white_upper = (180, 30, 255)
    white_mask = cv2.inRange(hsv, white_lower, white_upper)
    white_area = cv2.countNonZero(white_mask)
    white_ratio = white_area / total_area

    # Black mask
    black_lower = (0, 0, 0)
    black_upper = (180, 255, 30) # Adjust these values for better black detection
    black_mask = cv2.inRange(hsv, black_lower, black_upper)
    black_area = cv2.countNonZero(black_mask)
    black_ratio = black_area / total_area

    if red_ratio > 0.6 and black_ratio < 0.1:
        return "stop"
    elif 0.6 > red_ratio > 0.55 and black_ratio < 0.1 and blue_ratio < 0.01:
        return "no entry sign"
    elif blue_ratio > 0.4 and red_ratio > 0.1:
        return "No parking"
    elif blue_ratio > 0.2 and red_ratio > 0.1:
        return "No parking and stop"
    elif white_ratio > 0.6 and black_ratio < 0.01:
        return "no entry"
    elif blue_ratio > 0.01 and black_ratio < 0.01 and white_ratio < 0.1:
        return "Even-day"
    elif red_ratio > 0.1 and black_ratio > 0.01:
        return "no straight"
    elif blue_ratio > 0.01 and black_ratio < 0.01:
        return "no turning back"
    else:
        gray = cv2.cvtColor(sign_image, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(cv2.Canny(gray, 50, 150), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            find = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
            if len(cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)) == 4:
                return ""
            if red_ratio > 0.3 and white_ratio > 0.3 and len(find) == 8:
                return "give way to motor vihicles"
            if len(find) == 6 and blue_ratio > 0.01:
                return "stop all"
            if blue_ratio > 0.01 and red_ratio > 0.05 and white_ratio > 0.1:
                return "Odd-day"
            if len(find) == 6:
                return "maximum"
            if red_ratio > 0.1 and black_ratio > 0.01:
                return "no car"
            if 6 < len(find) < 10:
                return "maximum weight"
                continue

    return "unknown"

image_path = 'input_32.jpg'
original_img, detected_signs = detect_and_classify_sign(image_path)

for i, (x, y, w, h, sign) in enumerate(detected_signs):
    sign_name = classify_sign(sign)
    cv2.putText(original_img, sign_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    sign_path = f'detected_sign_{i}_{sign_name}.jpg'
    cv2.imwrite(sign_path, sign)
    print(f"Detected sign {i}: {sign_name}, saved at {sign_path}")

cv2.imwrite("output_labeled.jpg", original_img)
cv2.waitKey(0)
cv2.destroyAllWindows()