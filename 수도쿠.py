import sys

sys.stdin = open("input.txt", "r")

board = []

pos = []

for i in range(9):
    x = []
    for index, j in enumerate(sys.stdin.readline().rstrip().split()):
        if int(j) == 0:
            pos.append((i, index))
        x.append(int(j))
    board.append(x)


def Range(current_pos):
    if 0 <= current_pos < 3:
        ans = 3
    elif 3 <= current_pos < 6:
        ans = 6
    else:
        ans = 9
    return ans


def find(a, b, row, col):
    L = [0 for k in range(10)]

    for i in range(int(a) - 3, int(a)):
        for j in range(int(b) - 3, int(b)):
            L[board[i][j]] = 1
    for i in range(9):
        if board[row][i] != 0:
            L[board[row][i]] = 1
    for j in range(9):
        if board[j][col] != 0:
            L[board[j][col]] = 1
    collect = []
    for num, check in enumerate(L):
        if num != 0:
            if check == 0:
                collect.append(num)

    return collect


count = 0

def dfs(board, order):
    global count
    if order == len(pos):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end=' ')
            print()
        count = 1
        return

    current = pos[order]
    a = Range(current[0])
    b = Range(current[1])
    collect = find(a, b, current[0], current[1])

    for number in collect:
        board[current[0]][current[1]] = number
        dfs(board, order + 1)
        if count == 1:
            return
        board[current[0]][current[1]] = 0


dfs(board, 0)