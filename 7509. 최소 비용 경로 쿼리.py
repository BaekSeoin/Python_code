import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

T = int(input())
direction = [(1,0),(0,1),(-1,0),(0,-1)]

def inRange(a,b):
    if 0 <= a <row and 0<= b < column:
        return True
    return False

def bfs(List, end, Min):

    while List:
        a = List.popleft()
        current = a[0]
        dist = a[1]
        check = a[2]

        if current == end:
            if Min == None:
                Min = dist

            elif dist < Min:
                Min = dist

            continue

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1])

            if inRange(nextPos[0], nextPos[1]) and check[nextPos[0]][nextPos[1]] == 0:
                dist_2 = dist + board[nextPos[0]][nextPos[1]]
                check_2 = copy.deepcopy(check)
                check_2[nextPos[0]][nextPos[1]] = 1
                List.append((nextPos, dist_2, check_2))
    return Min

for i in range(T):
    row, column, Q = tuple(map(int, input().split()))
    board = [[int(i) for i in input().split()] for j in range(row)]
    result = []
    for j in range(Q):
        a,b,c,d = tuple(map(int, input().split()))
        start = (a-1, b-1)
        end = (c-1, d-1)
        List = deque()
        Min = None
        check = [[0 for i in range(column)] for j in range(row)]
        dist = board[start[0]][start[1]]
        check[start[0]][start[1]] = 1
        List.append((start, dist, check))
        result.append(bfs(List, end, Min))

    print('#',end='')
    print(i+1, end = ' ')
    print(sum(result))