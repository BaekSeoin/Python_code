import sys

sys.stdin = open("input.txt", "r")

N,M,R = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

def turn(board,n,m,r,c):
    first = []
    second = []
    third = []
    fourth = []

    for col in range(c,m+1):
        first.append(board[r][col])
    for row in range(r,n+1):
        second.append(board[row][m])
    for col in range(c,m+1):
        third.append(board[n][col])
    for row in range(r,n+1):
        fourth.append(board[row][c])

    for num, col in zip(first[1:],range(c,m)):
        board[r][col] = num
    for num, row in zip(second[1:],range(r,n)):
        board[row][m] = num
    for num, col in zip(third[:-1],range(c+1,m+1)):
        board[n][col] = num
    for num, row in zip(fourth[:-1],range(r+1,n+1)):
        board[row][c] = num

for time in range(R):
    for t in range(min(N,M)//2):
        turn(board,N-1-t,M-1-t,t,t)
for i in range(N):
    for j in range(M):
        print(board[i][j],end=' ')
    print()