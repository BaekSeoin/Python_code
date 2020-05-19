import sys
from collections import deque

sys.stdin = open("input.txt","r")

T = int(input())

direction = {1:[(-1,0),(1,0),(0,-1),(0,1)],2:[(-1,0),(1,0)],3:[(0,-1),(0,1)],4:[(-1,0),(0,1)],5:[(1,0),(0,1)],6:[(1,0),(0,-1)],7:[(-1,0),(0,-1)]}
go_or_not = {(1,0):[1,2,4,7],(-1,0):[1,2,5,6],(0,-1):[1,3,4,5],(0,1):[1,3,6,7]}

def inRange(a,b):
    if 0 <= a < row and 0 <= b < column:
        return True
    return False

def bfs(List):
    global count
    while List:
        a = List.popleft()
        current = a[0]
        depth = a[1]
        dir = board[current[0]][current[1]]

        if depth == time:
            break

        if dir == 0:
            continue

        for i in direction[dir]:
            nextPos = (current[0] + i[0], current[1]+i[1])
            if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] != 0 and check[nextPos[0]][nextPos[1]] == 0:
                compare = board[nextPos[0]][nextPos[1]]
                b = go_or_not[i]

                if compare in b:
                    List.append((nextPos,depth+1))
                    check[nextPos[0]][nextPos[1]] = 1
                    count +=1

for i in range(T):
    row, column, start_row, start_column, time = tuple(map(int,input().rstrip().split()))
    board = [[int(j) for j in input().rstrip().split()] for k in range(row)]
    check = [[0 for j in range(column)] for k in range(row)]
    depth = 1
    count = 1
    List = deque()
    check[start_row][start_column] = 1
    List.append(((start_row, start_column),depth))
    bfs(List)
    print('#', end='')
    print(i+1, end=' ')
    print(count)
