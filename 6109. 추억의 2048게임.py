import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def change_board(board,S):
    new_board = [[0 for i in range(N)] for j in range(N)]
    if S == "up":
        for col in range(N):
            lst = []
            for row in range(N):
                if board[row][col] !=0:
                    lst.append(board[row][col])
            index = 0
            r = 0
            while index < len(lst)-1:
                if lst[index] == lst[index+1]:
                    new_board[r][col] = 2 * lst[index]
                    index +=2
                    r +=1
                else:
                    new_board[r][col] = lst[index]
                    index+=1
                    r +=1
            if index == len(lst) - 1:
                new_board[r][col] = lst[index]

    elif S == "down":
        for col in range(N):
            lst = []
            for row in range(N-1,-1,-1):
                if board[row][col] !=0:
                    lst.append(board[row][col])
            index = 0
            r = N-1
            while index < len(lst)-1:
                if lst[index] == lst[index +1]:
                    new_board[r][col] = 2 * lst[index]
                    index +=2
                    r -=1
                else:
                    new_board[r][col] = lst[index]
                    index+=1
                    r-=1
            if index == len(lst) - 1:
                new_board[r][col] = lst[index]
    elif S == "left":
        for row in range(N):
            lst= []
            for col in range(N):
                if board[row][col] !=0:
                    lst.append(board[row][col])
            index = 0
            c = 0
            while index < len(lst)-1:
                if lst[index] == lst[index+1]:
                    new_board[row][c] = 2 * lst[index]
                    index+=2
                    c +=1
                else:
                    new_board[row][c] = lst[index]
                    index +=1
                    c +=1
            if index == len(lst) - 1:
                new_board[row][c] = lst[index]
    else:
        for row in range(N):
            lst = []
            for col in range(N-1,-1,-1):
                if board[row][col] !=0:
                    lst.append(board[row][col])
            index = 0
            c = N-1
            while index < len(lst)-1:
                if lst[index] == lst[index +1]:
                    new_board[row][c] = 2 * lst[index]
                    index +=2
                    c -=1
                else:
                    new_board[row][c] = lst[index]
                    index +=1
                    c -=1
            if index == len(lst) - 1:
                new_board[row][c] = lst[index]
    return new_board

for test in range(1,T+1):
    N, S = tuple(map(str,input().rstrip().split()))
    N = int(N)
    board = [[int(i) for i in input().rstrip().split()] for j in range(N)]
    board = change_board(board,S)
    print('#'+str(test))
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=' ')
        print()
