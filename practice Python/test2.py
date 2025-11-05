m,n = map(int,input().split())
a = []
b = []
for _ in range(m):
    x =list(map(int,input().split()))
    a.append(x)
for row in a:
    print(*row)
b = []
for _ in range(m):
    x =list(map(int,input().split()))
    b.append(x)
for row in b:
    print(*row)
result = []
for i in range(m):
    sum_result = [a[i][j]+b[i][j] for j in range(n)]
    result.append(sum_result)
for row in result:
    print(*row)