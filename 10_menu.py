from tkinter import *

root = Tk()
root.title("GUI 프로그램")
root.geometry("640x480") #가로 * 세로 

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="new file", command= create_new_file)
menu_file.add_command(label="new window")
menu_file.add_separator() # 구분 선
menu_file.add_command(label="Open File....")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File",menu=menu_file)

#Edit 메뉴 (빈 값)
menu.add_cascade(label="Edit")

#Language 메뉴 추가 (radio 버튼 통해서 택 1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="python")

menu_lang.add_radiobutton(label="c++")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="언어 선택",menu=menu_lang)

#View 메뉴 
menu_view = Menu(menu,tearoff= 0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View",menu=menu_view)

root.config(menu=menu)
root.mainloop() #창이 안닫히게 하는 것 
