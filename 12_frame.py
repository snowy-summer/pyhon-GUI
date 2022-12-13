from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480")  # 가로 * 세로

Label(root,text="메뉴를 선택해 주세요").pack(side="top")

Button(root,text="주문하기").pack(side="bottom")

#메뉴 프레임
frame_buger = Frame(root,relief="solid", bd=1)
frame_buger.pack(side = "left",fill="both", expand =True)

Button(frame_buger, text="햄버거").pack()
Button(frame_buger, text="치즈버거").pack()
Button(frame_buger, text="치킨버거").pack()

# 음료 프레임
frame_drink = LabelFrame(root,text="음료")
frame_drink.pack(side="right",fill="both", expand =True)
Button(frame_drink,text="콜라").pack()
Button(frame_drink,text="사이다").pack()

root.mainloop() #창이 안닫히게 하는 것 
