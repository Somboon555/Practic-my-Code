def bmi(mass,hight):
    mass=float(input("ใส่ตัวเลข:(kg)"))
    high=float(input("ใส่ตัวเลข(m):"))
    bmi=mass/(high*high)
    print("bmi=",bmi)
    if bmi>30 :
        print("อ้วนมาก")
    elif bmi>=29.99 :
        print("อ้วน")
    elif bmi>=18.6:
        print("สมส่วน")
    else :
        print("ผอม")