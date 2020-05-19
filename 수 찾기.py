import sys
sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())
A = [int(i) for i in sys.stdin.readline().rstrip().split()]
A.sort()

m = int(sys.stdin.readline().rstrip())

M = [int(i) for i in sys.stdin.readline().rstrip().split()]

result = [0]*m
Len = len(A)


for index,value in enumerate(M):
    mid = Len // 2

    if Len == 1:
        if A[0] == value:
            result[index] = 1
    else:

        if value > A[mid]:
            while value > A[mid] and mid < Len -1:
                mid += 1
                if A[mid] == value:
                    result[index] = 1
                    break


        elif value < A[mid]:
            while value < A[mid] and mid > 0:
                mid -= 1
                if A[mid] == value:
                    result[index] = 1
                    break
        else:
            result[index] = 1

for i in result:
    print(i)





