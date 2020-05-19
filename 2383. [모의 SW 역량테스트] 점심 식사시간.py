import sys
import operator

sys.stdin = open("input.txt", "r")

T = int(input().rstrip())

def find_stairs():
    storage = []
    for i in people:
        min_P = 1000
        for st in stairs:
            P = abs(i[0]-st[0]) + abs(i[1] - st[1]) + 1 + st[2]
            if P < min_P:
                min_P = P
                Pos = st
        #시간, 계단, 사람
        storage.append((min_P,Pos,i))
    storage = sorted(storage,key = operator.itemgetter(0))
    people2 = []
    for j in storage:
        people2.append(j[2])
    """
    for j in storage:
        if len(stairs[j[1]]) <3:
            stairs[j[1]].append(j[0])
        else:
            people2.append(j[2])"""
    return people2

def dfs(index):
    global time

    if index == len(people):
        d = 0
        for a,b in stairs.items():
            if len(b) == 0:
                continue
            c = max(b)
            if d < c:
                d = c
        if d < time:
            time = d
        return

    current = people[index]

    for k,v in stairs.items():
        if len(v) < 3:
            path = abs(current[0] - k[0]) + abs(current[1] - k[1]) + 1 + k[2]
            stairs[k].append(path)
            dfs(index+1)
            stairs[k].pop()
        else:
            stairs[k].sort()
            I = len(v) - 3
            Y = stairs[k][I]
            if abs(current[0] - k[0]) + abs(current[1] - k[1]) + 1 >= Y:
                path = abs(current[0] - k[0]) + abs(current[1] - k[1]) + 1 + k[2]
                stairs[k].append(path)
            else:
                stairs[k].append(Y + k[2])
            dfs(index+1)
            stairs[k].pop()

for test in range(1,T+1):
    N = int(input().rstrip())
    people = []
    stairs = dict()
    time = 10000
    for i in range(N):
        for j,x in enumerate(input().rstrip().split()):
            x = int(x)
            if x == 1:
                people.append((i,j))
            elif x > 1:
                stairs[(i,j,x)] = []
    people = find_stairs()
    dfs(0)
    print('#' + str(test),end=' ')
    if time !=10000:
        print(time)
    else:
        print(0)