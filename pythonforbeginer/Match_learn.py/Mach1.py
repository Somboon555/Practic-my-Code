number = int(input("Input number:"))
match number:
    case 1 :
        print("รับโปรโมชั่น")
    case 2 :
        print("สมัครโปรโมชั่น")
    case number if number >= 3 and number <=10:
        print("Hello")
    case _ :
        print(f"รหัส {number} ไม่ถูกต้องโปรดใส่รหัสใหม่")
    
    