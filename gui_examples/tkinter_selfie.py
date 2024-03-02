import tkinter as tk                      # tkinter 모듈을 tk로 임포트합니다.
import cv2                               # OpenCV 모듈을 임포트합니다.
import PIL.Image, PIL.ImageTk            # PIL 모듈에서 이미지 처리를 위한 모듈들을 임포트합니다.

from LetsVideoCapture import MyVideoCapture
            
class App:
    def __init__(self, window, window_title, video_source=0):
        self.num = 1
        # 윈도우와 윈도우 제목, 비디오 소스를 초기화합니다.
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.is_recording = False           # 녹화 상태를 나타내는 변수를 초기화합니다.
        
        # 비디오 캡쳐 객체를 초기화합니다.
        self.my_video = MyVideoCapture(self.video_source)
        
        # 캔버스를 생성하고 윈도우에 배치합니다.
        self.canvas = tk.Canvas(window, width=self.my_video.width, height=self.my_video.height)
        self.canvas.pack()
        
        # 녹화 버튼을 생성하고 윈도우에 배치합니다.
        self.btn_snapshot = tk.Button(window, text="촬영", width=20, height=5, command=self.capture)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
                      
        # 프레임 업데이트 함수를 호출하여 비디오를 업데이트합니다.
        self.update()
        
        # 윈도우 이벤트 루프를 실행합니다.
        self.window.mainloop()
        
    # 촬영을 하는 메서드입니다.
    def capture(self):
        ret, frame = self.my_video.get_frame()     # 비디오 프레임을 가져옵니다.
        frame = cv2.flip(frame, 1)                 # 프레임을 좌우로 뒤집습니다.
        cv2.imwrite(f'img{self.num}.jpg', frame)   # 프레임을 이미지 파일로 저장합니다.
        self.num+=1
        
    # 프레임을 업데이트하는 메서드입니다.
    def update(self):
        # 프레임 속도와 프레임 간의 딜레이를 설정합니다.
        self.fps = self.my_video.webcam.get(cv2.CAP_PROP_FPS)
        self.delay = round(1000.0/self.fps)
        ret, frame = self.my_video.get_frame()          # 비디오 프레임을 가져옵니다.
        
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(
                    image=PIL.Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                )# OpenCV 배열을 PIL 이미지로 변환하여 캔버스에 표시할 수 있는 형식으로 변환합니다.
                
            self.canvas.create_image(0,0,image=self.photo, anchor=tk.NW) # 캔버스에 이미지를 표시합니다.
        # 프레임 업데이트 함수를 재귀적으로 호출하여 프레임을 지속적으로 업데이트합니다.
        self.window.after(self.delay, self.update)
    
    # 소멸자를 정의하여 객체가 소멸될 때 녹화를 종료합니다.
    def __del__(self):
        if self.is_recording:
            self.my_video.video.release()            
        
# App 클래스의 인스턴스를 생성하고 윈도우를 실행합니다.
App(tk.Tk(), 'Tkinter and OpenCV')
