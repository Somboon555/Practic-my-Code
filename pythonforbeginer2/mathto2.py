fruit=["มะม่วง","ส้ม","มะละกอ"]
price=[20,50,30]

for x,y in zip(fruit,price[::-1]):
    print(x,"ราคา =",y)