from tkinter import*

# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#9E41BB")

# creat frame
fr = Frame(root,bg="#23b423")
fr1 = LabelFrame(root,text="Frame title")

# display frame
fr.pack(fill=BOTH,expand=True)
Button(fr,text="love you girl").grid(row=0,column=0)
Button(fr,text="love you girl").grid(row=1,column=0)
Button(fr,text="love you girl").grid(row=2,column=0)

fr1.pack(fill=BOTH,expand=True)
Button(fr1,text="love you girl").grid(row=0,column=0)
Button(fr1,text="love you girl").grid(row=1,column=0)
Button(fr1,text="love you girl").grid(row=2,column=0)
root.mainloop()