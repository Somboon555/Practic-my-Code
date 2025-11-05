from tkinter import*

# creat window
root = Tk()
def choiceColor():
    selection = choice.get()
    print(selection)
# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#560C6D")

choice = IntVar()
Radiobutton(root,text="red",value=1,variable=choice,command=choiceColor).grid(row=0,column=0)
Radiobutton(root,text="green",value=2,variable=choice,command=choiceColor).grid(row=0,column=1)
Radiobutton(root,text="blue",value=3,variable=choice,command=choiceColor).grid(row=0,column=2)
root.mainloop()