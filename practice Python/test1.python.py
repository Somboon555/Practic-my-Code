n = int(input())

number = []

for _ in range(n):
    x = int(input())
    number.append(x)

Max = max(number)
Min = min(number)

print("max =",Max)
print("min =",Min)