import sys
from collections import deque
sys.stdin = open("input.txt","r")

T = int(sys.stdin.readline().rstrip())

direction = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]

def inRange(n, a,b):
    if 0<=a and a<n and 0<= b and b < n:
        return True
    return False

for i in range(T):
    n = int(sys.stdin.readline().rstrip())
    start = tuple(map(int, sys.stdin.readline().rstrip().split()))
    end = tuple(map(int, sys.stdin.readline().rstrip().split()))

    discovered = [[0 for i in range(n)] for i in range(n)]

    List = deque()
    depth = 0
    List.append((start, depth))
    discovered[start[0]][start[1]] = 1

    while List:
        a = List.popleft()
        current = a[0]
        depth = a[1]

        if current == end:
            print(depth)
            break

        for i in direction:
            nextPos = (current[0] + i[0], current[1] + i[1])
            if inRange(n, nextPos[0], nextPos[1]) and discovered[nextPos[0]][nextPos[1]] != 1:
                List.append((nextPos, depth+1))
                discovered[nextPos[0]][nextPos[1]] = 1
