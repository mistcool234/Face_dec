import cv2
from camera import Camera
from face_detector import FaceDetector
from utils import draw_faces, display_frame

def main():
    camera = Camera()
    face_detector = FaceDetector()
    
    camera.start()
    
    while True:
        frame = camera.get_frame()
        print(f"Frame: {type(frame)}, None? {frame is None}, Size: {getattr(frame, 'size', 'N/A')}")
        if frame is None or frame.size == 0:
            print("No valid frame received. Exiting loop.")
            break

        faces = face_detector.detect_faces(frame)
        print(f"Faces detected: {faces}")
        frame_with_faces = draw_faces(frame, faces)

        # Only display if the frame is valid
        if frame_with_faces is not None and hasattr(frame_with_faces, 'size') and frame_with_faces.size > 0:
            display_frame(frame_with_faces)
        else:
            print("Invalid frame after drawing faces. Exiting loop.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("'q' pressed. Exiting loop.")
            break
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()