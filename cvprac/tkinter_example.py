import tkinter as tk
window = tk.Tk()
window.title("tkinter")
window.geometry("640x400+100+100")
window.resizable(False, False)

def afterInput(event):
    output.config(text=user_input.get())
    #afterinput함수
user_input = tk.Entry(window)
user_input.bind("<Return>", afterInput)
user_input.pack()
    #pack으로 작동
output = tk.Label(window, text="coffee")
output.pack()

window.mainloop()