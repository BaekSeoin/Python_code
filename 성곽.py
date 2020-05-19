import sys
from collections import deque

sys.stdin = open('input.txt','r')

col, row = map(int, sys.stdin.readline().rstrip().split())

board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(row)]

#
direction = [(-1,0),(1,0),(0,-1),(0,1)]
#남/동/북/서
direction_check = {(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}

def inRange(a,b):
    if (0<=a<row) and (0<=b<col):
        return True
    return False

for i in range(row):
    for j in range(col):
        ans = board[i][j]
        #남/동/북/서
        ans = [int(i) for i in str(format(ans, 'b'))]
        if len(ans) == 0:
            ans = [0,0,0,0]
        elif len(ans) == 1:
            ans = [0,0,0] + ans
        elif len(ans) == 2:
            ans = [0,0] + ans
        elif len(ans) == 3:
            ans = [0] + ans
        board[i][j] = ans

visit = [[0 for i in range(col)] for j in range(row)]


def bfs(List):
    global count, room
    while List:
        curPos = List.popleft()

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            check = direction_check[dir]

            if (inRange(nextPos[0],nextPos[1])) and (board[curPos[0]][curPos[1]][check] == 0) and (visit[nextPos[0]][nextPos[1]] == 0):
                List.append(nextPos)
                visit[nextPos[0]][nextPos[1]] = room
                count += 1

room = 0
max_count = 0
room_dict = dict()

for i in range(row):
    for j in range(col):
        if visit[i][j] == 0:
            room += 1
            List = deque()
            List.append((i,j))
            count = 1
            visit[i][j] = room
            count +=1
            bfs(List)
            max_count = max(max_count, count - 1)
            room_dict[room]  = count - 1
print(room)
print(max_count)

addMaxCount = 0

for i in range(row):
    for j in range(col):
        curPos = (i,j)
        curRoom = visit[curPos[0]][curPos[1]]
        curRoomCount = room_dict[curRoom]

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])):
                nextRoom = visit[nextPos[0]][nextPos[1]]
                if curRoom != nextRoom:
                    nextRoomCount = room_dict[nextRoom]
                    ans = curRoomCount + nextRoomCount
                    addMaxCount = max(addMaxCount, ans)
print(addMaxCount)

