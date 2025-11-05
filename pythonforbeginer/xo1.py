number=int(input("ป้อนตัวเลข:"))
for roand in range (number):
    for collum in range(number):
        if (roand+collum)%2==0:
            print("x",end='') # PRINT X ในเเถวเดี่ยว
        else :
             print("o",end='')

    print("") 
'''
3*3 การทำงานของ for x in range(x)ในfor x in range ที่ใช่end=" " print("")
roand=0 + collum=0 =0
...................
...................
roand=1 + collum=0 =1
...................
...................
roand=2 + collum=0 =2
=> 0 1 2 หาร 2 ลงตัวไหม => 0 1 0
   1 2 3                  1 0 1
   2 3 4                  0 1 0
'''
