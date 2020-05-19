import sys
import copy

sys.stdin = open("input.txt", "r")

M,N = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(M)]

def make_chess(a,b):
    new_board = []
    for i in range(a,a+8):
        x = []
        for j in range(b,b+8):
            x.append(board[i][j])
        new_board.append(copy.deepcopy(x))
    return new_board

def change_chess(new_board):
    count_a = 0
    count_b = 0
    for i in range(8):
        for j in range(8):
            if (i%2 == 0) and (j%2==0):
                if new_board[i][j] == 'B':
                    count_a +=1
            elif (i%2 == 0) and (j%2==1):
                if new_board[i][j] == 'W':
                    count_a +=1
            elif (i%2 ==1) and (j%2 == 0):
                if new_board[i][j] == 'W':
                    count_a+=1
            else:
                if new_board[i][j] == 'B':
                    count_a+=1
    for i in range(8):
        for j in range(8):
            if (i%2 == 0) and (j%2==0):
                if new_board[i][j] == 'W':
                    count_b +=1
            elif (i%2 == 0) and (j%2==1):
                if new_board[i][j] == 'B':
                    count_b +=1
            elif (i%2 ==1) and (j%2 == 0):
                if new_board[i][j] == 'B':
                    count_b+=1
            else:
                if new_board[i][j] == 'W':
                    count_b+=1
    return min(count_a,count_b)

min_final = []

for i in range(M-7):
    for j in range(N-7):
        new_board = make_chess(i,j)
        min_final.append(change_chess(new_board))

print(min(min_final))