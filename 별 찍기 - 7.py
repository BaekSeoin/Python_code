import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

for i in range(1, 2*N):
    if i <= N:
        print(' '*(N-i)+'*'*(2*i-1))
    else:
        print(' '* (i-N)+'*' * (2* (2*N-i)-1))