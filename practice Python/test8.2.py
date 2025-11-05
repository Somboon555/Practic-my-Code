pos = 1

swap = {'a':{1:2,2:1},'b':{2:3,3:2},'c':{1:3,3:1}}

for ch in input().strip().lower():
    pos = swap.get(ch,{}).get(pos,pos)

print(pos)