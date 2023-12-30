import cap
import cv2



cap = cv2.VideoCapture('/Users/xyy/PycharmProjects/LeetCode_MAC/opencv/DATA/thumb.mp4')

# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # 寬度、高度倍率調整，或是直接在dsize中指定像素
while True:
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.1, fy=0.1)
        cv2.imshow('img', frame)
    else:
        break
    cv2.waitKey()

cv2.waitKey(0)