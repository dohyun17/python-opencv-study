import cv2
from faceDetector import FaceDetector

cap = cv2.VideoCapture(0)
detector = FaceDetector()

while True:    
    ret, frame = cap.read()    
    image, unknownFace = detector.faceRectangle(frame)
    cv2.imshow('webcam', image)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()