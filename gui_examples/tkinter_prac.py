import tkinter                          # tkinter 모듈을 임포트합니다.
window = tkinter.Tk()                   # Tk 객체를 생성하여 윈도우 창을 만듭니다.

window.title("letscoding")
window.geometry("640x400+100+100")
window.resizable(False, False)

count = 0                               # 카운트 변수를 초기화합니다.
# 버튼 클릭 시 호출될 함수를 정의합니다.
def countUp():
    global count                         # 전역 변수 count를 사용합니다.
    count += 1                           # count를 1 증가시킵니다.
    label.config(text=str(count))        # Label에 현재 count 값을 표시합니다.
    
# Label 위젯을 생성하고 초기 텍스트를 "0"으로 설정합니다.
label = tkinter.Label(window, text="0")
label.pack()                           # 화면에 Label을 배치합니다.

# Button 위젯을 생성하고 속성을 설정합니다.
button = tkinter.Button(window, 
                        text="up",               # 버튼에 표시될 텍스트입니다.
                        overrelief="solid",      # 버튼이 눌렸을 때 3D 효과를 줍니다.
                        width=15,                # 버튼의 폭을 설정합니다.
                        command=countUp,         # 버튼 클릭 시 실행할 함수를 지정합니다.
                        repeatdelay=1000,        # 버튼을 길게 눌렀을 때 반복 시작 딜레이를 설정합니다.
                        repeatinterval=100)      # 버튼을 길게 눌렀을 때 반복 간격을 설정합니다.
button.pack()

def countDown():
    global count                         # 전역 변수 count를 사용합니다.
    count += -1                                  # count를 1 감소시킵니다.
    label.config(text=str(count))        # Label에 현재 count 값을 표시합니다

downbutton = tkinter.Button(window, 
                        text="down",             # 버튼에 표시될 텍스트입니다.
                        overrelief="solid",      # 버튼이 눌렸을 때 3D 효과를 줍니다.
                        width=15,                # 버튼의 폭을 설정합니다.
                        command=countDown,       # 버튼 클릭 시 실행할 함수를 지정합니다.
                        repeatdelay=1000,        # 버튼을 길게 눌렀을 때 반복 시작 딜레이를 설정합니다.
                        repeatinterval=100)      # 버튼을 길게 눌렀을 때 반복 간격을 설정합니다.
downbutton['state'] =tkinter.DISABLED
downbutton.pack()
button.pack()


window.mainloop()


