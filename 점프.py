import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for i in range(N)]
board_2 = [[0 for i in range(N)] for i in range(N)]

def path(board,board_2,row, column):
    count = 0
    for i in range(1,row+1):
        if board[row-i][column] == i:
            if board_2[row-i][column] != 0:
                count += board_2[row-i][column]
            else:
                count += path(board, board_2, row-i, column)


    for j in range(1,column+1):
        if board[row][column-j] == j:
            if board_2[row][column-j] != 0:
                count += board_2[row][column-j]
            else: count += path(board, board_2, row, column-j)

    board_2[row][column] = count

    return count

value = board[0][0]
board_2[value][0] = 1
board_2[0][value] = 1

print(path(board, board_2, N-1, N-1))