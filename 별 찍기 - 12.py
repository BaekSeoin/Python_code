import sys

sys.stdin = open("input.txt","r")

N = int(sys.stdin.readline().rstrip())

for i in range(1,2*N):
    if i <= N:
        print(' '*(N-i)+'*'*i)
    else:
        print(' '* (i-N)+'*'*(N*2-i))