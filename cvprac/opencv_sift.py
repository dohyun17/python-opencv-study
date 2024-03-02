import cv2
import os
PATH = os.getcwd()
cur_dir = os.path.join(PATH, 'cvprac')
image_path = os.path.join(cur_dir,'media\\sample.jpg')
image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# SIFT 객체 생성
sift = cv2.SIFT_create()

# 특징점 검출 및 기술자 계산
keypoints, descriptors = sift.detectAndCompute(gray, None)

# 특징점 그리기
image_with_keypoints = cv2.drawKeypoints(image, keypoints, None)

# 결과 이미지 출력
cv2.imshow('SIFT Features', image_with_keypoints)

cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기
