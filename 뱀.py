import sys
from collections import deque

sys.stdin = open("input.txt","r")

n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())

board = [[0 for i in range(n)] for j in range(n)]
#북/동/남/서 & 왼/오
direction = {(-1,0):[(0,-1),(0,1)], (0,1):[(-1,0),(1,0)],(1,0):[(0,1),(0,-1)],(0,-1):[(1,0),(-1,0)]}

def inRange(a,b):
    if 0<=a<n and 0<=b<n:
        return True
    return False

for i in range(k):
    a,b = tuple(map(int,sys.stdin.readline().rstrip().split()))
    board[a-1][b-1] = 1

l = int(sys.stdin.readline().rstrip())

change = deque()
for i in range(l):
    a, b = tuple(map(str, sys.stdin.readline().rstrip().split()))
    change.append((int(a),b))

dir = (0,1)

time = 0
current = deque()
current.append((0,0))

check = [[0 for i in range(n)] for j in range(n)]
check[0][0] = 1

while True:
    if len(change) > 0 and time == change[0][0]:
        x,c = change.popleft()
        if c == 'L':
            dir = direction[dir][0]
        else:
            dir = direction[dir][1]
    nextPos = (current[0][0] + dir[0], current[0][1] + dir[1])
    time +=1
    if inRange(nextPos[0],nextPos[1]) == False or check[nextPos[0]][nextPos[1]] == 1:
        print(time)
        break
    if board[nextPos[0]][nextPos[1]] == 1:
        current.appendleft(nextPos)
        board[nextPos[0]][nextPos[1]] = 0
        check[nextPos[0]][nextPos[1]] = 1
    else:
        current.appendleft(nextPos)
        prev = current.pop()
        check[nextPos[0]][nextPos[1]] = 1
        check[prev[0]][prev[1]] = 0

