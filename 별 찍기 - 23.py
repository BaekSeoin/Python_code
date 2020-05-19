import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [[' ' for i in range(4*N-3)] for j in range(2*N-1)]

a = (0,0)
b = (0, 4*N-4)
c = (2*N-2,0)
d = (2*N-2,4*N-4)

for i in range(1,N):
    shape[a[0]][a[1]+i] = '*'
    shape[b[0]][b[1]- i] = '*'
    shape[c[0]][c[1] + i] = '*'
    shape[d[0]][d[1] - i] = '*'


for i in range(N):
    shape[a[0]][a[1]] = '*'
    shape[a[0]][a[1]+ (N-1)] = '*'
    shape[b[0]][b[1]] = '*'
    shape[b[0]][b[1] - (N-1)] = '*'
    shape[c[0]][c[1]] = '*'
    shape[c[0]][c[1] + (N-1)] = '*'
    shape[d[0]][d[1]] = '*'
    shape[d[0]][d[1] - (N-1)] = '*'

    a = (a[0] + 1,a[1]+1)
    b = (b[0]+1,b[1]-1)
    c = (c[0]-1,c[1]+1)
    d = (d[0]-1,d[1]-1)

for i in range(2*N-1):
    print("".join(shape[i]).rstrip())