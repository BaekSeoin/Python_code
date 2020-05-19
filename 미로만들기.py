import sys
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(N)]

blackRoom = 0

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<N):
        return True
    return False

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            blackRoom +=1

visit = [[[0 for i in range(N)] for j in range(N)] for k in range(blackRoom+1)]

start = (0,0)
end = (N-1,N-1)
dist = 0

List = deque()
List.append((start,dist,0))

def bfs(List):
    while List:
        x = List.popleft()
        curPos = x[0]
        dist = x[1]
        crush = x[2]

        if curPos == end:
            continue

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if inRange(nextPos[0], nextPos[1]):
                if (board[nextPos[0]][nextPos[1]] == 1) and (visit[crush][nextPos[0]][nextPos[1]] == 0):
                    visit[crush][nextPos[0]][nextPos[1]] = 1
                    List.append((nextPos, dist+1, crush))
                elif (board[nextPos[0]][nextPos[1]] == 0):
                    if (crush + 1) <= blackRoom and (visit[crush+1][nextPos[0]][nextPos[1]] == 0):
                        visit[crush+1][nextPos[0]][nextPos[1]] = 1
                        List.append((nextPos, dist+1, crush+1))

bfs(List)

for b in range(blackRoom+1):
    if visit[b][end[0]][end[1]] != 0:
        print(b)
        break