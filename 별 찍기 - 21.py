import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[' ' for i in range(N)] for j in range(2*N)]


for i in range(2*N):
    for j in range(N):
        if (i %2 == 0) and (j % 2 == 0):
            shape[i][j] = '*'
        elif (i%2 == 1) and (j % 2 ==1):
            shape[i][j] = '*'

for i in range(2*N):
    print("".join(shape[i]).rstrip())
