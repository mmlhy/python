import os
import cv2
import numpy
import matplotlib.pyplot as plt

cameraCapture = cv2.VideoCapture(0)
fps = 30   
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'Mytest.avi',cv2.VideoWriter_fourcc('I','4','2','0'),
    fps,size)
success,frame = cameraCapture.read()
print(cameraCapture.isOpened())
numFramesRemaining = 10 * fps -1
while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    numFramesRemaining -= 1
    success,frame = cameraCapture.read()
cameraCapture.release()