import cv2
import numpy
import filters

img = cv2.imread('screenshot.png',1)
dst = img
kernerl = numpy.array([[-1,-1,-1],
                       [-1, 9,-1],
                       [-1,-1,-1]])
cv2.filter2D(img,-1,kernerl,dst)
cv2.imshow('test',dst)
cv2.waitKey()