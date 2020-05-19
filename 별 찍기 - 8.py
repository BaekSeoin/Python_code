import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

for i in range(1,2*N):
    if i <= N:
        print('*'*i,end='')
        print(' '*(2*N-2*i),end='')
        print('*'*i)
    else:
        j = 2*N - i
        print('*' * j, end='')
        print(' ' * (2 * N - 2 * j), end='')
        print('*' * j)
