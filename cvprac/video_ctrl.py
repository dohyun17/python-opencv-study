import cv2
import os
PATH = os.getcwd()
cur_dir = os.path.join(PATH, 'cvprac')
video_path = os.path.join(cur_dir,"media\\sample.mp4")
input_video = cv2.VideoCapture(video_path)

if input_video is not None :
    print("동영상 읽어오기 성공!")
else:
    print("동영상 읽어오기 실패!")    

videoLength = int(input_video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

output_video_path = os.path.join(cur_dir,"media\\output_sample.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 30.0
video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

from faceDetector import FaceDetector 
det = FaceDetector()
cur = 1
while cur < videoLength:
    ret, frame = input_video.read()
    det.drawRect(frame)
    
    print(f"{cur}/{videoLength}")
    cur += 1
    if not ret:
        break
    
    video_writer.write(frame)
    
input_video.release()
video_writer.release()