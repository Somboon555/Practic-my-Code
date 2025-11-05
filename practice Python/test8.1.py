#pos = int(input())
pos = 1

for ch in input().strip().lower():
    if ch =='a': pos = 3 - pos if pos in (1,2) else pos
    elif ch == 'b': pos = 5 - pos if pos in (2,3) else pos
    elif ch == 'c' : pos =  4 - pos if pos in(1,3) else pos

print(pos)
