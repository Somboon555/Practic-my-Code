from tkinter import*

# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#560C6D")

# creat buttom
btn1=Button(root,text="press it",bg="yellow",fg="#1511f1")
btn1.pack(side="top")

btn2=Button(root,text="press it",bg="yellow",fg="#f11181")
btn2.pack(side="left")

btn3=Button(root,text="press it",bg="yellow",fg="#f111f1")
btn3.pack(side="right")

root.mainloop()


