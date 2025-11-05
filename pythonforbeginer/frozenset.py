x={100:"หำ",99:"หำเเต่ใหญ่"}
print(x[100])
y=dict({99:"หำ",100:"หำเเต่ใหญ่"})
print(y[100])
print(y.get(100))
#update
y.update({0:"som"})
print(y)