from tkinter import *
from menu import *
root=Tk()#สร้างหน้าต่างnote
root.title("My_note")#โปรเเกรมชื่อmy_note

#สร้างข้อความ
My_title=Label(text="บันทึกความทรงจำ",fg="black",bg="white",font=100).pack(pady=10)

#สร้างfunctionเมื่อกดปุ่ม
def showmessage():
    message=txt.get()
    print(message)
def show_report():
    #หน้าจอ2
    report=Toplevel()#สร้างหน้าต่างreport
    massage=txt.get()
    report.title("สมุด")
    report.geometry("500x500")
    My_massage=Label(report,text=massage,fg="blue",bg="white",font=100)
    My_massage.pack(pady=10)


#กล่องข้อความ
txt=StringVar()
my_txt=Entry(root,textvariable=txt)
my_txt.pack(pady=109)
   
#ใส่ป่มในหน้าต่าง
btn1=Button(root,text="บันทึก",command=showmessage).pack()
btn2=Button(root,text="เปิดบันทึก",command=show_report).pack()


#หน้าต่าง1
root.geometry("500x400+500+100")
root.mainloop()