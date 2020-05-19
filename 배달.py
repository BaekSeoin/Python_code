import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int,sys.stdin.readline().rstrip().split())

map = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]
visit = [[[[[0 for i in range(M)] for j in range(N)] for k in range(4)] for q in range(2)] for p in range(2)]

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

direction = {(0,0):[(1,0),(-1,0),(0,1),(0,-1)],(1,0):[(-1,0),(0,1),(0,-1)],(-1,0):[(1,0),(0,1),(0,-1)],(0,1):[(1,0),(-1,0),(0,-1)],(0,-1):[(1,0),(-1,0),(0,1)]}
direction_num = {(1,0):0,(-1,0):1,(0,1):2,(0,-1):3}

count = 0
start = (0,0)
present= []

for i in range(N):
    for j in range(M):
        if map[i][j] == 'S':
            start = (i,j)
        elif map[i][j] == 'C':
            present.append((i,j))

first = present[0]
second = present[1]

def bfs(List):
    global count,min_dist

    while List:
        a = List.popleft()
        cur = a[0]
        dist = a[1]
        cur_dir = a[2]
        first_v = a[3]
        second_v = a[4]

        for dir in direction[cur_dir]:
            nextPos = (cur[0] + dir[0],cur[1] + dir[1])
            if nextPos == first:
                first_v_ = 1
            else:
                first_v_ = first_v

            if nextPos == second:
                second_v_ = 1
            else:
                second_v_ = second_v

            if (inRange(nextPos[0],nextPos[1])) and (visit[second_v_][first_v_][direction_num[dir]][nextPos[0]][nextPos[1]] == 0) \
                    and (map[nextPos[0]][nextPos[1]] != '#'):
                List.append((nextPos,dist+1,dir,first_v_,second_v_))
                visit[second_v_][first_v_][direction_num[dir]][nextPos[0]][nextPos[1]] = dist + 1

List = deque()
List.append((start,0,(0,0),0,0))

bfs(List)

max_a = 100000
max_b = 100000

for k in range(4):
    a = visit[1][1][k][first[0]][first[1]]
    b = visit[1][1][k][second[0]][second[1]]
    if a != 0:
        max_a = min(max_a,a)
    if b != 0:
        max_b = min(max_b,b)

if (max_a == 100000) and (max_b == 100000):
    print(-1)
else:
    print(min(max_a,max_b))