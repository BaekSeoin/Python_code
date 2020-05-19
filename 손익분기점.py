import sys

sys.stdin = open('input.txt','r')

A,B,C = map(int,sys.stdin.readline().rstrip().split())


if C != B:
    n = (A//(C-B)) + 1
else:
    n = 0

if n > 0:
    print(n)
else:
    print(-1)

