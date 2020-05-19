import sys

sys.stdin = open("input.txt", "r")

R,C = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(R)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<R and 0<=b<C:
        return True
    return False
ans = 1
for i in range(R):
    for j in range(C):
        if board[i][j] == 'W':
            for dir in direction:
                nextPos = (i+dir[0],j+dir[1])
                if inRange(nextPos[0],nextPos[1]):
                    if board[nextPos[0]][nextPos[1]] == '.':
                        board[nextPos[0]][nextPos[1]] = 'D'
                    elif board[nextPos[0]][nextPos[1]] == 'W' or board[nextPos[0]][nextPos[1]] == 'D':
                        continue
                    elif board[nextPos[0]][nextPos[1]] == 'S':
                        ans = 0
                        break
        if ans == 0:
            break
    if ans == 0:
        break
if ans == 1:
    print(ans)
    for i in range(R):
        for j in range(C):
            print(board[i][j],end='')
        print()
else:
    print(ans)

