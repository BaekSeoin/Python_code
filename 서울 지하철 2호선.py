import sys
import copy
from collections import deque

sys.setrecursionlimit(10000)

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

line = dict()
circle_or_not = dict()

for i in range(N):
    a,b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    try:
        line[a].append(b)
    except:
        line[a] = [b]
        circle_or_not[a] = 0
    try:
        line[b].append(a)
    except:
        line[b] = [a]
        circle_or_not[b] = 0

start_point = deque()
start = []
pos_point = []
visited = [0 for i in range(N+1)]

for key,value in line.items():
    if len(value) == 1:
        start_point.append(key)
        start.append(key)

    elif len(value) >=3:
        pos_point.append(key)


for st in start_point:
    circle_or_not[st] = -1



def BFS(start_point):
    while start_point:
        current = start_point.popleft()
        next_point = line[current]
        visited[current] = 1
        if len(next_point) == 1:
            circle_or_not[current] = -1
        else:
            count = 0
            for next in next_point:
                if circle_or_not[next] == 0 and visited[next] == 1:
                    count +=1
            if count >=2:
                circle_or_not[current] = 0
        for next in next_point:
            if circle_or_not[next] !=0:
                start_point.append(next)


BFS(start_point)
print(circle_or_not)
def bfs(List):
    while List:
        A = List.popleft()
        current = A[0]
        depth = A[1]
        if circle_or_not[current] == 0:
            return depth
        next = line[current]
        for n in next:
            if visited2[n] == 0:
                visited2[n] = 1
                List.append((n,depth+1))

visited = [0 for i in range(N+1)]

for k,v in circle_or_not.items():
    if v == -1:
        List = deque()
        List.append((k,0))
        visited2 = copy.deepcopy(visited)
        value = bfs(List)
        circle_or_not[k] = value

for s in range(1,N+1):
    dist = circle_or_not[s]
    if s !=N:
        print(dist,end=' ')
    else:
        print(dist)