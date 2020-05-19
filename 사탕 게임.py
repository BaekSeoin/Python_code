import sys
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<N):
        return True
    return False


def dfs(curPos,n,count,alpha):
    global num
    if n == 0:
        nextPos = (curPos[0], curPos[1] + 1)
        if (inRange(nextPos[0],nextPos[1])) and (visit[n][nextPos[0]][nextPos[1]] == 0) and (board[nextPos[0]][nextPos[1]] == alpha):
            visit[n][nextPos[0]][nextPos[1]] = count + 1
            num = count + 1
            dfs(nextPos,n,count + 1,alpha)
            visit[n][nextPos[0]][nextPos[1]] = num
    elif n == 1:
        nextPos = (curPos[0]+1, curPos[1])
        if (inRange(nextPos[0],nextPos[1])) and (visit[n][nextPos[0]][nextPos[1]] == 0) and (board[nextPos[0]][nextPos[1]] == alpha):
            visit[n][nextPos[0]][nextPos[1]] = count + 1
            num = count + 1
            dfs(nextPos,n,count + 1,alpha)
            visit[n][nextPos[0]][nextPos[1]] = num

maxNum = 0

for a in range(N):
    for b in range(N):
        for c in range(2):
            if c == 0:
                try:
                    x = board[a][b]
                    y = board[a][b+1]
                    board[a][b] = y
                    board[a][b+1] = x
                except:
                    continue
            elif c == 1:
                try:
                    x = board[a][b]
                    y = board[a+1][b]
                    board[a][b] = y
                    board[a+1][b] = x
                except:
                    continue
            #0 = 가로, 1 = 세로
            visit = [[[0 for i in range(N)] for j in range(N)] for k in range(2)]

            for i in range(N):
                for j in range(N):
                    if visit[0][i][j] == 0:
                        curPos = (i,j)
                        visit[0][i][j] = 1
                        num = 1
                        alpha = board[i][j]
                        dfs(curPos,0,1,alpha)
                        visit[0][i][j] = num
                        maxNum = max(maxNum,num)
                    if visit[1][i][j] == 0:
                        curPos = (i, j)
                        visit[1][i][j] = 1
                        num = 1
                        alpha = board[i][j]
                        dfs(curPos,1,1,alpha)
                        visit[1][i][j] = num
                        maxNum = max(maxNum, num)
            if c == 0:
                board[a][b] = x
                board[a][b+1] = y

            elif c == 1:
                board[a][b] = x
                board[a+1][b] = y


print(maxNum)



