from tkinter import*
from tkinter.filedialog import*
# creat window
root = Tk()

# Edit window
root.title("MyProject")
root.iconbitmap("icons/logo.ico")
root.geometry("400x400+100+200")
root.resizable(1,1)
root.config(bg="#560C6D")

def selecFile():
    file = askopenfilename(title="openflie",initialdir="./",filetypes=(("text File","*txt"),("Allfile","*")))
    with open(file,"r",encoding="utf-8") as f:
            Label(root,text=f.read()).pack()
btm1 = Button(root,text="choice your file",command=selecFile).pack()




root.mainloop()