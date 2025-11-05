#เขียนเเบบprimitive
x=1
x1=2
x2=3
v=1,2,3,4,5
print(type(v))
#เขียนเเบบnon primitive
x=[1,2,3,4]
e=["hello world","OoOoh"]
all=["hello",1,-2,True,0.3]
print(type(all))
#construuor
a=list([1,2,True])
#การเข้าถึงข้อมูล
print(a[-1])
print(a[0:2])
print(a[0]+a[1])
#ชื่อตัวเเปลที่เเก้ไข [index]
print(a[1])
a[1]="หนึ่ง"
print(a[1])
print(type(a))