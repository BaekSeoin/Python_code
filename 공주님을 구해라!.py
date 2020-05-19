import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M,T = map(int, sys.stdin.readline().rstrip().split())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

visit = [[[0 for i in range(M)] for j in range(N)] for k in range(2)]

def bfs(List):
    global T

    while List:
        x = List.popleft()
        curPos = x[0]
        curTime = x[1]
        have = x[2]

        if curPos == (N-1,M-1):
            break

        if curTime > T:
            break

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])):
                if have == 0:
                    if (visit[have][nextPos[0]][nextPos[1]] == 0) and (board[nextPos[0]][nextPos[1]] != 1):
                        if board[nextPos[0]][nextPos[1]] == 2:
                            List.append((nextPos,curTime+1,have+1))
                            visit[have+1][nextPos[0]][nextPos[1]] = curTime + 1
                        else:
                            List.append((nextPos, curTime + 1, have))
                            visit[have][nextPos[0]][nextPos[1]] = curTime + 1
                else:
                    if (visit[have][nextPos[0]][nextPos[1]] == 0):
                        List.append((nextPos,curTime+1,have))
                        visit[have][nextPos[0]][nextPos[1]] = curTime+1

List = deque()
List.append(((0,0), 0,0))
bfs(List)

minTime = T + 1

for i in range(2):
    if visit[i][N-1][M-1] !=0:
        minTime = min(minTime,visit[i][N-1][M-1])

if (minTime == T + 1):
    print("Fail")
else:
    print(minTime)
