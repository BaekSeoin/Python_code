import sys
from collections import deque
import copy
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

def inRange(a,b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

def change_pos(board, check, dir):
    #왼쪽이동
    if dir == 1:
        for i in range(n):
            for j in range(n):
                number = board[i][j]
                if number == 0:
                    continue
                else:
                    nextPos = (i,j-1)
                    while inRange(nextPos[0],nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == 0:
                            board[nextPos[0]][nextPos[1]+1] = 0
                            board[nextPos[0]][nextPos[1]] = number
                            nextPos = (nextPos[0], nextPos[1]-1)
                        elif board[nextPos[0]][nextPos[1]] == number:
                            if check[nextPos[0]][nextPos[1]] ==0:
                                check[nextPos[0]][nextPos[1]] = 1
                                board[nextPos[0]][nextPos[1]] = 2 * number
                                board[nextPos[0]][nextPos[1]+1] = 0

                            break

                        elif board[nextPos[0]][nextPos[1]] != number:
                            break
    #오른쪽이동
    if dir == 2:
        for i in range(n):
            for j in range(n-1,-1,-1):
                number = board[i][j]
                if number == 0:
                    continue
                else:
                    nextPos = (i,j+1)
                    while inRange(nextPos[0],nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == 0:
                            board[nextPos[0]][nextPos[1]-1] = 0
                            board[nextPos[0]][nextPos[1]] = number
                            nextPos = (nextPos[0], nextPos[1]+ 1)
                        elif board[nextPos[0]][nextPos[1]] == number:
                            if check[nextPos[0]][nextPos[1]] ==0:
                                check[nextPos[0]][nextPos[1]] = 1
                                board[nextPos[0]][nextPos[1]] = 2 * number
                                board[nextPos[0]][nextPos[1]-1] = 0
                            break
                        elif board[nextPos[0]][nextPos[1]] != number:

                            break
    #위로이동
    if dir == 3:
        for j in range(n):
            for i in range(n):
                number = board[i][j]
                if number == 0:
                    continue
                else:
                    nextPos = (i-1,j)
                    while inRange(nextPos[0], nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == 0:
                            board[nextPos[0]+1][nextPos[1]] = 0
                            board[nextPos[0]][nextPos[1]] = number
                            nextPos = (nextPos[0]-1, nextPos[1])
                        elif board[nextPos[0]][nextPos[1]] == number:
                            if check[nextPos[0]][nextPos[1]] ==0:
                                check[nextPos[0]][nextPos[1]] = 1
                                board[nextPos[0]][nextPos[1]] = 2 * number
                                board[nextPos[0]+1][nextPos[1]] = 0
                            break
                        elif board[nextPos[0]][nextPos[1]] != number:

                            break
    #아래로이동
    if dir == 4:
        for j in range(n):
            for i in range(n-1,-1,-1):
                number = board[i][j]
                if number == 0:
                    continue
                else:
                    nextPos = (i+1,j)
                    while inRange(nextPos[0], nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == 0:
                            board[nextPos[0]-1][nextPos[1]] = 0
                            board[nextPos[0]][nextPos[1]] = number
                            nextPos = (nextPos[0]+1, nextPos[1])
                        elif board[nextPos[0]][nextPos[1]] == number:
                            if check[nextPos[0]][nextPos[1]] ==0:
                                check[nextPos[0]][nextPos[1]] = 1
                                board[nextPos[0]][nextPos[1]] = 2 * number
                                board[nextPos[0]-1][nextPos[1]] = 0
                            break
                        elif board[nextPos[0]][nextPos[1]] != number:
                            break
    return board

List = deque()
List.append((board, 1))
Max = 0

Max_number = 0
for i in range(n):
    for j in range(n):
        Max_number += board[i][j]

while List:
    a = List.popleft()
    board = a[0]
    count = a[1]

    for i in range(1,5):
        board_2 = copy.deepcopy(board)
        check = [[0 for k in range(n)] for j in range(n)]
        b = change_pos(board_2,check,i)
        if count <5:
            List.append((b,count + 1))
        for k in range(n):
            for u in range(n):
                if b[k][u] > Max:
                    Max = b[k][u]

        if Max == Max_number:
            break
    if Max == Max_number:
        break

print(Max)