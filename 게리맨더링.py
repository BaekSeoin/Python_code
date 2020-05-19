import sys
from collections import deque

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

population = [int(i) for i in sys.stdin.readline().rstrip().split()]

connect = dict()

for i in range(N):
    x = [int(j) for j in sys.stdin.readline().rstrip().split()]
    connect[i+1] = []

    for j in x[1:]:
        connect[i+1].append(j)

min_pop = 100**2


def check(List):
    visit = dict()
    op_List = []

    for i in range(1,N+1):
        if i not in List:
            op_List.append(i)

    start_list = deque()
    start_list.append(List[0])

    while start_list:
        cur = start_list.popleft()
        next_pos = connect[cur]

        for i in next_pos:
            if i in List:
                try:
                    a = visit[i]
                except:
                    visit[i] = True
                    start_list.append(i)
    start_list = deque()
    start_list.append(op_List[0])

    while start_list:
        cur = start_list.popleft()

        next_pos = connect[cur]

        for i in next_pos:
            if i in op_List:
                try:
                    a = visit[i]
                except:
                    visit[i] = True
                    start_list.append(i)

    if len(List) == 1:
        visit[List[0]] = True
    if len(op_List) == 1:
        visit[op_List[0]] = True

    if len(visit) == N:
        return True
    return False

def cal(List):
    global min_pop

    a = 0
    b = 0

    for i in range(1,N+1):
        if i in List:
            a += population[i-1]
        else:
            b += population[i-1]
    ans = abs(a-b)

    if ans < min_pop:
        min_pop = ans


def dfs(List, cur):

    if (len(List) != 0) and (len(List) != N):
        if check(List):
            cal(List)

    for i in range(cur+1, N+1):
        List.append(i)
        dfs(List, i)
        List.pop()

List = []
dfs(List, 0)

if min_pop != 100**2:
    print(min_pop)
else:
    print(-1)