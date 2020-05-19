import sys
from collections import deque

sys.stdin = open("input.txt","r")

F, S, G, U, D = tuple(map(int, sys.stdin.readline().rstrip().split()))
time = 0
List = deque()

"""if G > S and U != 0:
    b = (G-S) // U
    S += b*U
    time = b
elif G <= S and D != 0:
    b = (S-G) // D
    S -= b*D
    time = b"""

List.append((S,time))

up_down = [U,-D]
visited = [0 for i in range(F+1)]
visited[S] = 1

while List:
    a = List.popleft()
    current = a[0]
    time = a[1]
    if current == G:
        print(time)
        break

    for i in up_down:
        nextPos = current + i
        if nextPos > F or nextPos < 1:
            continue
        elif visited[nextPos] == 0:
            visited[current] = 1
            List.append((nextPos,time+1))

    if len(List) == 0:
        print("use the stairs")
        break
