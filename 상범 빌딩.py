import sys
from collections import deque

sys.stdin = open('input.txt','r')

direction = [(0,-1,0),(0,0,-1),(0,1,0),(0,0,1),(1,0,0),(-1,0,0)]

def inRange(a,b,c):
    if (0<=a<L) and (0<=b<R) and (0<=c<C):
        return True
    return False

while True:

    L, R, C = map(int, sys.stdin.readline().rstrip().split())

    if (L == 0) and (R == 0) and (C == 0):
        break

    building = []
    visit = [[[0 for i in range(C)] for j in range(R)] for k in range(L)]
    for k in range(L):
        subb_building = []
        for j in range(R):
            sub_building = []
            for index,i in enumerate(sys.stdin.readline().rstrip()):
                if i == 'S':
                    start = (k,j,index)
                    visit[k][j][index] = 1
                if i == 'E':
                    end = (k,j,index)
                sub_building.append(i)
            subb_building.append(sub_building)
        a = sys.stdin.readline().rstrip()
        building.append(subb_building)


    List = deque()
    List.append((start,0))

    stop = False

    while List:
        x = List.popleft()
        cur = x[0]
        time = x[1]

        for dir in direction:
            nextPos = (cur[0] + dir[0], cur[1] + dir[1], cur[2] + dir[2])
            if (inRange(nextPos[0],nextPos[1], nextPos[2])) and (building[nextPos[0]][nextPos[1]][nextPos[2]] != '#') and (visit[nextPos[0]][nextPos[1]][nextPos[2]] == 0):
                visit[nextPos[0]][nextPos[1]][nextPos[2]] = 1
                if nextPos == end:
                    stop = True
                    break
                List.append((nextPos, time+1))
        if stop:
            break
    if stop:
        print("Escaped in", time+1, "minute(s).")
    else:
        print("Trapped!")

