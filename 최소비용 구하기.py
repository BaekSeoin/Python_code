import sys
import heapq
sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

path = {}
for i in range(m):
    a,b,c = tuple(map(int, sys.stdin.readline().rstrip().split()))
    if a in path:
        path[a].append((c,b))
    else:
        path[a] = [(c,b)]

start, end = tuple(map(int, sys.stdin.readline().rstrip().split()))

List = []
visit = [100000*n for i in range(n+1)]

def bfs(List):
    while List:
        x = heapq.heappop(List)
        current = x[1]
        cost = x[0]

        if current in path:
            for i in path[current]:
                next = i[1]
                cost_2 = i[0] + cost
                if visit[next] >= cost_2:
                    heapq.heappush(List, (cost_2, next))
                    visit[next] = cost_2

for j in path[start]:
    heapq.heappush(List, j)
    visit[j[1]] = j[0]

bfs(List)
print(visit)
print(visit[end])