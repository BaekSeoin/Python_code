import sys

sys.stdin = open("input.txt", "r")

R,C,N = tuple(map(int,sys.stdin.readline().rstrip().split()))

board = []
time = []

for i in range(R):
    board_2 = []
    time_2 = []
    for text in sys.stdin.readline().rstrip():
        board_2.append(text)
        time_2.append(0)
    board.append(board_2)
    time.append(time_2)

def inRange(a,b,chart,x):
    if 0<=a<R and 0<=b<C:
        chart[a][b] = x
    return chart

def time_pass(board,time):
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'O':
                time[i][j] +=1
    return board, time

def bomb_destroy(board,time):
    List = []
    for i in range(R):
        for j in range(C):
            if time[i][j] == 3:
                board = inRange(i,j,board,'.')
                board = inRange(i-1, j, board, '.')
                board = inRange(i+1, j, board, '.')
                board = inRange(i, j-1, board, '.')
                board = inRange(i, j+1, board, '.')
                List.append((i,j))

    for i,j in List:
        time = inRange(i,j,time,0)
        time = inRange(i-1, j, time, 0)
        time = inRange(i+1, j, time, 0)
        time = inRange(i, j-1, time, 0)
        time = inRange(i, j+1, time, 0)

    return board, time

def bomb_install(board):
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 'O'
    return board


for n in range(1,N+1):
    if n == 1:
        board, time = time_pass(board, time)

    elif n % 2 == 0:
        board,time = time_pass(board,time)
        board = bomb_install(board)
    else:
        board, time = time_pass(board, time)
        board, time = bomb_destroy(board, time)


for i in range(R):
    for j in range(C):
        print(board[i][j],end='')
    print()