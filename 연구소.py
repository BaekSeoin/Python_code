import sys
import copy
sys.setrecursionlimit(100000)
sys.stdin = open("input.txt","r")

row, column = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(row)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]

def inRange(a,b):
    if 0<= a and a < row and 0<= b and b < column:
        return True
    return False

def dfs(a,b, board, check):
    check[a][b] = 1

    for i in direction:
        nextPos = (a + i[0], b + i[1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == 0 and check[nextPos[0]][nextPos[1]] == 0:
            board[nextPos[0]][nextPos[1]] = 2
            check[nextPos[0]][nextPos[1]] = 1
            dfs(nextPos[0], nextPos[1], board, check)
List = []
chosen = []
final = []

for i in range(row):
    for j in range(column):
        if board[i][j] == 0:
            List.append((i,j))


def choose(List, chosen,i, final):

    a = List[i]
    chosen.append(a)

    if len(chosen) == 3:
        c = copy.deepcopy(chosen)
        final.append(c)
        return

    for k in range(i+1,len(List)):
        choose(List, chosen,k, final)
        chosen.pop()
    return

for i in range(len(List)-1):
    choose(List, chosen,i, final)
    chosen.pop()


total = []


for q in final:
    check = [[0 for i in range(column)] for j in range(row)]

    board_2 = copy.deepcopy(board)
    board_2[q[0][0]][q[0][1]] = 1
    board_2[q[1][0]][q[1][1]] = 1
    board_2[q[2][0]][q[2][1]] = 1

    for y in range(row):
        for o in range(column):
            if board_2[y][o] == 2 and check[y][o] == 0:
                dfs(y,o, board_2, check)

    count = 0
    for e in range(row):
        for w in range(column):
            if board_2[e][w] == 0:
                count +=1
    total.append(count)

print(max(total))