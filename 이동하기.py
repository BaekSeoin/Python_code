import sys

sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10000000)

N,M = map(int,sys.stdin.readline().rstrip().split())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

start = (0,0)
end = (N-1,M-1)

direction = [(-1,0),(-1,-1),(0,-1)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

memo = [[-1 for i in range(M)] for j in range(N)]
memo[0][0] = board[0][0]

def dp(n,m):
    if memo[n][m] != -1:
        return memo[n][m]
    a = 0
    b = 0
    c = 0
    for index,dir in enumerate(direction):
        nextPos = (n + dir[0], m + dir[1])
        if (index == 0) and inRange(nextPos[0],nextPos[1]):
            a = dp(nextPos[0],nextPos[1])
        elif (index == 1) and inRange(nextPos[0],nextPos[1]):
            b = dp(nextPos[0],nextPos[1])
        elif (index == 2) and inRange(nextPos[0],nextPos[1]):
            c = dp(nextPos[0],nextPos[1])
    ans = max(a,b,c) + board[n][m]
    memo[n][m] = ans
    return ans

print(dp(end[0],end[1]))
