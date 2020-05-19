import sys
sys.setrecursionlimit(40000)
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for i in range(n)]

def inRange(a,b):
    if 0<=a and a<n and 0<=b and b<n:
        return True
    return False

direction = [(-1,0),(1,0),(0,-1),(0,1)]

board_2 = [[0 for i in range(n)] for i in range(n)]

def panda(board,row, column):
    Max = 1

    if board_2[row][column] !=0:
        return board_2[row][column]

    for i in direction:
        nextPos = (row+i[0], column+i[1])
        if inRange(nextPos[0],nextPos[1]) and board[nextPos[0]][nextPos[1]] > board[row][column]:
            if Max < panda(board, nextPos[0],nextPos[1]) + 1:
                Max = panda(board, nextPos[0],nextPos[1]) + 1
                board_2[row][column] = Max

    return Max

result = []

for i in range(n):
    for j in range(n):
        path = panda(board, i, j)
        result.append(path)

print(max(result))
