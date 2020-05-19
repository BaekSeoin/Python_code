import sys
from collections import deque

sys.stdin = open("input.txt","r")

T = int(input().rstrip())

def bfs(start,List,check):
    global n_count
    while List:
        x = List.popleft()
        cur = x[0]
        prev = x[1]
        move = x[2]
        if move == Z:
            if cur >= start and check[cur] == 0:
                check[cur] +=1
                n_count += 1
            continue
        for next in line[cur]:
            if next != prev:
                List.append((next,cur,move+1))

for test in range(1,T+1):
    line = dict()
    N,M,Z = tuple(map(int,input().rstrip().split()))
    if Z > M and M!=1:
        Z = Z % (M-1) + (M-1)
    for i in range(M):
        a,b = tuple(map(int,input().rstrip().split()))
        try:
            line[a].append(b)
        except:
            line[a] = [b]
        try:
            line[b].append(a)
        except:
            line[b] = [a]
    n_count = 0
    for i in range(1,N+1):
        check = [0 for j in range(N + 1)]
        List = deque()
        List.append((i,0,0))
        bfs(i,List,check)
    print('#'+str(test),end=' ')
    print(n_count)
