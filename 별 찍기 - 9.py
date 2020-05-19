import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

for i in range(2*N):
    if i == N:
        continue
    elif i < N:
        print(' '*i,end='')
        print('*'*(2*N-(2*i+1)))
        #print(' '*i)
    else:
        j = 2*N - i - 1
        print(' ' * j, end='')
        print('*' * (2 * N - (2 * j + 1)))
        #print(' ' * j)
