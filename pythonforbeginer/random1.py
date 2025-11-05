import random
Random=random.randrange(1,10)
while True :
    myrandom=int(input("ป้อนค่า:"))
    print("ค่าที่ถูกต้อง",Random)
    if myrandom==Random:
        print("ถูก")
    if myrandom!=Random:
        print("ไม่ถูก")
        continue
