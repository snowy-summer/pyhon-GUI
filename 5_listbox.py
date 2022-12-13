from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480") #가로 * 세로 

listbox = Listbox(root, selectmode="extended", height= 0)  # extended 여러가지 선택이 가능하다. height 는 리스트의 크기?    3이면 3개의 리스트만 보여준다.
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd() :
    # 삭제
    #listbox.delete(0) # 맨 앞의 항목을 삭제
   
   #갯수 확인
   #print("리스트에는 ", listbox.size(), "개가 있어요")

    #항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ",listbox.get(0,2))

    #선택된 항목 확인 (위치로 변환 ex: 1,2,3)
    print(" 선택된 항목 : ", listbox.curselection())
btn = Button(root, text="클릭", command = btncmd)
btn.pack()
root.mainloop() #창이 안닫히게 하는 것 
