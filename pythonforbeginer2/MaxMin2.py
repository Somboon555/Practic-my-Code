number=[]
for Round in range(1,4):
    x=int(input("ใส่ตัวเลข :"))
    number.append(x)
number.sort()
print("น้อนไปมาก:",number)
number.reverse()
print("มากไปน้อย:",number)
print("min :",min(number))
print("max :",max(number))
print("sum:",sum(number))