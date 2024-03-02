import cv2
import os
PATH = os.getcwd()
cur_dir = os.path.join(PATH, 'cvprac')
image_path = os.path.join(cur_dir,'media\\sample.jpg')
image = cv2.imread(image_path)

if image is not None :
    print("이미지 읽어오기 성공!")
else:
    print("이미지 읽어오기 실패!")    
blockSize = 2 ** 2
ksize = 3*3
k = 0.04

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, blockSize, ksize, k)
image[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('Harris Corners', image)

cv2.waitKey(0) # 키 입력 대기
cv2.destroyAllWindows() # 모든 창 닫기
