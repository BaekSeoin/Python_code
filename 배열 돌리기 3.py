import sys
import copy

sys.stdin = open("input.txt","r")

N,M,R = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

calculate = [int(i) for i in sys.stdin.readline().rstrip().split()]

def type_1(board):
    new_board = [[] for i in range(N)]

    for row in range(N):
        new_board[N-1-row] = copy.deepcopy(board[row])
    return new_board

def type_2(board):
    new_board = [[] for i in range(N)]

    for row in range(N):
        A = board[row]
        for a in A[::-1]:
            new_board[row].append(a)
    return new_board

def type_3(board):
    new_board = [[] for i in range(N)]

    for row in range(M-1,-1,-1):
        A = board[row]
        count = 0
        for a in A:
            new_board[count].append(a)
            count +=1
    return new_board

def type_4(board):
    new_board = [[] for i in range(N)]

    for row in range(M):
        A = board[row]
        count = 0
        for a in A[::-1]:
            new_board[count].append(a)
            count +=1
    return new_board

def type_5(board):
    new_board = copy.deepcopy(board)

    for i in range(N//2):
        for j in range(M//2):
            new_board[i][j] = board[i + N//2][j]
    for i in range(N//2):
        for j in range(M//2,M):
            new_board[i][j] = board[i][j-M//2]
    for i in range(N//2,N):
        for j in range(M//2,M):
            new_board[i][j] = board[i-N//2][j]
    for i in range(N//2,N):
        for j in range(M//2):
            new_board[i][j] = board[i][j+M//2]
    return new_board

def type_6(board):
    new_board = copy.deepcopy(board)

    for i in range(N//2):
        for j in range(M//2):
            new_board[i][j] = board[i][j+M//2]
    for i in range(N//2):
        for j in range(M//2,M):
            new_board[i][j] = board[i+N//2][j]
    for i in range(N//2,N):
        for j in range(M//2,M):
            new_board[i][j] = board[i][j-M//2]
    for i in range(N//2,N):
        for j in range(M//2):
            new_board[i][j] = board[i-N//2][j]
    return new_board

for type in calculate:
    if type == 1:
        board = type_1(board)
    elif type == 2:
        board = type_2(board)
    elif type == 3:
        N,M = M,N
        board = type_3(board)
    elif type == 4:
        N, M = M, N
        board = type_4(board)
    elif type == 5:
        board = type_5(board)
    elif type == 6:
        board = type_6(board)

for i in range(N):
    for j in range(M):
        print(board[i][j],end=' ')
    print()