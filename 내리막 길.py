import sys

sys.stdin = open("input.txt", "r")

M,N = tuple(map(int,sys.stdin.readline().rstrip().split()))
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(M)]
visited = [[-1 for i in range(N)] for j in range(M)]

#상하좌우
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<M and 0<=b<N:
        return True
    return False

def dp(current):
    if visited[current[0]][current[1]] != -1:
        return visited[current[0]][current[1]]

    ans = 0
    for dir in direction:
        nextPos = (current[0] + dir[0],current[1] + dir[1])
        if inRange(nextPos[0],nextPos[1]) and board[current[0]][current[1]] < board[nextPos[0]][nextPos[1]]:
            ans += dp(nextPos)
    visited[current[0]][current[1]] = ans
    return ans

visited[0][0] = 1

for i in range(M):
    for j in range(N):
        dp((i,j))

print(visited[M-1][N-1])
