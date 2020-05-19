import sys
import copy
from collections import deque

sys.stdin = open("input.txt","r")

N, M = tuple(map(int, sys.stdin.readline().rstrip().split()))
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

visited = [[-1 for i in range(N)] for j in range(N)]

def inRange(a,b):
    if 0<=a<N and 0<=b<N:
        return True
    return False

virus = []
count = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i,j))
            count +=1
        elif board[i][j] == 1:
            visited[i][j] = None
        elif board[i][j] == 0:
            count +=1

num_of_virus = len(virus)
virus_collect = []
subset = []

def dfs(index, subset):
    global M
    if len(subset) == M:
        subset_2 = copy.deepcopy(subset)
        virus_collect.append(subset_2)
        return

    for i in range(index,num_of_virus-M+index+1):
        if i >= num_of_virus:
            break
        current = virus[i]
        subset.append(current)
        dfs(i+1, subset)
        subset.pop()
    return

dfs(0,subset)

def bfs(List, visited_2):
    global result, Min, number, count
    Max_time = 0
    while List:
        a = List.popleft()
        current = a[0]
        time = a[1]
        b = 0

        for i in direction:
            nextPos = (current[0] + i[0], current[1]+i[1])
            if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] !=1 and visited_2[nextPos[0]][nextPos[1]] ==-1:
                if len(result) > 0 and time+1 >= Min:
                    return 1000000
                if board[nextPos[0]][nextPos[1]] == 2:
                    visited_2[nextPos[0]][nextPos[1]] = 0
                    if time > Max_time:
                        Max_time = time
                else:
                    visited_2[nextPos[0]][nextPos[1]] = time+1
                    if time +1 > Max_time:
                        Max_time = time + 1
                number += 1
                List.append((nextPos,time + 1))

        if number == count:
            break

    if number == count:
        Max = Max_time
    else:
        Max = -1

    return Max

result = []
Min = 10000000
for k in virus_collect:
    visited_2 = copy.deepcopy(visited)
    List = deque()
    number = len(k)
    for q in k:
        visited_2[q[0]][q[1]] = 0
        List.append((q,0))
    time = bfs(List, visited_2)
    if time != -1 and time < Min:
        Min = time
        result.append(time)
    elif time == -1 and -1 not in result:
        result.append(time)

if max(result) == -1:
    print(-1)
else:
    result.sort()
    if num_of_virus == count:
        print(0)
    elif result[0] == -1:
        print(result[1])
    else:
        print(result[0])