import sys

sys.stdin = open('input.txt','r')

sys.setrecursionlimit(10**6)

N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))

memo = [[0 for i in range(M+1)] for j in range(N+1)]

memo[1][1] = 0

def dp(n,m):
    if n == 1:
        if m == 1:
            return memo[1][1]
        a = dp(n,m-1)
        memo[n][m] = a +1
        return memo[n][m]

    if memo[n][m] != 0:
        return memo[n][m]

    a = dp(n-1,m)
    memo[n][m] = a + m
    return memo[n][m]

print(dp(N,M))