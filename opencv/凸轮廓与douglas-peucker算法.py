import cv2
import numpy as np

# img = cv2.imread('/home/sensetime/edgeBoxes-Cpp-version/output/img/000021_10.png', －１)
# contours,hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.imread('don.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


length = len(contours)
print(length)
for i in range(length):
    cnt = contours[i]
    epsilon = 0.00001 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # cv2.drawContours(img, approx, -1, (0, 0, 255), 3)
    cv2.polylines(img, [approx], True, (0, 0, 255), 2)
cv2.imshow("approx",img)
cv2.waitKey(0)
cv2.destroyAllWindows()