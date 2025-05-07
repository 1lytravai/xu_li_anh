# Additional Exercises

import cv2 as cv
import numpy as np

# page 25
# change the pixels whose intensity values are
# smaller than 128 to black color and otherwise to white color

def ex_page_25():
    m = np.array([[0, 255, 255, 255, 0], 
                    [0, 190, 190, 190, 0],
                    [0, 127, 127, 127, 0],
                    [0, 0, 0, 0, 0]])
    # print(page25[0]) -> [0, 255, 255, 255, 0]
    # print(page25[0][0]) -> 0

    rows = len(m)
    cols = len(m[0])

    for r in range(rows):
        for c in range(cols):
            if m[r][c] > 128: m[r][c] = 0
            else: m[r][c] = 1
    return m

def ex_page_32():
    m = np.array([
        [ [0, 0, 255], [0, 255, 0], [255, 0, 0] ],
        [ [255, 0, 0], [255, 0, 255], [0, 0, 255] ]
    ], dtype=np.uint8)
    print(m[0])
    print(m[0][0])

    for r in range(len(m)):
        for c in range(lem(m[0])):
            if m[r, c] == [255, 255, 0]: m[r, c] = [255, 255, 255]
            else: pass

# print(ex_page_25())
ex_page_32()    
