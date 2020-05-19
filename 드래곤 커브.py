import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

direction = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
direction_change = {0:1,1:2,2:3,3:0}

board = [[0 for i in range(101)] for j in range(101)]

def make(dragon_curve):
    for curPos in dragon_curve:
        try:
            board[curPos[0]][curPos[1]] = 1
        except:
            continue

for i in range(N):
    col,row,dir,generation = tuple(map(int,sys.stdin.readline().rstrip().split()))
    next_dir = direction[dir]
    nextPos = (row+next_dir[0],col+next_dir[1])
    dragon_curve = [(row,col),nextPos]
    future_direction = [dir]

    for gen in range(generation):
        index = len(dragon_curve) -1
        Len = len(dragon_curve)
        current = dragon_curve[index]
        nextPoint = current
        new_index = 2 ** gen - 1
        for add in range(Len-1):
            new_dir = direction_change[future_direction[new_index]]
            next_dir = direction[new_dir]
            nextPoint = (nextPoint[0] + next_dir[0], nextPoint[1] + next_dir[1])
            dragon_curve.append(nextPoint)
            future_direction.append(new_dir)
            index -=1
            new_index-=1

    make(dragon_curve)

count = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            if board[i+1][j] == 1 and board[i][j+1] == 1 and board[i+1][j+1]==1:
                count +=1
print(count)
