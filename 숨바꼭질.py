import sys
from collections import deque
sys.stdin = open("input.txt","r")

N, K = (map(int, sys.stdin.readline().rstrip().split()))

def inRange(a):
    if 0<= a and a <= 100000:
        return True
    return False

Pos = deque()
check = [0 for i in range(100001)]

Pos.append((N,0))
check[N] = 1

while deque:
    a = Pos.popleft()
    current = a[0]
    time = a[1]

    if current == K:
        print(time)
        break

    nextPos = current - 1
    if inRange(nextPos) and check[nextPos] != 1:
        Pos.append((nextPos, time+1))
        check[nextPos] = 1

    nextPos = current + 1
    if inRange(nextPos)and check[nextPos] != 1:
        Pos.append((nextPos, time+1))
        check[nextPos] = 1

    nextPos = current * 2
    if inRange(nextPos) and check[nextPos] != 1:
        Pos.append((nextPos,time+1))
        check[nextPos] = 1

