import sys
import copy
from collections import deque

sys.stdin = open('input.txt','r')

N,M = map(int, sys.stdin.readline().rstrip().split())

map = [[i for i in sys.stdin.readline().rstrip()] for j in range(N)]
visit = [[[[[[[[-1 for i in range(M)] for j in range(N)] for a in range(2)] for b in range(2)] for c in range(2)] for d in range(2)]
         for e in range(2)] for f in range(2)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

key_check = {'a':True,'b':True,'c':True,'d':True,'e':True,'f':True}

key_change = {'A':'a','B':'b','C':'c','D':'d','E':'e','F':'f'}

end = []

for i in range(N):
    for j in range(M):
        if map[i][j] == '0':
            start = (i,j)
            map[i][j] = '.'
        elif map[i][j] == '1':
            end.append((i,j))
            map[i][j] = '.'

def inRange(a,b):
    if (0<=a<N) and (0<=b<M):
        return True
    return False

def keyInfo(x,a,b,c,d,e,f):
    if x == 'a':
        if a == 1:
            return True
        else:
            return False
    elif x == 'b':
        if b == 1:
            return True
        else:
            return False
    elif x == 'c':
        if c == 1:
            return True
        else:
            return False
    elif x == 'd':
        if d == 1:
            return True
        else:
            return False
    elif x == 'e':
        if e == 1:
            return True
        else:
            return False
    elif x == 'f':
        if f == 1:
            return True
        else:
            return False


min_dist = 100000

def bfs(List):

    while List:
        x = List.popleft()
        cur = x[0]
        dist = x[1]
        a = x[2]
        b = x[3]
        c = x[4]
        d = x[5]
        e = x[6]
        f = x[7]

        for dir in direction:
            nextPos = (cur[0] + dir[0], cur[1] + dir[1])
            if (inRange(nextPos[0],nextPos[1])) and (visit[a][b][c][d][e][f][nextPos[0]][nextPos[1]] == -1):
                if map[nextPos[0]][nextPos[1]] == '#':
                    continue
                elif map[nextPos[0]][nextPos[1]] == '.':
                    List.append((nextPos,dist+1,a,b,c,d,e,f))
                    visit[a][b][c][d][e][f][nextPos[0]][nextPos[1]] = dist + 1
                else:
                    try:
                        k = key_change[map[nextPos[0]][nextPos[1]]]
                        if keyInfo(k,a,b,c,d,e,f):
                            List.append((nextPos,dist+1,a,b,c,d,e,f))
                            visit[a][b][c][d][e][f][nextPos[0]][nextPos[1]] = dist + 1
                    except:
                        try:
                            if key_check[map[nextPos[0]][nextPos[1]]]:
                                a_,b_,c_,d_,e_,f_ = a,b,c,d,e,f
                                if map[nextPos[0]][nextPos[1]] == 'a':
                                    a_ = 1
                                elif map[nextPos[0]][nextPos[1]] == 'b':
                                    b_ = 1
                                elif map[nextPos[0]][nextPos[1]] == 'c':
                                    c_ = 1
                                elif map[nextPos[0]][nextPos[1]] == 'd':
                                    d_ = 1
                                elif map[nextPos[0]][nextPos[1]] == 'e':
                                    e_ = 1
                                elif map[nextPos[0]][nextPos[1]] == 'f':
                                    f_ = 1
                                List.append((nextPos, dist + 1,a_,b_,c_,d_,e_,f_))
                                visit[a_][b_][c_][d_][e_][f_][nextPos[0]][nextPos[1]] = dist + 1
                        except:
                            continue

List = deque()
lst = []
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

List.append((start,0,a,b,c,d,e,f))
visit[a][b][c][d][e][f][start[0]][start[1]] = 0
bfs(List)

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for i,j in end:
                            dist = visit[a][b][c][d][e][f][i][j]
                            if dist == -1:
                                continue
                            if dist < min_dist:
                                min_dist = dist

if min_dist != 100000:
    print(min_dist)
else:
    print(-1)
