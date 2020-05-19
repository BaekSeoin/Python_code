#적록색약
import sys
import copy

sys.setrecursionlimit(100000)
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())
board = [[i for i in sys.stdin.readline().rstrip()] for i in range(N)]
board_Y = copy.deepcopy(board)
board_N = copy.deepcopy(board)


direction = [(-1,0),(1,0),(0,-1),(0,1)]

def InRange(a):
    if 0 <= a[0] and a[0] < N and 0 <= a[1] and a[1] < N:
        return True
    return False

def dfs_Y(board_Y,a):
    if board_Y[a[0]][a[1]] != 'P':
        color = board_Y[a[0]][a[1]]
        board_Y[a[0]][a[1]] = 'P'

        for i in direction:
            nextPos = (a[0]+i[0], a[1]+i[1])

            if InRange(nextPos) and (color == 'R' or color == 'G'):
                if board_Y[nextPos[0]][nextPos[1]] == 'R' or board_Y[nextPos[0]][nextPos[1]] == 'G':
                    dfs_Y(board_Y, nextPos)

            elif InRange(nextPos) and color == 'B':
                if board_Y[nextPos[0]][nextPos[1]] == 'B':
                    dfs_Y(board_Y, nextPos)
        return True
    return False


def dfs_N(board_N,a):
    if board_N[a[0]][a[1]] != 'P':
        color = board_N[a[0]][a[1]]
        board_N[a[0]][a[1]] = 'P'

        for i in direction:
            nextPos = (a[0]+i[0], a[1]+i[1])

            if InRange(nextPos) and color == board_N[nextPos[0]][nextPos[1]]:
                dfs_N(board_N, nextPos)
        return True
    return False


cnt_Y = 0
cnt_N = 0


for i in range(N):
    for j in range(N):
        if dfs_N(board_N,(i,j)):
            cnt_N +=1
        if dfs_Y(board_Y,(i,j)):
            cnt_Y += 1

print(cnt_N, cnt_Y)








