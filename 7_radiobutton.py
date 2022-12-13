from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480") #가로 * 세로 

Label(root,text="메뉴를 선택하세요").pack()

burger_var = IntVar() #여기에 int형으로 값을 저장한다.

btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select() #기본값
btn_burger2 = Radiobutton(root, text="치킨버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="불고기버거", value=3, variable=burger_var)
btn_burger4 = Radiobutton(root, text="치즈버거", value=4, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_burger4.pack()

Label(root,text="음료를 선택하세요").pack()

dirnk_var = StringVar()

btn_drink1 = Radiobutton(root, text="콜라",value="콜라",variable=dirnk_var)
btn_drink1.select() #기본값
btn_drink2 = Radiobutton(root, text="사이다",value="사이다",variable=dirnk_var)

btn_drink1.pack()
btn_drink2.pack()

def btncmd() :
    print(burger_var.get()) #햄버거중 선택된 항목의 값 (value)출력
    print(dirnk_var.get()) #음료 선택된 값 출력


btn = Button(root, text="주문", command = btncmd)
btn.pack()
root.mainloop() #창이 안닫히게 하는 것 
