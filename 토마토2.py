import sys
from collections import deque

sys.stdin = open("input.txt","r")

column, row, h = tuple(map(int, sys.stdin.readline().rstrip().split()))

box = [[[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(row)] for k in range(h)]

direction = [(0,-1,0),(0,0,1),(0,1,0),(0,0,-1),(1,0,0),(-1,0,0)]
visit = [[[-1 for i in range(column)] for j in range(row)] for k in range(h)]

def inRange(a,b,c):
    if 0<= a < h and 0<=b<row and 0<=c <column:
        return True
    return False

List = deque()
day = 0

for i in range(h):
    for j in range(row):
        for k in range(column):
            if box[i][j][k] == 1:
                List.append(((i,j,k),day))
                visit[i][j][k] = day
            elif box[i][j][k] == -1:
                visit[i][j][k] = -2

Max_day = 0
def bfs(List):
    global Max_day
    if len(List) == row * column * h:
        return True
    while List:
        a = List.popleft()
        current = a[0]
        day = a[1]

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1], current[2] + i[2])
            if inRange(nextPos[0], nextPos[1], nextPos[2]) and box[nextPos[0]][nextPos[1]][nextPos[2]] == 0 and visit[nextPos[0]][nextPos[1]][nextPos[2]] == -1:
                List.append((nextPos, day+1))
                visit[nextPos[0]][nextPos[1]][nextPos[2]] = day+1
                if day + 1 > Max_day:
                    Max_day = day +1
    return False

result = bfs(List)

if result == True:
    print(0)
else:
    for i in range(h):
        for j in range(row):
            for k in range(column):
                if visit[i][j][k] == -1:
                    print(-1)
                    break
            if visit[i][j][k] == -1:
                break
        if visit[i][j][k] == -1:
            break

