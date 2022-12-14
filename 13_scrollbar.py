from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480")  # 가로 * 세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right",fill="y")
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand= scrollbar.set) #set이 없으면 스크롤을 내려도 다시 올라옴

for i in range(1,32): #1~32 일
    listbox.insert(END,str(i) + "일") #1일, 2일 ....
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)
root.mainloop() #창이 안닫히게 하는 것 
