import sys

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def check_col(row, column):
    for i in range(column-1):
        if board[row][i] == board[row][i+1]:
            continue
        elif board[row][i] - board[row][i+1] == 1:
            if visited[row][i+1] == 0:
                for j in range(1,X):
                    try:
                        if board[row][i+1] == board[row][i+1+j] and visited[row][i+1+j] == 0:
                            continue
                        else:
                            return False
                    except:
                        return False
                for j in range(0,X):
                    visited[row][i+1+j] = 1
            else:
                return False

        elif board[row][i] - board[row][i+1] == -1:
            if visited[row][i] == 0:
                for j in range(1,X):
                    if (i-j) <0 or (i-j) >= N:
                        return False
                    elif visited[row][i-j] !=0:
                        return False
                    elif board[row][i] == board[row][i-j]:
                        continue
                    else:
                        return False
                for j in range(0,X):
                    visited[row][i-j] = 1
            else:
                return False
        else:
            return False
    return True

def check_row(row, column):
    for i in range(row-1):
        if board[i][column] == board[i+1][column]:
            continue
        elif board[i][column] - board[i+1][column] == 1:
            if visited[i+1][column] == 0:
                for j in range(1,X):
                    try:
                        if board[i+1][column] == board[i+1+j][column] and visited[i+1+j][column] == 0:
                            continue
                        else:
                            return False
                    except:
                        return False
                for j in range(0,X):
                    visited[i+1+j][column] = 1
            else:
                return False

        elif board[i][column] - board[i+1][column] == -1:
            if visited[i][column] == 0:
                for j in range(1,X):
                    if (i - j) < 0 or (i - j) >= N:
                        return False
                    elif visited[i-j][column] !=0:
                        return False
                    elif board[i][column] == board[i-j][column]:
                        continue
                    else:
                        return False
                for j in range(0,X):
                    visited[i-j][column] = 1
            else:
                return False
        else:
            return False
    return True


for test in range(1,T+1):
    N, X = tuple(map(int, input().rstrip().split()))
    board = [[int(i) for i in input().rstrip().split()] for j in range(N)]

    count = 0
    visited = [[0 for i in range(N)] for j in range(N)]
    for col in range(N):
        if check_row(N,col):
            count +=1
            #print(col)

    visited = [[0 for i in range(N)] for j in range(N)]
    for row in range(N):
        if check_col(row,N):
            count +=1
            #print(row)
    print('#'+str(test),end=' ')
    print(count)