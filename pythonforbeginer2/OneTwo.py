number=[]
Number=[]
Maxnumber=[]
for Round in range(1,4):
    x=int(input("ใส่ตัวเลข :"))
    Maxnumber.append(x)
    if x % 2 == 0:
      number.append(x)
    else:
      Number.append(x)
print("เลขคี่",Number)
print("เลขคู่",number)
print("เลขเลขทั้งหมด",Maxnumber)
