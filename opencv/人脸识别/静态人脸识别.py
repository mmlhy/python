import cv2

filename = 'we.jpg'

def detect(filename):
    face_cascade = cv2.CascadeClassifier('/home/miaomeng/桌面/python/opencv/人脸识别/cascades/haarcascade_frontalface_default.xml')
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    #faces = face_cascade.detectMultiScale(gray, 1.1, 5, cv2.CASCADE_SCALE_IMAGE, (50, 50), (100, 100))
    for(x,y,w,h)in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.namedWindow('vikings detected!!')
    cv2.imshow('vikings detected!!',img)
    cv2.imwrite('vikings.jpg',img)
    cv2.waitKey()
detect(filename)