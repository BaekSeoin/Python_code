import sys
from collections import deque

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline().rstrip())

a,b = map(int, sys.stdin.readline().rstrip().split())

m = int(sys.stdin.readline().rstrip())

family = dict()
parents = dict()

for i in range(m):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    parents[y] = x
    try:
        family[x].append(y)
    except:
        family[x] = []
        family[x].append(y)

List = deque()
List.append((a,0))
final_count = -1

visit = dict()
visit[a] = True

while List:
    cur,count = List.popleft()

    if cur == b:
        final_count = count
        break
    try:
        for i in family[cur]:
            try:
                t = visit[i]
            except:
                List.append((i, count + 1))
                visit[i] = True
    except:
        pass

    try:
        pa = parents[cur]

        try:
            t = visit[pa]
        except:
            List.append((pa, count + 1))
            visit[pa] = True
        for i in family[pa]:
            if i != cur:
                try:
                    t = visit[i]
                except:
                    List.append((i,count + 2))
                    visit[i] = True
    except:
        pass



if final_count == -1:
    List = deque()
    List.append((b, 0))
    visit = dict()
    visit[b] = True
    final_count = -1

    while List:
        cur, count = List.popleft()

        if cur == a:
            final_count = count
            break
        try:

            for i in family[cur]:
                try:
                    t = visit[i]
                except:
                    List.append((i, count + 1))
                    visit[i] = True
        except:
            pass

        try:
            pa = parents[cur]

            try:
                t = visit[pa]
            except:
                List.append((pa, count + 1))
                visit[pa] = True

            for i in family[pa]:
                if i != cur:
                    try:
                        t = visit[i]
                    except:
                        List.append((i, count + 2))
                        visit[i] = True
        except:
            pass

print(final_count)
