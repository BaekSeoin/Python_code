import sys
import copy
from collections import deque

sys.stdin = open('input.txt','r')


N,M = map(int, sys.stdin.readline().rstrip().split())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

direction = [(-1,0),(1,0),(0,1),(0,-1)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<N):
        return True
    return False

virus = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i,j))

vlen = len(virus)
virus_candidate = []
def dfs(index,List):
    if len(List) == M:
        virus_candidate.append(copy.deepcopy(List))
        return

    if index == vlen:
        return

    List.append(virus[index])
    dfs(index+1,List)
    List.pop()
    dfs(index+1,List)

List = []
dfs(0,List)

def bfs(virus_1):
    visit = [[-1 for i in range(N)] for j in range(N)]

    virus_2 = deque()

    for i in virus_1:
        virus_2.append((i,0))
        visit[i[0]][i[1]] = 0

    while virus_2:
        x = virus_2.popleft()
        curPos = x[0]
        count = x[1]

        for dir in direction:
            nextPos = (curPos[0] + dir[0],curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (board[nextPos[0]][nextPos[1]] != 1) and (visit[nextPos[0]][nextPos[1]] ==-1):
                visit[nextPos[0]][nextPos[1]] = count + 1
                virus_2.append((nextPos,count+1))


    Max = 0
    for i in range(N):
        for j in range(N):
            if (board[i][j] != 1):
                if visit[i][j] == -1:
                    return -1
                if board[i][j] == 0:
                    Max = max(Max,visit[i][j])
    return Max


ans = -1

for virus_1 in virus_candidate:
    r = bfs(virus_1)
    if r != -1:
        if ans == -1:
            ans = r
        else:
            ans = min(ans,r)
print(ans)