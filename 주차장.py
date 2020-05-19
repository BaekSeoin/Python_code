import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int,sys.stdin.readline().rstrip().split())

board = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]

direction = [(1,0),(-1,0),(0,-1),(0,1)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

car = []
parking = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 'C':
            car.append((i,j))
        elif board[i][j] == 'P':
            parking.append((i,j))

car_index = 0
ans_min_time = 1000000
time_list = []

dist = dict()

for i in car:
    dist[i] = dict()
    for j in parking:
        dist[i][j] = 1000000

def bfs(curPos, parkingPos):
    global min_time, max_time

    curVisit = [[0 for i in range(M)] for j in range(N)]
    curVisit[curPos[0]][curPos[1]] = 1
    List = deque()
    List.append((curPos,0))
    start = curPos

    while List:
        x = List.popleft()
        curPos = x[0]
        time = x[1]

        if curPos == parkingPos:
            dist[start][parkingPos] = time
            if time not in time_list:
                time_list.append(time)
            return

        for dir in direction:
            nextPos = (curPos[0] + dir[0], curPos[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (board[nextPos[0]][nextPos[1]] !='X') \
                    and (curVisit[nextPos[0]][nextPos[1]] == 0):
                List.append((nextPos,time+1))
                curVisit[nextPos[0]][nextPos[1]] = 1
    return


for i in car:
    min_time = 1000000
    for j in parking:
        bfs(i,j)

time_list.sort()

parking_list = dict()

check = dict()

for i in time_list:
    check[i] = 0

for i in car:
    curParking = dist[i]
    parking_list[i] = []
    find_min = 1000000
    find_max = 0

    for k,v in curParking.items():
        parking_list[i].append((v,k))
        find_min = min(v,find_min)
        find_max = max(v,find_max)

    parking_list[i].sort()

    for j in range(find_min,find_max+1):
        try:
            check[j] +=1
        except:
            continue
print(check)

def dfs(car_index,time):
    global ans_min_time, stop

    if car_index == len(car):
        ans_min_time = time
        stop = True
        return

    curPos = car[car_index]
    pList = parking_list[curPos]

    for p in pList:
        parkingPos = p[1]
        if p[0] == 1000000:
            stop = True
            return
        if visit[parkingPos[0]][parkingPos[1]] == 0:
            cur_time = dist[curPos][parkingPos]
            if cur_time > time:
                return

            visit[parkingPos[0]][parkingPos[1]] = 1
            dfs(car_index+1,time)
            visit[parkingPos[0]][parkingPos[1]] = 0
            if stop:
                return


for time in time_list:
    a = check[time]
    if a >= len(car):
        stop = False
        visit = [[0 for i in range(M)] for j in range(N)]
        dfs(0,time)

        if ans_min_time != 1000000:
            break

if len(car) == 0:
    print(0)
elif ans_min_time == 1000000:
    print(-1)
else:
    print(ans_min_time)