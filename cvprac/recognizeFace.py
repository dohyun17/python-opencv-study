import cv2
from faceDetector import FaceDetector
from trainImgs import TrainImgs
import numpy as np

cap = cv2.VideoCapture(0)
detector = FaceDetector()
trainImg = TrainImgs()
##################################################
###    머신러닝이 사진들을 읽고 학습하는 구간     ###
faces, labels = trainImg.prepare_training_data()
model = cv2.face.LBPHFaceRecognizer_create()
model.train(faces, np.array(labels))
##################################################
while True:    
    ret, frame = cap.read()    
    image, unknownFace = detector.faceRectangle(frame)
    
    try:
        # grayScaleFace = cv2.cvtColor(inputFace, cv2.COLOR_BGR2GRAY)
        grayScaleFace, rect = detector.detect_face(frame)
        result = model.predict(grayScaleFace)
        
        if result[1] < 500:            
            confidence = int(100 * (1-(result[1])/300))
            display_string = str(confidence)+'% Confidence it is ' + names(result[0])
        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 120, 255), 2)
        if confidence > 70:
            
            cv2.putText(image, "Hi Member!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Face Cropper", image)
        else :
            
            cv2.putText(image, "Not Member!", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("Face Cropper", image)
    except :
        
        #print(RuntimeError)
        cv2.putText(image, "Face Not Found!", (400, 500), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Face Cropper", image)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()