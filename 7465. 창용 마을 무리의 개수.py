import sys
sys.stdin = open("input.txt","r")

T = int(input())

def dfs(List,result):
    if len(List) == 0:
        return

    current = List.pop()

    for u in town[current]:
        if result[u-1] == 0:
            result[u-1] = c
            List.append(u)
            dfs(List, result)

for i in range(T):
    n,m = tuple(map(int, input().split()))
    result = [0 for j in range(n)]
    c = 1
    town = {}
    for o in range(1,n+1):
        town[o] = []

    if m == 0:
        print('#', end='')
        print(i + 1, end=' ')
        print(n)
        continue

    for k in range(m):
        a,b = tuple(map(int, input().split()))
        town[a].append(b)
        town[b].append(a)

    for y in town:

        if result[y-1] ==0:
            List = []
            result[y-1] = c
            List.append(y)
            dfs(List, result)
            c += 1

    print('#',end='')
    print(i+1,end=' ')
    print(c-1)