import cv2
import os
PATH = os.getcwd()
cur_dir = os.path.join(PATH, 'cvprac')
image_path = os.path.join(cur_dir,'media\\sample.jpg')
image = cv2.imread(image_path)

cascade_filename = "cascade\\haarcascade_eye.xml"
cascade_filepath = os.path.join(cur_dir, cascade_filename)
cascade = cv2.CascadeClassifier(cascade_filepath)

if image is not None :
    print("이미지 읽어오기 성공!")
else:
    print("이미지 읽어오기 실패!")    
eyes = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 검출된 눈에 경계 상자 그리기
for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 결과 이미지 출력
cv2.imshow('Eyes Detection', image)

cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기
