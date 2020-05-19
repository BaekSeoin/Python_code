import sys
import heapq
from collections import deque

sys.stdin = open('input.txt','r')

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<501) and (0<=b<501):
        return True
    return False

start = (0,0)
end = (500,500)

board = [[0 for i in range(500+1)] for j in range(500+1)]

dangerous = int(sys.stdin.readline().rstrip())
numOfDangerous = 0

for i in range(dangerous):
    a,b,x,y = map(int, sys.stdin.readline().rstrip().split())
    min_i = min(a,x)
    max_i = max(a,x)
    min_j = min(b,y)
    max_j = max(b,y)
    for k in range(min_i,max_i+1):
        for r in range(min_j, max_j+1):
            board[k][r] = 1
            numOfDangerous +=1

death = int(sys.stdin.readline().rstrip())

for i in range(death):
    a,b,x,y = map(int, sys.stdin.readline().rstrip().split())
    min_i = min(a,x)
    max_i = max(a,x)
    min_j = min(b,y)
    max_j = max(b,y)
    for k in range(min_i,max_i+1):
        for r in range(min_j, max_j+1):
            board[k][r] = 2

List = deque()
List.append((0, start))
#heapq.heappush(List,(0,start))

visit = [[[0 for i in range(501)] for j in range(501)] for k in range(numOfDangerous+1)]
visit[0][0][0] = 1

def bfs(List):
    while List:
        x = List.popleft()
        curPos = x[1]
        crush = x[0]

        if curPos == end:
            continue

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])

            if (inRange(nextPos[0],nextPos[1])):
                if (board[nextPos[0]][nextPos[1]] == 0) and (visit[crush][nextPos[0]][nextPos[1]] == 0):
                    stop = False
                    for i in range(crush):
                        if visit[i][nextPos[0]][nextPos[1]] == 1:
                            stop = True
                            break
                    if stop:
                        continue
                    #heapq.heappush(List, (crush, nextPos))
                    List.append((nextPos, crush))
                    visit[crush][nextPos[0]][nextPos[1]] = 1

                if (board[nextPos[0]][nextPos[1]] == 1) and (crush+1 <= numOfDangerous) and (visit[crush+1][nextPos[0]][nextPos[1]]==0):
                    stop = False
                    for i in range(crush+1):
                        if visit[i][nextPos[0]][nextPos[1]]==1:
                            stop = True
                            break
                    if stop:
                        continue
                    #heapq.heappush(List, (crush+1, nextPos))
                    List.append((nextPos, crush+1))
                    visit[crush + 1][nextPos[0]][nextPos[1]] = 1


bfs(List)
