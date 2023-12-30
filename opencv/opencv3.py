import cv2
import numpy as np

kernel1 = np.ones((5, 5), np.uint8)
kernel2 = np.ones((5, 5), np.uint8)


img = cv2.imread('/Users/xyy/PycharmProjects/LeetCode_MAC/opencv/DATA/colorcolor.jpg')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
blur = cv2.GaussianBlur(img, (5, -87), 10)  # 高斯模糊
canny = cv2.Canny(img, 150, 200)  # 邊緣處理
dilate = cv2.dilate(canny, kernel1, iterations=1)  # 膨脹效果 kernel必須是二維陣列 iterations為膨脹次數
erode = cv2.erode(dilate, kernel2, iterations=1 )  # 侵蝕 將線條變細


cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)
