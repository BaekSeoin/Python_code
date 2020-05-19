import sys
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt","r")

t = int(sys.stdin.readline().rstrip())

direction = [(-1,0),(0,1),(1,0),(0,-1)]


def inRange(a, b, row, column):
    if 0 <= a and a < row and 0 <= b and b < column:
        return True
    return False

def dfs(a,b,count):
    discovered[a][b] = count

    for i in direction:
        nextPos = (a + i[0], b + i[1])
        if inRange(nextPos[0],nextPos[1], row, column) and discovered[nextPos[0]][nextPos[1]] == 0 and board[nextPos[0]][nextPos[1]] == 1:
            dfs(nextPos[0], nextPos[1], count)

for i in range(t):
    column, row, k = tuple(map(int, sys.stdin.readline().rstrip().split()))

    board = [[0 for i in range(column)] for j in range(row)]
    discovered = [[0 for i in range(column)] for j in range(row)]

    for q in range(k):
        a = tuple(map(int, sys.stdin.readline().rstrip().split()))
        board[a[1]][a[0]] = 1

    count = 0
    for u in range(row):
        for r in range(column):
            if board[u][r] == 1 and discovered[u][r] == 0:
                count += 1
                dfs(u,r,count)

    print(count)