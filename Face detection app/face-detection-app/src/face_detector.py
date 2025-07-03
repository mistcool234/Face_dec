import cv2

class FaceDetector:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        # Load the pre-trained face detection model
        self.model = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_faces(self, frame):
        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.model.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)
        return faces