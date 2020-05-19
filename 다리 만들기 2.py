import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int,sys.stdin.readline().rstrip().split())
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

start = dict()

check = [[0 for i in range(M)] for j in range(N)]

island = 1

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

def dfs(i,j):
    for dir in direction:
        nextPos = (i+dir[0], j+dir[1])
        if (inRange(nextPos[0], nextPos[1])) and (board[nextPos[0]][nextPos[1]] == 1) and (check[nextPos[0]][nextPos[1]] == 0):
            check[nextPos[0]][nextPos[1]] = island
            dfs(nextPos[0],nextPos[1])

for i in range(N):
    for j in range(M):
        if (check[i][j] == 0) and (board[i][j] == 1):
            check[i][j] = island
            dfs(i,j)
            island+=1


for i in range(N):
    for j in range(M):
        if check[i][j] !=0:
            for dir in direction:
                nextPos = (i+dir[0], j+dir[1])
                if inRange(nextPos[0], nextPos[1]) and check[nextPos[0]][nextPos[1]] == 0:
                    try:
                        start[check[i][j]].append((i,j))
                        break
                    except:
                        start[check[i][j]] = []
                        start[check[i][j]].append((i,j))
                        break

store = [[0 for i in range(island)] for j in range(island)]

for k,v in start.items():
    for (i,j) in v:
        for dir in direction:
            nextPos = (i+dir[0], j+dir[1])
            while inRange(nextPos[0], nextPos[1]):
                if check[nextPos[0]][nextPos[1]] != k:
                    if check[nextPos[0]][nextPos[1]] != 0:
                        ans = (abs(i-nextPos[0]), abs(j-nextPos[1]))
                        dist = max(ans[0], ans[1]) - 1
                        n = check[nextPos[0]][nextPos[1]]
                        if dist >= 2:
                            if store[k][n] == 0:
                                store[k][n] = dist
                            else:
                                if dist < store[k][n]:
                                    store[k][n] = dist
                        break
                    nextPos = (nextPos[0] + dir[0], nextPos[1] + dir[1])
                else:
                    break

ans_list = []


for i in range(1,island-1):
    for j in range(i+1, island):
        ans = store[i][j]
        if ans !=0:
            ans_list.append((i,j, ans))

max_index = len(ans_list)
List = []
index = 0
min_dist = 100000

def bfs(List, island_check):

    visit = []
    visit.append(List[0])

    while List:
        cur = List.popleft()
        next_island = island_check[cur]
        for i in next_island:
            if i not in visit:
                visit.append(i)
                List.append(i)


    return visit

def dfsimport sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int,sys.stdin.readline().rstrip().split())
board = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(N)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

start = dict()

check = [[0 for i in range(M)] for j in range(N)]

island = 1

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

def dfs(i,j):
    for dir in direction:
        nextPos = (i+dir[0], j+dir[1])
        if (inRange(nextPos[0], nextPos[1])) and (board[nextPos[0]][nextPos[1]] == 1) and (check[nextPos[0]][nextPos[1]] == 0):
            check[nextPos[0]][nextPos[1]] = island
            dfs(nextPos[0],nextPos[1])

for i in range(N):
    for j in range(M):
        if (check[i][j] == 0) and (board[i][j] == 1):
            check[i][j] = island
            dfs(i,j)
            island+=1


for i in range(N):
    for j in range(M):
        if check[i][j] !=0:
            for dir in direction:
                nextPos = (i+dir[0], j+dir[1])
                if inRange(nextPos[0], nextPos[1]) and check[nextPos[0]][nextPos[1]] == 0:
                    try:
                        start[check[i][j]].append((i,j))
                        break
                    except:
                        start[check[i][j]] = []
                        start[check[i][j]].append((i,j))
                        break

store = [[0 for i in range(island)] for j in range(island)]

for k,v in start.items():
    for (i,j) in v:
        for dir in direction:
            nextPos = (i+dir[0], j+dir[1])
            while inRange(nextPos[0], nextPos[1]):
                if check[nextPos[0]][nextPos[1]] != k:
                    if check[nextPos[0]][nextPos[1]] != 0:
                        ans = (abs(i-nextPos[0]), abs(j-nextPos[1]))
                        dist = max(ans[0], ans[1]) - 1
                        n = check[nextPos[0]][nextPos[1]]
                        if dist >= 2:
                            if store[k][n] == 0:
                                store[k][n] = dist
                            else:
                                if dist < store[k][n]:
                                    store[k][n] = dist
                        break
                    nextPos = (nextPos[0] + dir[0], nextPos[1] + dir[1])
                else:
                    break

ans_list = []


for i in range(1,island-1):
    for j in range(i+1, island):
        ans = store[i][j]
        if ans !=0:
            ans_list.append((i,j, ans))

max_index = len(ans_list)
List = []
index = 0
min_dist = 100000

def bfs(List, island_check):

    visit = []
    visit.append(List[0])

    while List:
        cur = List.popleft()
        next_island = island_check[cur]
        for i in next_island:
            if i not in visit:
                visit.append(i)
                List.append(i)


    return visit

def dfs(List, index):
    global min_dist

    if len(List) == island-2:
        island_check = dict()
        island_dist = 0

        for a,b,c in List:
            try:
                island_check[a].append(b)
            except:
                island_check[a] = []
                island_check[a].append(b)
            try:
                island_check[b].append(a)
            except:
                island_check[b] = []
                island_check[b].append(a)

            island_dist += c

        lst = deque()
        lst.append(a)

        visit = bfs(lst, island_check)

        if len(visit) == (island - 1):
            if island_dist < min_dist:
                min_dist = island_dist
        return
    if index > max_index - 1:
        return

    cur = ans_list[index]
    List.append(cur)
    dfs(List, index+1)
    List.pop()
    dfs(List, index+1)

dfs(List, index)
if min_dist == 100000:
    print(-1)
else:
    print(min_dist)(List, index)
    global min_dist

    if len(List) == island-2:
        island_check = dict()
        island_dist = 0

        for a,b,c in List:
            try:
                island_check[a].append(b)
            except:
                island_check[a] = []
                island_check[a].append(b)
            try:
                island_check[b].append(a)
            except:
                island_check[b] = []
                island_check[b].append(a)

            island_dist += c

        lst = deque()
        lst.append(a)

        visit = bfs(lst, island_check)

        if len(visit) == (island - 1):
            if island_dist < min_dist:
                min_dist = island_dist
        return
    if index > max_index - 1:
        return

    cur = ans_list[index]
    List.append(cur)
    dfs(List, index+1)
    List.pop()
    dfs(List, index+1)

dfs(List, index)
if min_dist == 100000:
    print(-1)
else:
    print(min_dist)