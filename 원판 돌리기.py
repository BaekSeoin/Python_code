import sys
from collections import deque

sys.stdin = open('input.txt','r')

N,M,T = tuple(map(int,sys.stdin.readline().rstrip().split()))

circle = []

for i in range(N):
    List = deque(int(i) for i in sys.stdin.readline().rstrip().split())
    circle.append(List)

for test in range(T):
    x,d,k = tuple(map(int,sys.stdin.readline().rstrip().split()))

    for i in range(x,N+1,x):
        if d == 0:
            circle[i - 1].rotate(k)
        else:
            circle[i - 1].rotate(-k)
    List = dict()
    total_count = 0
    for i in range(N):
        for j in range(M):
            if circle[i][j] !=0:
                count = 0
                if j+1 < M:
                    if circle[i][j] == circle[i][j+1]:
                        List[(i,j+1)] = True
                        count +=1
                else:
                    if circle[i][j] == circle[i][0]:
                        List[(i,0)] = True
                        count +=1
                if j-1 != -1:
                    if circle[i][j] == circle[i][j-1]:
                        List[(i, j - 1)] = True
                        count +=1
                else:
                    if circle[i][j] == circle[i][M-1]:
                        List[(i, M -1)] = True
                        count +=1

                if ((i+1) < N) and circle[i][j] == circle[i+1][j]:
                    List[(i+1,j)] = True
                    count +=1
                total_count += count

                if count !=0:
                    List[(i,j)] = True
    if total_count !=0:
        for i,j in List.keys():
            circle[i][j] = 0
    else:
        S = 0
        c = 0
        for i in circle:
            for j in i:
                if j !=0:
                    c +=1
                    S +=j
        if S !=0 and c !=0:
            avg = S / c

            for index,i in enumerate(circle):
                for index2,j in enumerate(i):
                    if j !=0:
                        if j > avg:
                            circle[index][index2] = j - 1
                        elif j < avg:
                            circle[index][index2] = j + 1


ans = 0
for i in range(N):
    for j in range(M):
        ans += circle[i][j]
print(ans)

