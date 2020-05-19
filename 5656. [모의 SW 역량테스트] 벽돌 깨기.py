import sys
import copy
from collections import deque

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

#상하좌우
direction = [(-1,0),(1,0),(0,-1),(0,1)]

def inRange(a,b):
    if 0<=a<H and 0<=b<W:
        return True
    return False

def move(current,board):
    A = board[current[0]][current[1]]
    board[current[0]][current[1]] = 0
    for dir in direction:
        nextPos = (current[0] + dir[0], current[1] + dir[1])
        for n in range(A-1):
            if inRange(nextPos[0], nextPos[1]):
                if board[nextPos[0]][nextPos[1]] >1:
                    board = move(nextPos, board)
                board[nextPos[0]][nextPos[1]] = 0
                nextPos = (nextPos[0] + dir[0], nextPos[1] + dir[1])
    return board

def remove_zero(board):
    for j in range(W):
        List = []
        for i in range(H):
            if board[i][j] !=0:
                List.append(board[i][j])
                board[i][j] = 0
        x = H-1
        while List:
            b = List.pop()
            board[x][j] = b
            x -= 1
    return board

def find_start(first,board):
    for y in range(H):
        if board[y][first] !=0:
            return (y,first)
    return 0


for test in range(1,T+1):
    N,W,H = tuple(map(int, input().rstrip().split()))
    board = [[int(i) for i in input().rstrip().split()] for j in range(H)]
    board2 = copy.deepcopy(board)
    collect = deque()
    collect.append(board2)
    for num in range(N):
        LEN = len(collect)
        for r in range(LEN):
            for first in range(W):
                board3 = copy.deepcopy(collect[0])
                current = find_start(first,board3)
                if current != 0:
                    board3 = move(current,board3)
                    board3 = remove_zero(board3)
                    collect.append(board3)
            collect.popleft()

    Min_count = 10000
    while collect:
        count = 0
        now = collect.popleft()
        for v in range(H):
            for l in range(W):
                if now[v][l] !=0:
                    count +=1
        if count < Min_count:
            Min_count = count
    print('#'+str(test),end=' ')
    if Min_count != 10000:
        print(Min_count)
    else:
        print(0)