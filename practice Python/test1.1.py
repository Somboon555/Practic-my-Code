#set variable value
row = int(input())
collum = int(input())

matrix_1 = []
matrix_2 = []
result = []

#add value in matrix_1
print("value in matrix_1")
for i in range(row):
    value = []
    for j in range(collum):
        x = int(input(f'nummber{i}{j}:'))
        value.append(x)
    print('')
    matrix_1.append(value)

#add value in matrix_2
print("value in matrix_2")
for i in range(row):
    value = []
    for j in range(collum):
        x = int(input(f'nummber{i}{j}:'))
        value.append(x)
    print('')
    matrix_2.append(value)

#add the two matrix
print("result")
for i in range(row):
    sum_matrix = []
    for j in range(collum):
        sum_matrix= matrix_1[i][j] + matrix_2[i][j]
        result.append(sum_matrix)
print(result)

#output matrix_1
print("output matrix_1")
for row in matrix_1:
    for val in row:
        print(val, end='')
    print('')

#output matrix_2
print("output matrix_2")
for row in matrix_2:
    for val in row:
        print(val, end='')
    print('')

