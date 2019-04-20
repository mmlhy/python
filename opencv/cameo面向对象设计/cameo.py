import cv2
import filters
from managers import WindowManager,CaptureManager

class Cameo(object):
    def __init__(self):
        self._windowManger = WindowManager('Cameo',self.onKeypress)
        self._captureManger = CaptureManager(cv2.VideoCapture(0),self._windowManger,True)
        self._curveFilter = filters.BGRPortraCurveFilter()

    def run(self):
        self._windowManger.createWindow()
        while self._windowManger.isWindowCreated:
            self._captureManger.enterFrame()
            frame = self._captureManger.frame


            filters.strokeEdges(frame,frame)
            self._curveFilter.apply(frame,frame)


            self._captureManger.exitFrame()
            self._windowManger.processEvents()

    def onKeypress(self,keycode):
        """
        空格 截图
        tab  暂停，开始
        esc 退出
        """
        if keycode == 32: # space
            self._captureManger.writeImage('screenshot.png')
        elif keycode == 9: #tab
            if not self._captureManger.isWritingVideo:
                self._captureManger.startWritingVideo('screencast.avi')
            else:
                self._captureManger.stopWritingVideo()
        elif keycode == 27:#escape
            self._windowManger.destroyWindow()

if __name__=="__main__":
        Cameo().run()