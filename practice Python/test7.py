x = list(map(int,input().split()))
x.sort()
     
y = input()
z=[]

for n in y:
    if n== 'A':
        z.append(x[0])
    elif n == 'C':
        z.append(x[-1])
    else:
        mid_x = len(x)//2
        z.append(x[mid_x])

print(*z)
