import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

shape = [['*' for i in range(N)] for j in range(N)]

for i in range(N):
    print("".join(shape[i]))
