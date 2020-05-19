import sys
import copy
import heapq

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def change(curPos,board):
    board[curPos[0]][curPos[1]] = 0
    if curPos[1] - 1 >= 0:
        board[curPos[0]][curPos[1] - 1] = 0
    if curPos[1] + 1 < M:
        board[curPos[0]][curPos[1] + 1] = 0

    if curPos[0] - 1 >=0:
        board[curPos[0] - 1] = copy.deepcopy(m)
    if curPos[0] + 1 < N:
        board[curPos[0] + 1] = copy.deepcopy(m)

def calculate_point(curPos,board):
    A,B,C,D,E = [0],[0],[0],[0],[0]
    A = board[curPos[0]][curPos[1]]
    if curPos[1] - 1 >= 0:
        B = board[curPos[0]][curPos[1] - 1]
    if curPos[1] + 1 < M:
        C = board[curPos[0]][curPos[1] + 1]

    if curPos[0] - 1 >=0:
        D = board[curPos[0] - 1]
    if curPos[0] + 1 < N:
        E = board[curPos[0] + 1]

    return A,B,C,D,E

for test in range(1,T+1):
    N,M = tuple(map(int,input().rstrip().split()))
    board = [[[int(i)] for i in input().rstrip().split()] for j in range(N)]
    Max_point = 0

    m = [[0] for i in range(M)]

    priority = []
    for i in range(N):
        for j in range(M):
            if board[i][j][0] != 0:
                A,B,C,D,E = calculate_point((i,j),board)
                point = A[0]

                value = [-board[i][j]]
                heapq.heappush(priority,(point,value,(i,j)))
    while priority:
        current = heapq.heappop(priority)
        curPos = current[2]
        cur_value = current[1][0]
        cur_point = -current[0]
        if cur_value == 0:
            continue
        else:
            Max_point += board[curPos[0]][curPos[1]]
            change(curPos,board)
    print('#'+str(test),end=' ')
    print(Max_point)