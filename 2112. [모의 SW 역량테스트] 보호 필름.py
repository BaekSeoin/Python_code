import sys
import copy

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def Pass(board):
    count = 0
    for column in range(W):
        for row in range(D-(K-1)):
            c = 0
            for j in range(1,K):
                if board[row][column] == board[row+j][column]:
                    c +=1
                else:break
            if c == K-1:
                count +=1
                break
        if c != K-1:
            return False
    if count == W:
        return True
    return False

def change(board,row,number):
    for column in range(W):
        board[row][column] = number
    return board


def dfs(board,row,count):
    global Ans
    for i in range(3):
        if i == 0:
            B = copy.deepcopy(board[row])
        if i == 0 or i == 1:
            board = change(board,row,i)
        if Pass(board):
            if i == 0 or i == 1:
                if count + 1 < Ans:
                    Ans = count + 1
            else:
                if count < Ans:
                    Ans = count
            #print(Ans,row)
        else:
            if row + 1 < D and count + 1 < Ans and (i == 0 or i == 1):
                dfs(board,row+1,count +1)
            elif row + 1 < D and count < Ans and i == 2:
                dfs(board, row + 1, count)
        if i == 1:
            board[row] = B

for test in range(1,T+1):
    #두께, 가로크기, 합격기준
    D, W, K = tuple(map(int, input().rstrip().split()))
    board = [[int(i) for i in input().rstrip().split()] for j in range(D)]
    result = 0
    print('#'+str(test),end=' ')
    Ans = 1000
    if K == 1:
        print(result)
    elif Pass(board):
        print(result)
    else:
        dfs(board,0,result)
        print(Ans)