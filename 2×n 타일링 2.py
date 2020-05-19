import sys

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline().rstrip())
if n >= 2:
    memo = [-1 for i in range(n+1)]
    memo[1] = 1
    memo[2] = 3
else:
    memo = [-1 for i in range(n + 1)]
    memo[1] = 1

def dp(n):
    if memo[n] != -1:
        return memo[n]
    else:
        ans = dp(n-2) * 2 + dp(n-1)
        memo[n] = ans
        return memo[n]

print(dp(n) % 10007)
