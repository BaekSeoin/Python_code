import sys

sys.stdin = open("input.txt","r")

N,X = tuple(map(int,sys.stdin.readline().rstrip().split()))

text = 'BPPPB'

burger_L = 2**(N-1)


def dp(n):
    if store[n] != 0:
        return store[n]
    else:
        prev = dp(n-1)
        cur = 'B'+prev+'P'+prev+'B'
        store[n] = cur
        return store[n]

count = 0
hamburger= dp(N)
Len = len(hamburger)
for i in range(1,X+1):
    if hamburger[Len-i] == 'P':
        count+=1
print(count)



