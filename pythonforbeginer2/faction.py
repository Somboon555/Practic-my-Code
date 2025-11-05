def randomnumber():
    import random
    number_gak="" #กำหนดค่าเริ่มต้น
    i=0 #นับจำนวนที่ผิด
    random_number=random.randint(1,10)
    
    while True:
        x = int(input("สุ่มเลข1-10 :"))
        if x == random_number:
            print("เทพจัดตอบได้ไงวะ")
            break
        else: 
            number_gak+="กาก"#ใส่คำว่า"กาก"ทุกครั้งที่ผิด
            print(number_gak)
    print("เฉลย",random_number)
randomnumber()
'''''
    ใช้สำหรับสุ่มตัวเลขจำนวนเต็มในช่วงที่กำหนดตั้งแต่ 
    a ถึง b รวมปลายทั้งสองด้าน (คือ a และ b ก็มีโอกาสถูกสุ่มออกมา)
    '''''
'''''
    PEP 8 เป็นแนวทางการเขียนโค้ดสำหรับ Python ซึ่งช่วยให้โค้ดอ่านง่ายและมีมาตรฐานเดียวกัน 9
    โดยหนึ่งในหลักการของ PEP 8 คือการตั้งชื่อ ตัวแปร ควรใช้ ตัวอักษรพิมพ์เล็ก
     และอาจใช้ขีดล่าง _ เพื่อแยกคำ เช่น my_variable หรือ random_number
     '''''
