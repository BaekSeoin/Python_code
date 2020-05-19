import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

path = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

direction = {}

for i in range(1,n+1):
    direction[i] = [int(j) for j in range(1,n+1) if j != i]

def dfs(List, start,current,cost):
    global Min_cost

    for i in direction[current]:
        if path[current - 1][i - 1] !=0 and i != start and i not in List:
            cost += path[current - 1][i - 1]
            if cost < Min_cost:
                List.append(i)
                dfs(List, start, i, cost)
                List.pop()
                cost -= path[current - 1][i - 1]
            else:
                cost -= path[current - 1][i - 1]
        elif path[current - 1][i - 1] !=0 and len(List) == n and i == start:
            cost += path[current - 1][i - 1]
            if cost <= Min_cost:
                Min_cost = cost
            return

Min_cost = 1000000 * n +1
for i in range(1,n+1):
    cost = 0
    List = []
    List.append(i)
    dfs(List,i,i,cost)

print(Min_cost)