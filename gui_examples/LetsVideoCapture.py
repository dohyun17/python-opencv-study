import cv2

class MyVideoCapture:
    def __init__(self, video_source=0):
        # 비디오 소스를 초기화하고 열 수 없는 경우 예외를 발생시킵니다.
        self.webcam = cv2.VideoCapture(video_source) # 0번 카메라에서 비디오를 촬영하라
        if not self.webcam.isOpened():
            raise ValueError('unable to open video source', video_source)
        
        # 비디오의 너비와 높이를 가져옵니다.
        self.width = int(self.webcam.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.webcam.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
    # 현재 프레임을 가져오는 메서드입니다.
    def get_frame(self):
        if self.webcam.isOpened():
            ret, frame = self.webcam.read()
            if ret :
                frame = cv2.flip(frame, 1)         # 프레임을 좌우로 뒤집습니다.
                return (ret, frame)
            else:
                return (ret, None)
        else:
            return (False, None)
    
    # 비디오 객체가 소멸될 때 카메라를 해제합니다.
    def __del__(self):
        if self.webcam.isOpened():
            self.webcam.release()