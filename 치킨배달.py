import sys
import copy

sys.stdin = open("input.txt","r")

n,m = tuple(map(int, sys.stdin.readline().rstrip().split()))
city = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

chicken_result = []

def dfs(List,m,index):
    if len(List) == m:
        List_2 = copy.deepcopy(List)
        chicken_result.append(List_2)
        return
    if index >= len(chicken):
        return

    current = chicken[index]
    #선택
    List.append(current)
    dfs(List,m,index+1)
    List.pop()
    #선택 안함
    dfs(List,m,index+1)

for i in range(1,m+1):
    List = []
    dfs(List,i,0)

min_chicken = 100000000000000

for i in chicken_result:
    path = 0
    home_2 = [100000 for q in range(len(home))]
    for j in i:
        for u,k in enumerate(home):
            diff = abs(j[0]-k[0]) + abs(j[1]-k[1])
            if home_2[u] > diff:
                home_2[u] = diff
    path = sum(home_2)
    if path < min_chicken:
        min_chicken = path

print(min_chicken)