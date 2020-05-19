#토마토
import sys
from collections import deque
sys.stdin = open("input.txt","r")

column,row = tuple(map(int, sys.stdin.readline().rstrip().split()))
tomato = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(row)]
check = [[100000 for i in range(column)] for j in range(row)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]

def inRange(a,b):
    if 0<= a and a<row and 0<=b and b < column:
        return True
    return False

dist = 0
List = deque()

for i in range(row):
    for j in range(column):
        if tomato[i][j] == 1:
            check[i][j] = dist
            List.append(((i,j),dist))

while List:
    a = List.popleft()
    current = a[0]
    dist = a[1]

    for i in direction:
        nextPos = (current[0] + i[0], current[1] + i[1])
        if inRange(nextPos[0], nextPos[1]) and tomato[nextPos[0]][nextPos[1]] == 0 and check[nextPos[0]][nextPos[1]] == 100000:
            List.append(((nextPos[0],nextPos[1]),dist+1))
            check[nextPos[0]][nextPos[1]] = dist + 1
            tomato[nextPos[0]][nextPos[1]] = 1

count = 0
Max_dist = 0

if dist == 0:
    print(0)
else:
    for i in range(row):
        for j in range(column):
            if tomato[i][j] == 0:
                count +=1
    if count >0:
        print(-1)
    else:
        for i in range(row):
            for j in range(column):
                if check[i][j] > Max_dist and check[i][j] != 100000:
                    Max_dist = check[i][j]
        print(Max_dist)
