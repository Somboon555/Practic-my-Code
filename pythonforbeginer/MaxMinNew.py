try :
    n = int(input("จำนวนของข้อมูล: "))# n คือ จำนวนรอบของข้อมูล
    if n < 0 :
        print("อย่าใส่ลบน้องพี่ฉุนล่ะ")
        n = 0 # เช็ตค่าเริ่มต้น
except ValueError:
    print("อย่ากวนส้นเท้าใส่เลขดีๆ")
    n = 0 # เช็ตค่าเริ่มต้น
max_value=None
min_value=None
#ประกาศตัวเเปร
for _ in range(n):
    try:
        a = float(input("ใส่ตัวเลข :")) #ค่าข้อมูล
        if max_value is None or a > max_value:
            max_value=a
        if min_value is None or a < min_value:
            min_value=a
    except ValueError:
        print("ใส่ตัวเลขโว้ยยยยยยยยยยยย")
if min_value is not None and max_value is not None:
    print("ค่าที่มากที่สุด",max_value)
    print("ต่าที่น้อยที่สุด",min_value)