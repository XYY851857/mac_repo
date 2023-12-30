import cv2
import numpy as np
import random
high, width = 300, 300

img = np.empty((high, width, 3), np.uint8)
x, y, = 0, 0
for row in range(high):
    # if row < 255:
    #     x += 1
    # else:
    #     x -= 1
    if row < 255:
        x = row + 1
    for col in range(width):
        # if col < 255:
        #     y += 1
        # else:
        #     y -= 1
        if col < 255:
            y = col + 1
        # img[row][col] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        img[row][col] = [x, 0, y]
cv2.imshow('img', img)
cv2.waitKey(1500)