from tkinter import*
from tkinter import messagebox

# creat window
root = Tk()


def quitprogram():
    confirm = messagebox.askquestion("hey dude","DO you really want ot quit it")
    if confirm == "yes":
        root.destroy()
def showName():
    name = myText.get()
    myText.delete(0,END)
    if name =="":
        messagebox.showerror("faq error","hey!! where are your message????")
    else :
        messagebox.showinfo("detail","from="+name)
    
# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#9E41BB")

# entry Widget
myText = Entry(root,width=20,font=("Arial",15))
myText.pack(padx=10)


# create button
btn = Button(root,text="Save",bg="#ff0000",command=showName)
btn.pack(pady=10)


btnQuit = Button(root,text="quit",command=quitprogram)
btnQuit.pack()





root.mainloop()