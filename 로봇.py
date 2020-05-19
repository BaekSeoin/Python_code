import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int, sys.stdin.readline().rstrip().split())
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

start = [int(i) for i in sys.stdin.readline().rstrip().split()]
end = [int(i) for i in sys.stdin.readline().rstrip().split()]
start = (start[0]-1, start[1]-1,start[2])
end = (end[0]-1, end[1]-1, end[2])

visit = [[[0 for i in range(M)] for j in range(N)] for k in range(5)]

#동/서/남/북
direction = {1:(0,1),2:(0,-1),3:(1,0),4:(-1,0)}

#왼/오
change_direction = {1:(4,3),2:(3,4),3:(1,2),4:(2,1)}

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

def check(k,curPos,dir):
    for i in range(1,k+1):
        nextPos = (curPos[0] + dir[0] * i, curPos[1] + dir[1] * i)
        if board[nextPos[0]][nextPos[1]] == 1:
            return False
    return True

def bfs(List):
    while List:
        x = List.popleft()
        curPos = x[0]
        numOfOrder = x[1]
        dir = direction[curPos[2]]

        if curPos == end:
            print(numOfOrder)
            return

        for k in range(1,6):
            if k <= 3:
                nextPos = (curPos[0] + dir[0] * k, curPos[1] + dir[1] * k)
                if (inRange(nextPos[0],nextPos[1])) and (visit[curPos[2]][nextPos[0]][nextPos[1]] == 0):
                    if check(k,curPos,dir):
                        visit[curPos[2]][nextPos[0]][nextPos[1]] = 1
                        nextPos = (nextPos[0],nextPos[1], curPos[2])
                        List.append((nextPos,numOfOrder+1))

            elif k == 4: #왼쪽으로 turn
                newDir = change_direction[curPos[2]][0]
                if visit[newDir][curPos[0]][curPos[1]] == 0:
                    visit[newDir][curPos[0]][curPos[1]] = 1
                    nextPos = (curPos[0],curPos[1], newDir)
                    List.append((nextPos,numOfOrder+1))
            elif k == 5: #오른쪽으로 turn
                newDir = change_direction[curPos[2]][1]
                if visit[newDir][curPos[0]][curPos[1]] == 0:
                    visit[newDir][curPos[0]][curPos[1]] = 1
                    nextPos = (curPos[0],curPos[1], newDir)
                    List.append((nextPos,numOfOrder+1))


List = deque()
List.append((start,0))
visit[start[2]][start[0]][start[1]] = 1
bfs(List)