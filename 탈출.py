import sys
from collections import deque

sys.stdin = open("input.txt","r")

direction = [(-1,0),(1,0),(0,-1),(0,1)]

row, column = tuple(map(int,sys.stdin.readline().rstrip().split()))
forest = [[i for i in sys.stdin.readline().rstrip()]for j in range(row)]
check = [[0 for i in range(column)] for j in range(row)]

def inRange(a,b):
    if 0<=a<row and 0<=b<column:
        return True
    return False

pos = deque()
time = 0

for i in range(row):
    for j in range(column):
        if forest[i][j] == 'S':
            S_pos = (i,j)
        elif forest[i][j] == '*':
            pos.append(((i,j),-1))
        elif forest[i][j] == 'D':
            final_pos = (i,j)
pos.append((S_pos,time))

def S_change(pos):
    while pos:
        a = pos.popleft()
        current = a[0]
        time = a[1]

        if time != -1:
            if current == final_pos:
                print(time)
                return

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1])
            if time == -1:
                if inRange(nextPos[0],nextPos[1]) and (forest[nextPos[0]][nextPos[1]] == '.' or forest[nextPos[0]][nextPos[1]] == 'S'):
                    pos.append((nextPos,time))
                    forest[nextPos[0]][nextPos[1]] = '*'
            else:
                if inRange(nextPos[0],nextPos[1]) and (forest[nextPos[0]][nextPos[1]] == '.' or forest[nextPos[0]][nextPos[1]] == 'D'):
                    pos.append((nextPos,time+1))
                    forest[nextPos[0]][nextPos[1]] = 'S'
    print('KAKTUS')

S_change(pos)