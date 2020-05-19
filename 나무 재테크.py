import sys
from collections import deque

sys.stdin = open("input.txt","r")

direction = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def inRange(a,b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

n,m,k = tuple(map(int, sys.stdin.readline().rstrip().split()))
A = [[5 for i in range(n)]for j in range(n)]
A_plus = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(n)]

tree = [[deque() for i in range(n)] for j in range(n)]

for i in range(m):
    x,y,age = tuple(map(int, sys.stdin.readline().rstrip().split()))
    tree[x-1][y-1].append([age,1])

for i in range(n):
    for j in range(n):
        sorted(tree[i][j])

def spring(r,c,a):
    global Fall
    result = deque()
    while a:
        i = a.popleft()
        age = i[0]
        if A[r][c] >= age:
            A[r][c] -= age
            result.append([age+1,1])
            if (age+1) % 5 == 0:
                Fall.append((r,c))
        else:
            result.append([age,0])
    return result

def summer(r,c,a):
    while a:
        i = a.pop()
        live = i[1]
        age = i[0]
        if live == 0:
            A[r][c] += age // 2
        else:
            a.append([age,live])
            break
def fall(Fall):
    for i in Fall:
        for j in direction:
            nextPos = (i[0]+j[0], i[1]+j[1])
            if inRange(nextPos[0],nextPos[1]):
                tree[nextPos[0]][nextPos[1]].appendleft([1,1])
def winter():
    for i in range(n):
        for j in range(n):
            plus = A_plus[i][j]
            A[i][j] += plus

for year in range(k):
    Fall =[]
    #봄 & 여름
    for i in range(n):
        for j in range(n):
            if tree[i][j] != deque():
                result = spring(i,j,tree[i][j])
                tree[i][j] = result
                summer(i,j,tree[i][j])
    #가을
    fall(Fall)
    #겨울
    winter()

def tree_live(a):
    global count
    for i in a:
        if i[1] == 1:
            count+=1
        else:
            return
count = 0
for i in range(n):
    for j in range(n):
        if tree[i][j] != deque():
            tree_live(tree[i][j])
print(count)