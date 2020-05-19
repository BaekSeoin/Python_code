import sys
from collections import deque
sys.stdin = open("input.txt","r")

n,m = tuple(map(int, sys.stdin.readline().rstrip().split()))

board = [[int(i) for i in sys.stdin.readline().rstrip()] for j in range(n)]

direction = [(-1,0),(0,1),(1,0),(0,-1)]

check = [[0 for i in range(m)] for j in range(n)]

def inRange(a,b):
    if 0 <= a and a < n and 0 <= b and b < m:
        return True
    return False

count = 1

List = deque()
List.append(((0,0), count))
check[0][0] = count

while List:
    a = List.popleft()
    current = a[0]
    count = a[1]

    if current == (n-1,m-1):
        print(count)
        break

    for i in direction:
        nextPos = (current[0] + i[0], current[1] + i[1])
        if inRange(nextPos[0], nextPos[1]) and board[nextPos[0]][nextPos[1]] != 0 and check[nextPos[0]][nextPos[1]] == 0:
            check[nextPos[0]][nextPos[1]] = count + 1
            List.append((nextPos, count + 1))
