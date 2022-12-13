from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480") #가로 * 세로 

txt = Text(root, width= 30, height=5)  # 텍스트가 입력 가능한 창이 생긴다.
txt.pack()

txt.insert(END,"글자를 입력하세요")    # 사람들에게 어떤 창인지 알려 주는 것이 가능하다.

e = Entry(root, width= 30)  # 한줄의 입력을 받을때 사용한다. 
e.pack()
e.insert(0,"한 줄만 입력하세요")

def btncmd() :
    #내용 출력
    print(txt.get("1.0",END))  # 처음 부터 끝까지의 텍스트를 가지고 온다.   1은 첫 째줄을 의미하고 0은 0번째의 단어 모음(띄어쓰기 기준)
    print(e.get())

    #내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)

btn = Button(root, text="클릭", command = btncmd)
btn.pack()
root.mainloop() #창이 안닫히게 하는 것 
