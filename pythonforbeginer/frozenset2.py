x={100:"หำ",99:"หำเเต่ใหญ่"}
"""""
for i in x:
    print(i)
"""
"""""
for i in x.values():
    print(i)
"""""
"""""
for i in x.keys():
    print(i)
"""
"""""
for i in x.items():
    print(i)
"""
for i,o in x.items():
    print("key",i,"value",o)
x.pop(100)
print(x)