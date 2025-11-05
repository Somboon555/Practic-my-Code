from tkinter import *
from PIL import ImageTk, Image

# Create window
root = Tk()
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1, 1)
root.config(bg="#560C6D")


img = ImageTk.PhotoImage(Image.open("icons/1bffa63a24a85158 - Copy.jpg"))
label = Label(root,image=img).pack()
root.mainloop()
