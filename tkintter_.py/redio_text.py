from tkinter import *
import tkinter.messagebox
root=Tk()
root.title("radio_button")
root.geometry("500x500")

language = IntVar()
Radiobutton(text="python",variable=language,value=1).grid(row=1,column=1)
Radiobutton(text="java",variable=language,value=2).grid(row=2,column=1)
Radiobutton(text="c++",variable=language,value=3).grid(row=3,column=1)

root.mainloop()