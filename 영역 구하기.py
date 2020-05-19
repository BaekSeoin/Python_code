import sys
sys.setrecursionlimit(100000)

sys.stdin = open("input.txt","r")

row, column, k = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[-1 for i in range(column)] for j in range(row)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0 <= a <row and 0<= b < column:
        return True
    return False

def make(start, end):
    for i in range(start[1], end[1]):
        for j in range(start[0], end[0]):
            board[j][i] = 0

for i in range(k):
    a = tuple(map(int, sys.stdin.readline().rstrip().split()))
    start = (a[1],a[0])
    end = (a[3],a[2])
    make(start, end)


def dfs(List):
    global count
    current = List.pop()

    for i in direction:
        nextPos = (current[0] + i[0], current[1] + i[1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == -1:
            List.append(nextPos)
            board[nextPos[0]][nextPos[1]] = count
            count += 1
            dfs(List)

result = []

for i in range(row):
    for j in range(column):
        if board[i][j] == -1:
            count = 1
            List = []
            List.append((i,j))
            board[i][j] = count
            count += 1
            dfs(List)
            result.append(count-1)

result.sort()
print(len(result))
for k in result:
    print(k, end=' ')
