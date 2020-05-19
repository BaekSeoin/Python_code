import sys

sys.stdin = open('input.txt','r')

T = int(sys.stdin.readline().rstrip())

def dp(m,n):
    if n > m:
        return 0
    if memo[m][n] != 0:
        return memo[m][n]
    a = dp(m-1,n-1)
    b = dp(m-1,n)
    memo[m][n] = a+b
    return memo[m][n]

for t in range(T):
    N,M = tuple(map(int,sys.stdin.readline().rstrip().split()))
    memo = [[0 for i in range(N+1)] for j in range(M+1)]
    for i in range(1,M+1):
        memo[i][1] = i
        if N > 1:
            memo[i][2] = int(i * (i - 1) / 2)
    #print(memo)
    print(int(dp(M,N)))
