import cv2

class Camera:
    def __init__(self):
        self.capture = None

    def start(self):
        self.capture = cv2.VideoCapture(0)

    def get_frame(self):
        if self.capture is not None:
            ret, frame = self.capture.read()
            if ret and frame is not None and frame.size > 0:
                return frame
        # Return a black frame of standard size if invalid
        return cv2.imread(cv2.samples.findFile('lena.jpg')) if cv2.haveImageReader('lena.jpg') else None

    def release(self):
        if self.capture is not None:
            self.capture.release()