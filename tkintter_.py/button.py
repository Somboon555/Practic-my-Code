from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root=Tk()
root.title("color")

def buttoncolor():
    color=askcolor()
    mylable=Label(text="hello_wold",bg=color[1]).pack()
def selecfire():
    openfire=askopenfilename()
    if openfire :
        with open(openfire,encoding="utf-8") as file:
            my_lable=Label(text=file.read()).pack()
btn1=Button(text="เลือกสี",command= buttoncolor).pack()
btn2=Button(text="เลือกไฟล์",command= selecfire).pack()
root.geometry("600x500+50+100")
root.mainloop()