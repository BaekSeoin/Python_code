import sys
import copy
from collections import deque
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

direction = [(-1,0),(1,0),(0,-1),(0,1)]

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]


for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = (i,j)
            board[i][j] = 0



def inRange(a,b):
    if 0 <= a <n and 0 <= b < n:
        return True
    return False


def find_fish(board, List, result):
    Min_dist = 100000000
    check = [[100000000 for i in range(n)] for j in range(n)]
    b = List[0]
    check[b[0]][b[1]] = 0

    while List:
        current = List.popleft()
        if check[current[0]][current[1]] == Min_dist:
            break

        for i in direction:
            nextPos = (current[0]+i[0], current[1] + i[1])
            if inRange(nextPos[0],nextPos[1]) and board[nextPos[0]][nextPos[1]] <= shark_body and check[nextPos[0]][nextPos[1]] > check[current[0]][current[1]] + 1:
                List.append(nextPos)
                check[nextPos[0]][nextPos[1]] = check[current[0]][current[1]] + 1
                if board[nextPos[0]][nextPos[1]]!= 0 and board[nextPos[0]][nextPos[1]] < shark_body:
                    result.append(nextPos)
                    Min_dist = check[nextPos[0]][nextPos[1]]

    if Min_dist == 100000000:
        return False, False, False
    elif Min_dist != 100000000:
        return True, min(result), Min_dist


shark_body = 2
shark_count = 0
shark_time = 0
List = deque()
List.append(shark)


while True:

    result = []

    a = find_fish(board,List,result)
    if a[0] == False:
        break
    else:
        board[a[1][0]][a[1][1]] = 0
        List = deque()
        List.append(a[1])
        shark_count +=1
        shark_time += a[2]
        if shark_count == shark_body:
            shark_body += 1
            shark_count = 0

print(shark_time)