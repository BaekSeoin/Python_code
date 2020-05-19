import sys

sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(5000)

N = int(sys.stdin.readline().rstrip())

line = dict()

for j in range(N):
    a,b = tuple(map(int,sys.stdin.readline().rstrip().split()))
    try:
        line[a].append(b)
    except:
        line[a] = [b]
    try:
        line[b].append(a)
    except:
        line[b] = [a]

visit = [0 for i in range(N+1)]

ans = 0
point = 0
change = 0

def dfs(start,current,prev,visit):
    global ans,point,change
    next_line = line[current]
    for next in next_line:
        if next != prev:
            if visit[next] == -1 and next == start:
                ans = 1
                return
            elif visit[next] == -1 and next != start:
                ans = 2
                point = next
                return
            visit[next] = -1
            dfs(start,next,current,visit)
            if ans == 1:
                return
            elif ans == 2 and current == point and change == 0:
                change = 1
                return
            elif ans == 2 and current != point and change == 0:
                return
            elif change == 1:
                visit[current] = 0
                return
            visit[next] = 0

visit[1] = -1
dfs(1,1,0,visit)

def dfs2(n,prev):
    if visit[n] !=0 and visit[n] != -1:
        return visit[n]

    next_line = line[n]
    min_ans = []
    if len(next_line) == 1 and next_line[0] == prev:
        return -5
    for next in next_line:
        if next != prev:
            if visit[next] == -1:
                min_ans.append(1)
            elif visit[next] != 0:
                min_ans.append(visit[next] + 1)
            else:
                ans = dfs2(next,n)
                if ans != -5:
                    min_ans.append(ans+1)
    visit[n] = min(min_ans)
    return visit[n]

one_next = line[1]

one_count = 0
for o_n in one_next:
    if visit[o_n] == -1:
        one_count +=1
if one_count < 2:
    visit[1] = 0

for n in range(1,N+1):
    if len(line[n]) == 1:
        dfs2(n,0)

for i in range(1,N+1):
    if visit[i] == -1:
        if i !=N:
            print(0,end=' ')
        else:
            print(0)
    else:
        if i!=N:
            print(visit[i],end=' ')
        else:
            print(visit[i])