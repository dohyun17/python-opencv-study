import tkinter as tk                # tkinter 모듈을 tk로 임포트합니다.
from math import *                  # math 모듈에서 모든 함수를 가져옵니다.

window = tk.Tk()                    # Tk 클래스의 인스턴스를 생성하여 윈도우 창을 만듭니다.
window.title("letscoding")          # 윈도우 창의 제목을 "letscoding"으로 설정합니다.
window.geometry("640x400+100+100")  # 윈도우 창의 크기와 위치를 설정합니다. (너비x높이+X위치+Y위치)
window.resizable(False, False)      # 윈도우 창의 크기를 조절할 수 없도록 설정합니다.

def calc(event):                    # calc 함수를 정의합니다. 이 함수는 이벤트가 발생할 때 실행됩니다.
    label.config(text= f"결과={str(eval(entry.get()))}")    
                                    # entry에서 입력된 텍스트를 가져와서 eval() 함수로 계산한 뒤, label에 표시합니다.

entry = tk.Entry(window)            # Entry 위젯을 생성하여 윈도우에 추가합니다. (사용자로부터 입력을 받는 상자)
entry.bind('<Return>', calc)        # Enter 키가 눌리면 calc 함수가 호출되도록 바인딩합니다.
entry.pack()                        # Entry 위젯을 화면에 표시합니다.

label = tk.Label(window)           # Label 위젯을 생성하여 윈도우에 추가합니다. (텍스트 또는 이미지 표시)
label.pack()                        # Label 위젯을 화면에 표시합니다.

window.mainloop()                   # 윈도우 창을 실행하고, 사용자의 이벤트를 대기합니다.
