#단지번호붙이기
import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip()] for i in range(N)]
direction = [(-1,0),(1,0),(0,-1),(0,1)]
home_num = []
T = 2

def InRange(a):
    if 0 <= a[0] and a[0] < N and 0<= a[1] and a[1] < N:
        return True
    return False

def dfs(board,a,T):
    global cnt
    if board[a[0]][a[1]] == 1:
        board[a[0]][a[1]] = T
        cnt += 1

        for h in direction:
            nextPos = (a[0]+h[0], a[1]+h[1])
            if InRange(nextPos):
                dfs(board, nextPos,T)
        return True

    return False

for i in range(N):
    for j in range(N):
        cnt = 0
        if dfs(board, (i,j),T):
            T += 1
            home_num.append(cnt)

print(T-2)
home_num.sort()
for i in home_num:
    print(i)

