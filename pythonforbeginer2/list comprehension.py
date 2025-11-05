name=[1,2,3]
""""
for i in range(len(name)):
    name[i]=name[i]**2
print(name)
"""
name=[i*i for i in name]
print(name)