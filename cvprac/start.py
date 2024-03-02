import cv2
import os

PATH = os.getcwd()
cur_dir = os.path.join(PATH, 'opencv_prac')
image_path = os.path.join(cur_dir,'sample.jpg')
print(image_path)
image = cv2.imread(image_path)
if image is not None:
    print("성공적")
else:
    print("실패")

#image[300:500, 650:700] = [0,0,255]

cv2.putText(img=image,
            text='hello,opencv',  
            org=(50,50),
            fontFace= cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(255,255,255),
            thickness=2)
#blurred_image = cv2.blur(image, (0,0))
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("no brand",gray_image)
cv2.imwrite(os.path.join(cur_dir ,"new_sample.jpg"), image)
#cv2.imwrite("new_sample.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()                        