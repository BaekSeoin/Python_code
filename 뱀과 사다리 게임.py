import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

move = [0 for i in range(101)]

visit = [0 for i in range(101)]

for n in range(N):
    x,y = tuple(map(int,sys.stdin.readline().rstrip().split()))
    move[x] = y

for m in range(M):
    u,v = tuple(map(int,sys.stdin.readline().rstrip().split()))
    move[u] = v

def bfs(List):
    while List:
        A = List.popleft()
        current = A[0]
        depth = A[1]
        if current == 100:
            print(depth)
            return

        for next in range(1,7):
            nextPos = current + next
            if nextPos <=100 and move[nextPos] !=0:
                nextPos = move[nextPos]
            if nextPos <= 100 and visit[nextPos] == 0:
                visit[nextPos] = 1
                List.append((nextPos,depth+1))
List = deque()
List.append((1,0))
bfs(List)