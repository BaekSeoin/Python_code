import sys
import heapq

sys.stdin = open("input.txt","r")

V,E = tuple(map(int, sys.stdin.readline().rstrip().split()))

K = int(sys.stdin.readline().rstrip())

node = [[[],[]] for i in range(V+1)]
#[[[][]],[[],[]]]
node[0] = None

for i in range(E):
    u,v,w = tuple(map(int, sys.stdin.readline().rstrip().split()))
    node[u][0].append(v)
    node[u][1].append(w)

path = [10000000 for i in range(V+1)]
path[0] = None
path[K] = 0

List = []
heapq.heappush(List,(path[K],K))

while List:
    a = heapq.heappop(List)
    current_dist = a[0]
    current_pos = a[1]

    if current_dist > path[current_pos]:
        continue

    for next_Node_ID, next_Node_weight in zip(node[current_pos][0], node[current_pos][1]):
        if path[next_Node_ID] > path[current_pos] + next_Node_weight:
            path[next_Node_ID] = path[current_pos] + next_Node_weight
            heapq.heappush(List,(path[next_Node_ID],next_Node_ID))

for i in range(1,len(path)):

    if path[i] == 10000000:
        print("INF")
    else:
        print(path[i])