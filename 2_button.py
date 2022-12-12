from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480+400+300") #가로 * 세로 + x좌표 + y좌표

btn1 = Button(root, text=" 버튼 1")
btn1.pack() #pack을 사용해야 버튼이 들어간다.

btn2 = Button(root, padx=5, pady= 10, text="버튼 2")
btn2.pack()

btn3 = Button(padx=10, pady=5, text=" 버튼 3")    #pad를 통해버튼 내부에서 여백 설정
btn3.pack()

btn4 = Button(root,width=10,height=3,text="버튼 4") #버튼의 절대값 크기 설정
btn4.pack()

btn5 = Button(root, fg = "red", bg="yellow", text="버튼 5")  #fg 글자색 ,  bg 배경색
btn5.pack()

photo = PhotoImage(file="img.png")
btn6 = Button(root,image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")

btn7 = Button(root,text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #창이 안닫히게 하는 것 
