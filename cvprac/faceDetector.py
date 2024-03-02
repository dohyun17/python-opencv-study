import cv2
import os

class FaceDetector():
    def __init__(self):
        PATH = os.getcwd()
        cur_dir = os.path.join(PATH, 'cvprac')
        cascade_filename = "cascade\\haarcascade_frontalface_default.xml"
        cascade_filepath = os.path.join(cur_dir, cascade_filename)
        print(f"cascade_filepath: {cascade_filepath}")
        self.cascade = cv2.CascadeClassifier(cascade_filepath)
    
    """
    1. 얼굴로 인식되는 모든 객체에게 네모칸을 그린다.
    """    
    def drawRect(self, image):
        faces = self.cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    """
    2. 인식된 얼굴부분에 네모칸을 그린다.
       네모칸을 (400, 500) 사이즈로 변경한다.
    """ 
    def faceRectangle(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # 프레임에서 얼굴이 인식되지 않는다면, 
        # 전달받은 프레임을 그대로 되돌려준다.
        if (len(faces) == 0):
            return img,[]

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,255),2)
            
            #얼굴로 인식된 네모칸을 roi에 담고, 사이즈를 400, 500으로 정한다.
            roi = img[y:y+h, x:x+w]
            roi = cv2.resize(roi, (400,500))
            
        (x, y, w, h) = faces[0]       
        
        return img, roi
    
    """
    3. 인식된 얼굴 중에서 첫 번째 얼굴만 회색으로 만들어서 가져온다.
    """
    def detect_face(self, img):
        # 이미지를 흑백으로 변환한다.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 얼굴찾기 알고리즘을 활용하여 얼굴들(faces)을 찾아낸다.
        faces = self.cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        
        # 얼굴이 하나도 인식되지 않으면 아무것도 되돌려주지 않는다.
        if (len(faces) == 0):
            return None, None
        
        # 얼굴이 하나만 인식되었다고 가정하고, 얼굴부분만 잘라낸다.
        (x, y, w, h) = faces[0]
        
        # 회색화한 얼굴부분만 잘라서 되돌려준다.
        return gray[y:y+w, x:x+h], faces[0]