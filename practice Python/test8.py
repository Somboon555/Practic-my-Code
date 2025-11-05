# setting position of ball

pos = int(input())

# swapping cup
swap = input().strip()

# loop through each swap command in the sequence
for ch in swap:
    # If the command is 'A'
    if ch.lower()== 'a': 
        #if position of ball is 1,swap 1 to 2
        if pos == 1 : pos = 2
         #position of ball is 2,swap 2 to 1
        elif pos == 2 : pos = 1
     # If the command is 'B'
    elif  ch.lower()== 'b':
        #if position of ball is 2,swap 2 to 3
        if pos == 2 : pos = 3
         #if position of ball is 3,swap 3 to 2
        elif pos == 3 : pos = 2
         # If the command is 'C'
    elif  ch.lower() == 'c':
        #if position of ball is 1,swap 1 to 3
        if pos == 1 : pos = 3
        #if position of ball is 3,swap 3 to 1
        elif pos == 3 : pos = 1

# print the final position of the ball
print(pos)