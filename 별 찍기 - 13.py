import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

for i in range(1,2*N):
    if i <= N:
        print('*'*i)
    else:
        j = 2*N - i
        print('*'*j)

