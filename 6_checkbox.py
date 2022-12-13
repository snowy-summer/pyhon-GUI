from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480") #가로 * 세로 
chkvar = IntVar() #chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="오늘 하루 보지 않기",variable=chkvar)
chkbox.select() #자동 선택 처리  기본으로 체크 표시가 되어 있음
chkbox.deselect() # 선택 해제 처리
chkbox.pack()


chkvar2 = IntVar()
chkbox2 = Checkbutton(root,text="일주일동안 보지 않기", variable= chkvar2)
chkbox2.pack()

def btncmd() :
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크     이 출력 된다.
    print(chkvar2.get())


btn = Button(root, text="클릭", command = btncmd)
btn.pack()
root.mainloop() #창이 안닫히게 하는 것 
