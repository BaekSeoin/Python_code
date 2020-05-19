import sys
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())
board = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]

start = []
end = []

move = {'U':(-1,0),'D':(1,0),'L':(0,-1),'R':(0,1),'T':{0:((-1,0),(1,0)),1:((0,-1),(0,1))}}

def inRange(a,b):
    if (0<=a<N) and (0<=b<N):
        return True
    return False

def rectangle_check(a,b):

    check = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

    stop = False
    for i,j in check:
        pos = (a+i,b+j)
        if (inRange(pos[0],pos[1])) and (board[pos[0]][pos[1]] == 0):
            stop = False
        else:
            stop = True
        if stop:
            return False
    return True


for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            start.append((i,j))
            board[i][j] = 0
        elif board[i][j] == 'E':
            end.append((i,j))
            board[i][j] = 0
        board[i][j] = int(board[i][j])

visit = [[[0 for i in range(N)] for j in range(N)] for k in range(2)]


def bfs(List):
    global minTime

    while List:

        x = List.popleft()
        curPos = x[0]
        curTime = x[1]
        curDir = x[2]
        curPos1 = curPos[0]
        curPos2 = curPos[1]
        curPos3 = curPos[2]

        if curPos2 == end[1]:
            if ((curPos1 == end[0]) and (curPos3 == end[2])) or ((curPos1 == end[2]) and (curPos3 == end[1])):
                minTime = curTime
                break

        for key,dir in move.items():
            if key != 'T':
                nextPos1 = (curPos1[0] + dir[0],curPos1[1]+dir[1])
                nextPos2 = (curPos2[0] + dir[0], curPos2[1] + dir[1])
                nextPos3 = (curPos3[0] + dir[0], curPos3[1] + dir[1])

                if (inRange(nextPos1[0], nextPos1[1])) and (inRange(nextPos2[0], nextPos2[1])) and (inRange(nextPos3[0], nextPos3[1])):
                    if (board[nextPos1[0]][nextPos1[1]] == 0) and (board[nextPos2[0]][nextPos2[1]] == 0) and (
                            board[nextPos3[0]][nextPos3[1]] == 0):
                        if visit[curDir][nextPos2[0]][nextPos2[1]] == 0:
                            nextPos = (nextPos1,nextPos2,nextPos3)
                            List.append((nextPos,curTime+1,curDir))
                            visit[curDir][nextPos2[0]][nextPos2[1]] = 1
            elif key == 'T':
                if curDir == 0:
                    nextDir = 1
                else:
                    nextDir = 0
                dir = dir[curDir]
                dir1 = dir[0]
                dir2 = dir[1]

                nextPos1 = (curPos2[0] + dir1[0],curPos2[1] + dir1[1])
                nextPos2 = (curPos2[0], curPos2[1])
                nextPos3 = (curPos2[0] + dir2[0], curPos2[1] + dir2[1])

                if rectangle_check(nextPos2[0],nextPos2[1]):
                    if visit[nextDir][nextPos2[0]][nextPos2[1]] == 0:
                        nextPos = (nextPos1,nextPos2,nextPos3)
                        List.append((nextPos,curTime+1,nextDir))
                        visit[nextDir][nextPos2[0]][nextPos2[1]] = 1

List = deque()

a = (start[1][0] - start[0][0], start[1][1] - start[0][1])
if a == (1,0):
    curDir = 1
else:
    curDir = 0

List.append((start,0,curDir))
minTime = -1
visit[curDir][start[1][0]][start[1][1]] = 1
bfs(List)

if minTime == -1:
    print(0)
else:
    print(minTime)