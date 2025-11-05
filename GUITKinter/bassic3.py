from tkinter import*

# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#560C6D")

# labal
label1 = Label(root,text="Hello would",font=("Arial",30,"bold"),bg="#107daf",fg="white")
label1.pack()#new edit label

label2 = Label(root,text="I am a cute boy",font=("Arial",30,"bold"),bg="#10af4d",fg="white")
label2.pack(padx=10,pady=10,ipady="10")

label3 = Label(root,text="Yes I want to have some girl",font=("Arial",30,"bold"),bg="#afac10",fg="white")
label3.pack(fill="x",expand=True)
root.mainloop()

