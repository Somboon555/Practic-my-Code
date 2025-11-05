from tkinter import *
from tkinter import messagebox
# Somboon is very cute and creat this project 
# funtion
# close program
def quitprogram():
    confirm = messagebox.askquestion("hey dude","DO you really want to quit it")
    if confirm == "yes":
        root.destroy()
# addItem
def addItem():
    data  = inputEntry.get()
    listbox.insert(END,data)
    inputEntry.delete(0,END)
# removeItem
def removeItem():
    listbox.delete(ANCHOR)

# Clear List
def clearList():
    listbox.delete(0,END)
# root window
root = Tk()
root.title("Checklist Application")
root.iconbitmap("icon/check.ico")
root.geometry("400x500+500+100")
root.resizable(0,0)

# settings
font_style = ("Arial", 15)
color = "#04f1aa"
root.config(bg=color)

# design frames
input_frame = Frame(root, bg=color)
output_frame = Frame(root, bg=color)
button_frame = Frame(root, bg=color)

input_frame.pack(pady=10)
output_frame.pack(pady=10)
button_frame.pack(pady=10)

# input entry and button
inputEntry = Entry(input_frame, width=25, font=font_style)
btnAdd = Button(input_frame, text="Add List", font=font_style,command=addItem)

inputEntry.grid(row=0, column=0, padx=5)
btnAdd.grid(row=0, column=1, padx=5)

# outout
listbox = Listbox(output_frame,width=35,height=12,font=font_style)
listbox.grid(row=0,column=0,padx=5,pady=5)

# button widget
btnRemove  = Button(button_frame,text="delet list",font=font_style,command=removeItem)
btnClear = Button(button_frame,text="clear list",font=font_style,command=clearList)
btmQuit = Button(button_frame,text="close promgram",font=font_style,command=quitprogram)

    

btnRemove.grid(row=0,column=0,padx=5,pady=5)
btnClear.grid(row=0,column=1,padx=5,pady=5)
btmQuit.grid(row=0,column=2,padx=5,pady=5)

root.mainloop()

