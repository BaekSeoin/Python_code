import sys
from collections import deque

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline().rstrip())

def inRange(a,b):
    if (0<=a<row) and (0<=b<col):
        return True
    return False

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def fire(fireList):
    nextFireList = []
    for cur in fireList:
        for dir in direction:
            nextPos = (cur[0] + dir[0], cur[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (building[nextPos[0]][nextPos[1]] == '.'):
                building[nextPos[0]][nextPos[1]] = '*'
                nextFireList.append(nextPos)

    return nextFireList

def bfs(List):
    global minTime, time, fireList
    while List:
        a = List.popleft()
        curPos = a[0]
        curTime = a[1]

        if time == curTime:
            time += 1
            fireList = fire(fireList)

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if inRange(nextPos[0],nextPos[1]):
                if (building[nextPos[0]][nextPos[1]] == '.') and (visit[nextPos[0]][nextPos[1]] == 0):
                    visit[nextPos[0]][nextPos[1]] = 1
                    List.append((nextPos,curTime+1))
            else:
                if (curTime + 1) < minTime:
                    minTime = curTime + 1
                return

for test in range(T):
    col, row = map(int, sys.stdin.readline().rstrip().split())
    building = [[i for i in sys.stdin.readline().rstrip()] for j in range(row)]
    visit = [[0 for i in range(col)]for j in range(row)]
    fireList = []
    for i in range(row):
        for j in range(col):
            if building[i][j] == '@':
                start = (i,j)
                building[i][j] = '.'
                visit[i][j] = 1
            elif building[i][j] == '*':
                fireList.append((i,j))

    minTime = 100000000
    time = 0
    List = deque()
    List.append((start, 0))
    bfs(List)
    if minTime == 100000000:
        print("IMPOSSIBLE")
    else:
        print(minTime)
