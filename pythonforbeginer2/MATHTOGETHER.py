bly=["hi","hello","goodbly"]
name=["สมบูรณ์","บูน"]
'''
for x in bly:
     for y in name:
        result.append(x+y)
print( result)
'''
result=[x+y for x in bly for y in name]
print(result)
