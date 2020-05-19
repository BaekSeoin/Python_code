import sys
import heapq
import copy
sys.stdin = open("input.txt","r")

r,c,k = tuple(map(int, sys.stdin.readline().rstrip().split()))

A = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(3)]

time = 0
List = [0 for g in range(len(A[0]))]

def cleansing(row, COL,A):
    for i in range(row):
        A[i][COL] = 0
    return A


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
        Max_row = 0
        for index,p in enumerate(A):
            array = [0 for k in range(max(p)+1)]
            for number in p:
                array[number] += 1
            heap = []
            for index_2,count in enumerate(array):
                if index_2 == 0 or count == 0:
                    continue
                heapq.heappush(heap,(count,index_2))
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
                    A_add +=1
    else:
        for COL in range(len(A[0])):
            column = []
            for ROW in range(len(A)):
                column.append(A[ROW][COL])
            array = [0 for i in range(len(column)+1)]
            for number in column:
                array[number] +=1
            heap = []
            for index_2, count in enumerate(array):
                if index_2 == 0 or count == 0:
                    continue
                heapq.heappush(heap, (count, index_2))

            order = -2
            A = cleansing(row, COL, A)
            while heap:
                q = heapq.heappop(heap)

                order += 2
                if len(A) <= order+1:
                    List_2 = copy.deepcopy(List)
                    List_3 = copy.deepcopy(List)
                    if len(A) % 2 == 0:
                        A.append(List_2)
                        A.append(List_3)
                    else:
                        A.append(List_2)

                A[order][COL] = q[1]
                A[order+1][COL] = q[0]

                if order+1 >= 99:
                    break
