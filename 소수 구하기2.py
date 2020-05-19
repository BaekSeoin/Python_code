import sys

sys.stdin = open("input.txt","r")

m,n = tuple(map(int, sys.stdin.readline().rstrip().split()))

def find(n):
    s = [True] * (n+1)

    for i in range(2, int((n) ** 0.5) + 1):
        if s[i]:
            for j in range(i+i, n+1, i):
                s[j] = False

    return [i for i in range(2,n+1) if s[i]]

l = find(n)

for i in l:
    if i >= m:
        print(i)