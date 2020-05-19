import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline().rstrip())

List = deque()

for i in range(N):
    x = [i for i in sys.stdin.readline().rstrip().split()]
    if x[0] == "push":
        List.append(int(x[1]))
    elif x[0] == "pop":
        if len(List) > 0:
            y = List.popleft()
            print(y)
        else:
            print(-1)
    elif x[0] == "size":
        print(len(List))
    elif x[0] == "empty":
        if len(List) == 0:
            print(1)
        else:
            print(0)
    elif x[0] == "front":
        if len(List) > 0:
            print(List[0])
        else:
            print(-1)
    elif x[0] =="back":
        if len(List) > 0:
            print(List[-1])
        else:
            print(-1)