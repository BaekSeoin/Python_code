import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

row, column = tuple(map(int, sys.stdin.readline().rstrip().split()))

miro = [[i for i in sys.stdin.readline().rstrip()] for j in range(row)]
J_visit = [[0 for i in range(column)]for j in range(row)]

direction = [(1,0),(0,1),(-1,0),(0,-1)]

def inRange(a,b):
    if 0<= a <row and 0<= b < column:
        return True
    return False

collect_jihoon_pos = deque()
collect_fire_pos = deque()
dist = 0

collect_fire_pos = deque()

for i in range(row):

    for j in range(column):
        if miro[i][j] == "J":
            jihoon_pos = (i,j)
            J_visit[i][j] = 1
        if miro[i][j] == "F":
            collect_fire_pos.append((i,j))

collect_jihoon_pos.append((jihoon_pos, miro, dist, collect_fire_pos))

def jihoon(collect_jihoon_pos, J_visit):
    global ans
    ans = 0
    while collect_jihoon_pos:
        a = collect_jihoon_pos.popleft()
        current = a[0]
        dist = a[2]

        for j in direction:
            count = 0
            nextPos = (current[0] + j[0], current[1] + j[1])
            if inRange(nextPos[0], nextPos[1]) and a[1][nextPos[0]][nextPos[1]] == '.' and J_visit[nextPos[0]][nextPos[1]] == 0:
                miro = copy.deepcopy(a[1])
                collect_fire_pos = a[3]
                miro[current[0]][current[1]] = '.'
                miro[nextPos[0]][nextPos[1]] = 'J'
                J_visit[nextPos[0]][nextPos[1]] = 1
                check, next_fire_pos, miro = fire(miro, collect_fire_pos)
                if check:
                    collect_jihoon_pos.append(((nextPos[0], nextPos[1]),miro, dist+1, next_fire_pos))
                if not check:
                    count += 1
                    if count == 4:
                        return ans

            elif not inRange(nextPos[0], nextPos[1]):
                ans = dist + 1
                return ans


def fire(miro, collect_fire_pos):
    next_fire_pos = deque()
    miro_v2 = copy.deepcopy(miro)

    for i in collect_fire_pos:
        current = i
        for j in direction:
            nextPos = (current[0] + j[0], current[1] + j[1])

            if inRange(nextPos[0], nextPos[1]) and miro_v2[nextPos[0]][nextPos[1]] == ".":
                miro_v2[nextPos[0]][nextPos[1]] = "F"
                next_fire_pos.append(nextPos)
            elif inRange(nextPos[0], nextPos[1]) and miro_v2[nextPos[0]][nextPos[1]] =='J':
                return False, False, False

    return True, next_fire_pos, miro_v2

jihoon(collect_jihoon_pos, J_visit)

if ans > 0:
    print(ans)
else:
    print("IMPOSSIBLE")
