import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[" " for i in range(2*N)] for j in range(N)]

for i in range(N):
    if i % 2 == 0:
        for j in range(0,2*N,2):
            shape[i][j] = '*'
    else:
        for j in range(1,2*N,2):
            shape[i][j] = '*'

for i in range(N):
    print("".join(shape[i]).rstrip())