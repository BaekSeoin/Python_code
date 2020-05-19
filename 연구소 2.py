import sys
import copy

sys.stdin = open("input.txt","r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = []
visited1 = [[-1 for i in range(N)] for j in range(N)]

virus = []

final_virus = []

def inRange(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

direction = [(-1,0),(1,0),(0,-1),(0,1)]

for i in range(N):
    new = []
    for j,num in enumerate(sys.stdin.readline().rstrip().split()):
        new.append(int(num))
        if int(num) == 2:
            virus.append((i,j))
        if int(num) == 1:
            visited1[i][j] = -2
    board.append(new)

def dfs(index,List):
    if len(List) == M:
        final_virus.append(copy.deepcopy(List))
        return

    for i in range(index+1,len(virus)):
        List.append(virus[i])
        dfs(i,List)
        List.pop()

List = []
dfs(-1, List)

def bfs(Lst):
    while Lst:
        x = Lst.pop(0)
        curPos = x[0]
        count = x[1]

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if inRange(nextPos[0],nextPos[1]) and visited[nextPos[0]][nextPos[1]] == -1:
                visited[nextPos[0]][nextPos[1]] = count+1
                Lst.append((nextPos,count+1))
    return count

def check(visited):
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                return False
    return True

min_count = 10000
for vir in final_virus:
    Lst = []
    visited = copy.deepcopy(visited1)
    for v in vir:
        visited[v[0]][v[1]] = 0
        Lst.append((v,0))
    count = bfs(Lst)
    if check(visited):
        if count < min_count:
            min_count = count
if min_count == 10000:
    print(-1)
else:
    print(min_count)

