i=0
while i<=2 : #i นับรอบลูป
    number=float(input("ใส่ตัวเลข :")) #รับตัวเเปรใส่number
    i+=1 #เพิ่มรอบ 
    if i==1:
       min=number+1
       max=number-1 
#เพื่อกันบัค เพราะหากใช้ min = 999 เจอ number ต่ำกว่า 999 ทั้งหมด มันจะ บัค minจะเป็น 999
#เพื่อกันบัค เพราะหากใช้ max = 0 เจอ number ต่ำกว่า 0 ทั้งหมด มันจะ บัค minจะเป็น 0
    if number > max: #เปรียบเเทบ number กับ max หากมาก เเทน number ใน  max
        max=number
    if number < min : #เปรียบเเทบ number กับ min หากน้อย เเทน number ใน  min 
        min=number
print("ค่าน้อยสุด",min)
print("ค่ามากสุด",max)   
