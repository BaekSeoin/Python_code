import sys
import heapq

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

A_i = [int(i) for i in sys.stdin.readline().rstrip().split()]

M = int(sys.stdin.readline().rstrip())

for x in range(M):
    i,j,k = map(int, sys.stdin.readline().rstrip().split())

    List = A_i[i-1:j]

    heapq.heapify(List)

    count = 0

    check = False

    while List:
        num = heapq.heappop(List)
        if num > k:
            check = True
            break
    if check:
        print(len(List)+1)
    else:
        print(0)
