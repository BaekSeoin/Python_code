import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[" " for i in range(2*N-1)] for j in range(N)]

Range = (0,2*N-1)

for i in range(N-1,-1,-1):
    if i == (N-1):
        for j in range(2*N-1):
            if j % 2 == 0:
                shape[i][j] = '*'
    else:
        for j in range(Range[0], Range[1]):
            if shape[i+1][j] ==" ":
                shape[i][j] = "*"

    Range = (Range[0]+1, Range[1]-1)

for i in range(N):
    print("".join(shape[i]).rstrip())
