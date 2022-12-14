from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")  # 가로 * 세로



menu = Menu(root)

def open():
    pass

def save():
    pass

def exit():
   root.destroy()

menu_file =Menu(menu, tearoff=0)
menu_file.add_command(label="열기",command=open)
menu_file.add_command(label="저장",command=save)
menu_file.add_command(label="끝내기",command=exit)


menu.add_cascade(label="파일",menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

text = Text(root,width=640,height=400)
text.pack()



root.config(menu=menu)
root.mainloop() #창이 안닫히게 하는 것 
