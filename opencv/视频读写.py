import os
import cv2
import numpy
import matplotlib.pyplot as plt

videoCapture = cv2.VideoCapture('output.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'Mytest.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
    fps,size)
success,frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success,frame = videoCapture.read()