#구슬탈출 2
import sys
from collections import deque
import copy
sys.stdin = open("input.txt","r")

row, column = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(row)]

def inRange(a,b):
    if 0 <= a < row and 0 <= b and column:
        return True
    return False

def change(board, dir):
    number = 0

    #왼쪽이동
    if dir == 1:
        for i in range(1,row-1):
            for j in range(1,column-1):
                if board[i][j] == '.' or board[i][j] =='O' or board[i][j] =='#':
                    continue
                else:
                    x = board[i][j]
                    nextPos = (i,j-1)
                    if nextPos[1] == 0:
                        continue
                    while inRange(nextPos[0],nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == '.':
                            nextPos = (nextPos[0], nextPos[1] -1)
                        elif board[nextPos[0]][nextPos[1]] == 'O':
                            if x == 'R':
                                number +=2
                            else:
                                number +=1
                            board[i][j] = '.'
                            break
                        else:
                            if (nextPos[0], nextPos[1]+1) == (i,j):
                                break
                            else:
                                board[nextPos[0]][nextPos[1]+1] = x
                                board[i][j] = '.'
                                break
            if number == 3 or number == 1:
                return False
            elif number == 2:
                return True
    # 오른쪽이동
    if dir == 2:
        for i in range(1, row - 1):
            for j in range(column-2,0,-1):
                if board[i][j] == '.' or board[i][j] == 'O' or board[i][j] == '#':
                    continue
                else:
                    x = board[i][j]
                    nextPos = (i, j + 1)
                    if nextPos[1] == column-1:
                        continue
                    while inRange(nextPos[0], nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == '.':
                            nextPos = (nextPos[0], nextPos[1] + 1)
                        elif board[nextPos[0]][nextPos[1]] == 'O':
                            if x == 'R':
                                number +=2
                            else:
                                number +=1
                            board[i][j] = '.'
                            break
                        else:
                            if (nextPos[0], nextPos[1]-1) == (i,j):
                                break
                            else:
                                board[nextPos[0]][nextPos[1] - 1] = x
                                board[i][j] = '.'
                                break
            if number == 3 or number == 1:
                return False
            elif number == 2:
                return True
    # 위쪽이동
    if dir == 3:
        for j in range(1, column - 1):
            for i in range(1, row-1):
                if board[i][j] == '.' or board[i][j] == 'O' or board[i][j] == '#':
                    continue
                else:
                    x = board[i][j]
                    nextPos = (i-1, j)
                    if nextPos[0] == 0:
                        continue
                    while inRange(nextPos[0], nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == '.':
                            nextPos = (nextPos[0]-1, nextPos[1])
                        elif board[nextPos[0]][nextPos[1]] == 'O':
                            if x == 'R':
                                number +=2
                            else:
                                number +=1
                            board[i][j] = '.'
                            break
                        else:
                            if (nextPos[0]+1, nextPos[1]) == (i,j):
                                break
                            else:
                                board[nextPos[0]+1][nextPos[1]] = x
                                board[i][j] = '.'
                                break
            if number == 3 or number == 1:
                return False
            elif number == 2:
                return True
    # 아래쪽이동
    if dir == 4:
        for j in range(1, column - 1):
            for i in range(row-2,0,-1):
                if board[i][j] == '.' or board[i][j] == 'O' or board[i][j] == '#':
                    continue
                else:
                    x = board[i][j]
                    nextPos = (i+1, j)
                    if nextPos[0] == row-1:
                        continue
                    while inRange(nextPos[0], nextPos[1]):
                        if board[nextPos[0]][nextPos[1]] == '.':
                            nextPos = (nextPos[0]+1, nextPos[1])
                        elif board[nextPos[0]][nextPos[1]] == 'O':
                            if x == 'R':
                                number +=2
                            else:
                                number +=1
                            board[i][j] = '.'
                            break
                        else:
                            if (nextPos[0]-1, nextPos[1]) == (i,j):
                                break
                            else:
                                board[nextPos[0]-1][nextPos[1]] = x
                                board[i][j] = '.'
                                break
            if number == 3 or number == 1:
                return False
            elif number == 2:
                return True
    return board



List = deque()
count = 0
List.append((board,count,0))

while List:
    q = List.popleft()
    board =q[0]
    count = q[1]
    direction = q[2]

    if count == 10:
        print(-1)
        break

    for i in range(1,5):
        if count >= 2:
            if i ==1 and (direction == 1 or direction == 2):
                continue
            elif i == 2 and (direction == 1 or direction == 2):
                continue
            elif i == 3 and (direction == 4 or direction ==3):
                continue
            elif i == 4 and (direction == 3 or direction ==4):
                continue
        board_2 = copy.deepcopy(board)
        a = change(board_2, i)
        if a == True:
            print(count+1)
            break
        elif a == False:
            continue
        else:
            List.append((a,count+1,i))
    if a == True:
        break

