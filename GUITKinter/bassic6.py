from tkinter import*

# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#9E41BB")

# creat buttom
btn1 = Button(root,text="press it")
btn2 = Button(root,text="press it")
btn3 = Button(root,text="press it")

# grid layout
btn1.grid(row=0,column=0)
btn2.grid(row=1,column=0,pady=5)
btn3.grid(row=3,column=0,pady=5)
root.mainloop()
