import sys

sys.stdin = open('input.txt','r')

n,k = map(int, sys.stdin.readline().rstrip().split())

Cn = [0]

memo = [[-1 for i in range(k+1)] for j in range(k+1)]

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    Cn.append(num)
    memo[num][num] = 1
    memo[num][k] = 0

    for j in range(i):
        memo[num][num-j+1] = 0

def dp(n,k):
    if memo[n][k] != -1:
        return memo[n][k]

    a = dp(n-1,k)
    b = dp(n,k-Cn[n])

    memo[n][k] = a + b
    return memo[n][k]



print(dp(n,k))

