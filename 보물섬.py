import sys
from collections import deque

sys.stdin = open('input.txt','r')

R,C = map(int, sys.stdin.readline().rstrip().split())

map = [[i for i in sys.stdin.readline().rstrip()] for j in range(R)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<R) and (0<=b<C):
        return True
    return False


def bfs(List):
    global max_dist
    while List:
        a = List.popleft()
        cur = a[0]
        dist = a[1]

        if dist > max_dist:
            max_dist = dist

        for dir in direction:
            nextPos = (cur[0]+dir[0], cur[1] + dir[1])
            if (inRange(nextPos[0], nextPos[1])) and (map[nextPos[0]][nextPos[1]] == 'L') and (visit[nextPos[0]][nextPos[1]] == 0):
                List.append((nextPos,dist+1))
                visit[nextPos[0]][nextPos[1]] = 1
max_dist = 0

for i in range(R):
    for j in range(C):
        if map[i][j] == 'L':
            List = deque()
            dist = 0
            visit = [[0 for i in range(C)] for j in range(R)]
            List.append(((i,j), dist))
            visit[i][j] = 1
            bfs(List)
print(max_dist)