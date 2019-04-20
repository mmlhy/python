import cv2
import os
import sys
import numpy as np

def read_images(path,sz=None):
    c=0
    x,y = [],[]
    for dirname,dirnames,filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname,subdirname)
            for filename in os.listdir(subject_path):
                try:
                    if(filename==".directory"):
                        continue
                    filepath = os.path.join(subject_path,filename)
                    im = cv2.imread(os.path.join(subject_path,filename),cv2.IMREAD_GRAYSCALE)

                    im = cv2.resize(im,(200,200))
                    x.append(np.asarray(im,dtype=np.uint8))
                    y.append(c)
                except IOError (errno,strerror):
                    print("I/O error({0}):{1}".format(errno,strerror))
                except:
                    print("Unexpected error:",sys.exc_info()[0])
                    raise
            c=c+1
    return [x,y]

def face_rec():
    names = ['tom','Jane','Jack']
    [x,y] = read_images('./test')
    print(y)
    if x is None :
        print("error!no data")
        sys.exit()
    y = np.asarray(y, dtype=np.int32)
    model = cv2.face.EigenFaceRecognizer_create()
    model.train(np.asarray(x), np.asarray(y))
    camera = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(
        './cascades/haarcascade_frontalface_default.xml')
    while True:
        read,img = camera.read()
        faces = face_cascade.detectMultiScale(img, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            roi = gray[x:x + w, y:y + h]
            try:
                roi = cv2.resize(roi, (200, 200), interpolation=cv2.INTER_LINEAR)
                params = model.predict(roi)
                print("Label: %s, Confidence: %.2f" % (params[0], params[1]))
                cv2.putText(img, names[params[0]], (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)
            except:
                continue
        cv2.imshow("camera", img)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
	 face_rec()
	 cv2.waitKey(0)