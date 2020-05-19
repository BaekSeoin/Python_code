import sys

sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10**6)

n,m = tuple(map(int, sys.stdin.readline().rstrip().split()))

Dic = {}
for i in range(1,n+1):
    Dic[i] = []


for i in range(m):
    a,b = tuple(map(int, sys.stdin.readline().rstrip().split()))
    Dic[a].append(b)
    Dic[b].append(a)

check = [0 for i in range(n+1)]
connected = 1

def dfs(current):
    global check
    for j in Dic[current]:
        if check[j] == 0:
            check[j] = connected
            dfs(j)

for k in range(1,n+1):
    if check[k] == 0:
        check[k] = connected
        dfs(k)
        connected +=1

print(max(check))