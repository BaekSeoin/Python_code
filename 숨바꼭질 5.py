import sys
from collections import deque, OrderedDict

sys.stdin = open("input.txt", "r")

N, sis_current = tuple(map(int,sys.stdin.readline().rstrip().split()))

store_sis_pos = sis_current

#짝수초/홀수초
visited = dict()
visited[N] = [0,-1]

sister_pos = OrderedDict()
sister_pos[sis_current] = 0

store_time=0

def sister_move(sis_current,time):
    sis_current += time
    return sis_current

for time in range(1,500001):
    sis_current = sister_move(sis_current,time)
    if sis_current > 500000:
        store_time = time
        break
    sister_pos[sis_current] = time

List = deque()
List.append((N,0))

def bfs(List):
    while List:
        A = List.popleft()
        current =A[0]
        time = A[1]

        for i in range(3):
            if i == 0:
                nextPos = current - 1
            elif i == 1:
                nextPos = current +1
            else:
                nextPos = current * 2

            if (0<=nextPos<=500000) and time+1 < store_time:
                ans = (time+1) % 2 #짝수면 0, 홀수면 1
                try:
                    if visited[nextPos][ans] == -1:
                        visited[nextPos][ans] = time + 1
                        List.append((nextPos,time+1))
                except:
                    visited[nextPos] = [-1,-1]
                    visited[nextPos][ans] = time+1
                    List.append((nextPos,time+1))

bfs(List)

final = 0

#위치, 시간
for cur_pos,cur_time in sister_pos.items():
    ans = cur_time % 2
    try:
        subin = visited[cur_pos][ans]
        if (cur_time >= subin) and (subin != -1):
            print(cur_time)
            final = 1
            break
    except:
        continue

if final == 0:
    print(-1)

