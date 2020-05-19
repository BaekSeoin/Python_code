import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

N,M = map(int, sys.stdin.readline().rstrip().split())

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]



def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

direction = [(-1,0),(1,0),(0,-1),(0,1)]

d = (0,0)
s = (0,0)
wall = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'K':
            d = (i,j)
        elif board[i][j] == 'H':
            s = (i,j)

            for dir in direction:
                nextPos = (i+dir[0], j+dir[1])
                if (inRange(nextPos[0],nextPos[1])) and (board[nextPos[0]][nextPos[1]] == '.'):
                    wall.append(nextPos)


def dfs(n,index, List):

    if len(List) == n:
        wall_2.append(copy.deepcopy(List))
        return
    if index >= len(wall):
        return

    List.append(wall[index])
    dfs(n,index+1,List)
    List.pop()
    dfs(n,index+1,List)

ans = -1

def bfs(lst):
    while lst:
        curPos = lst.popleft()

        if curPos == s:
            return True

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])

            if (inRange(nextPos[0],nextPos[1])) and (visit[nextPos[0]][nextPos[1]] == 0) and (board[nextPos[0]][nextPos[1]] == '.'):
                visit[nextPos[0]][nextPos[1]] = 1
                lst.append(nextPos)
    return False


for n in range(1,len(wall)+1):
    wall_2 = []
    List = []
    dfs(n,0,List)

    stop = False
    for l in wall_2:
        for i,j in l:
            board[i][j] = '#'
        visit = [[0 for i in range(M)] for j in range(N)]
        lst = deque()
        lst.append(d)
        visit[d[0]][d[1]] = 1
        a = bfs(lst)
        print(a)

        if a:
            ans = n
            stop = True
            break
        else:
            for i, j in l:
                board[i][j] = '.'
    if stop:
        break
print(ans)

