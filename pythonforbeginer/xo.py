number=int(input("ป้อนตัวเลข:"))
for roand in range (number):
    for collum in range(number):
        if collum%2==0:
            print("x",end='') # PRINT X ในเเถวเดี่ยว
        else :
             print("o",end='')

    print("") 