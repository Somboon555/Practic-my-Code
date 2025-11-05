word = 'AB'
peter = ["..#..", ".#.#.", "#.X.#", ".#.#.", "..#.."]
wendy = ["..*..", ".*.*.", "*.X.*", ".*.*.", "..*.."]  
    
result = [""]*5

for i,ch in enumerate(word,start = 1):
    frame =  wendy if i % 3 == 0 else peter
    frame = [row.replace('X',ch) for row in frame]

    if i == 1:
            for r in range(5):
                result[r] = frame[r]
    
    else:
        for r in range(5):
            left_last = result[r][-1]
            right_first = frame[r][0]
            
            if (left_last == '#' and right_first == '*') or \
            (left_last == '*' and right_first == '#'):
                overlap = '*'
            else:
                overlap = right_first

            result[r] = result[r][:-1] + overlap + frame[r][1:]
for row in result:
    print(row) 