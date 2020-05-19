import sys
from collections import deque
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

direction = [(1,0),(0,1),(-1,0),(0,-1)]

#dist, island
discovered = [[[0,0] for i in range(n)] for j in range(n)]

def inRange(a,b):
    if 0<=a < n and 0<= b < n:
        return True
    return False

no_island = 1

def bfs(pos, no_island):
    global List
    List = deque()
    List.append(pos)
    discovered[pos[0]][pos[1]] = [0,no_island]

    while List:
        current = List.popleft()
        island_pos.append(current)

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1])
            if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] == 1 and discovered[nextPos[0]][nextPos[1]][1] == 0:
                discovered[nextPos[0]][nextPos[1]] = [0, no_island]
                List.append(nextPos)

island_pos = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and discovered[i][j][1] == 0:
            bfs((i,j),no_island)
            no_island += 1



min_value = 10000000

def search():
    global island_pos
    global min_value
    count = 0

    while island_pos:
        if count > 1:
            break
        current = island_pos.popleft()
        dist = discovered[current[0]][current[1]][0]
        no_island = discovered[current[0]][current[1]][1]

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1])
            if inRange(nextPos[0], nextPos[1]):
                if discovered[nextPos[0]][nextPos[1]][1] == 0:
                    island_pos.append(nextPos)
                    discovered[nextPos[0]][nextPos[1]][0] = dist + 1
                    discovered[nextPos[0]][nextPos[1]][1] = no_island

                elif discovered[nextPos[0]][nextPos[1]][1] != no_island:
                    value = dist + discovered[nextPos[0]][nextPos[1]][0]

                    if value < min_value:
                        min_value = value
                        count += 1
search()

print(min_value)