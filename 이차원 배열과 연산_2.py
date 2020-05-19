import sys
import heapq
sys.stdin = open("input.txt","r")

r,c,k = tuple(map(int, sys.stdin.readline().rstrip().split()))

A = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(3)]

time = 0

def move(A):
    Max_row = 0
    for index, p in enumerate(A):
        array = [0 for k in range(max(p) + 1)]
        for number in p:
            array[number] += 1
        heap = []
        for index_2, count in enumerate(array):
            if index_2 == 0 or count == 0:
                continue
            heapq.heappush(heap, (count, index_2))
        A[index] = []
        while heap:
            q = heapq.heappop(heap)
            A[index].append(q[1])
            A[index].append(q[0])
            if len(A[index]) > 100:
                break
        if Max_row < len(A[index]):
            Max_row = len(A[index])

    for add in range(len(A)):
        A_add = len(A[add])
        if A_add < Max_row:
            while A_add != Max_row:
                A[add].append(0)
                A_add += 1

while True:
    row = len(A)
    col = len(A[0])

    if time > 100:
        print(-1)
        break

    if (row > r-1) and (col > c-1) and A[r-1][c-1] == k:
        print(time)
        break

    time +=1

    if row >= col:
        move(A)

    else:
        A = [list(x) for x in zip(*A)]
        move(A)
        A = [list(x) for x in zip(*A)]
