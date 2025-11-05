from tkinter import*

# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#9E41BB")

# entry Widget
myText = Entry(root,width=20,font=("Arial",15))
myText.pack(padx=10)
myText.insert(0,"input your data")

# create button
btn = Button(root,text="Save",bg="#ff0000")
btn.pack(pady=10)
root.mainloop()