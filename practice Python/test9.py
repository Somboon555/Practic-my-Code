number = [int(input()) for _ in range(10)]

remainders  = []
for i in number:
    s = i % 42
    remainders.append(s)

unique_remainders =set(remainders)

print(len(unique_remainders))
