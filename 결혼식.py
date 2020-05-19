import sys

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

friends = dict()

for j in range(n+1):
    friends[j] = []

for i in range(m):
    a,b = tuple(map(int,sys.stdin.readline().rstrip().split()))
    friends[a].append(b)
    friends[b].append(a)

visited = [0 for i in range(n+1)]
#visited[1] = 1
count = 0

def dfs(current,depth):
    global count
    if depth > 2:
        return

    if visited[current] == 0:
        visited[current] = 1
        count +=1

    for i in friends[current]:
        nextPos = i
        dfs(nextPos,depth + 1)

dfs(1,0)
print(count-1)