from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("menu")

#functoin new window
def newwindow():
    window=Toplevel(root)
    window.geometry("500x500")
    window.title("New_Fill")
    window.mainloop()

#aboutProgram
def aboutprogram():
    tkinter.messagebox.showinfo("เเจ้งเตือนผู้ใช้","สมบูรณ์ชอบHee")

#exitProgram
def exitprogram():
    comfire=tkinter.messagebox.askquestion("ยืนยัน","ต้องการปิดหรือไม่")
    if comfire == "yes":
        root.destroy()

#creat menu
my_menu=Menu(root)
root.config(menu=my_menu)

#creat menuitem
menuitem1=Menu(root)
menuitem1.add_command(label="Graphic")
menuitem1.add_command(label="Option")
menuitem1.add_command(label="Vidio")

menuitem2=Menu(root)
menuitem2.add_command(label="NewWindow",command=newwindow)
menuitem2.add_command(label="Exit",command=exitprogram)
menuitem2.add_command(label="about",command=aboutprogram)
#main menu
my_menu.add_cascade(label="file",menu=menuitem2)
my_menu.add_cascade(label="setting",menu=menuitem1)


root.geometry("500x500+100+100")
root.mainloop()