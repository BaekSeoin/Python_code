import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

for i in range(1,N+1):
    print(' '*(i-1),end='')
    print('*' * (2*N- (2*i-1)))