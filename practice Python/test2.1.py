#input row collum
m,n = map(int,input().split())
#input value in matrix A B
A = [list(map(int,input().split())) for _ in range(m)]
B = [list(map(int,input().split())) for _ in range(m)]
#output sum_matrix
result = []
for i in range(m):
    sum_result = [A[i][j]+B[i][j] for j in range(n)]
    result.append(sum_result)
for row in result:
    print(*row)