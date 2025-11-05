imformation=[1,3,2,4,5,6,7]
number=["โม้","ทุเรียน","Hero"]
#ก่อน
print(imformation)
#append เติมข้อมูล
imformation.append("โม้")
print(imformation)
#remove 
number.remove("ทุเรียน")
print(number)
#pop เอาตัวสุดท้ายออก
imformation.pop()
imformation.pop()
imformation.pop()
print(imformation)
#del ลบจากตำเเหน่งindex and clear ตัวเเปร
del imformation[0]
print(imformation)
#del imformation
#print(imformation)
#clear ลบข่อมูล
imformation.clear()
print(imformation)
Name=[1,2,"ชื่อ"]
Name.insert(2,"two")
print(Name)