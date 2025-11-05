number=int(input("ป้อนตัวเลข:"))
for roand in range (number):
    for collum in range(number):
        if collum==0 or collum==number-1 or roand==0 or roand==number-1 :
            print("x",end='') # PRINT X ในเเถวเดี่ยว
        else :
             print(" ",end='')
    print(" ") 