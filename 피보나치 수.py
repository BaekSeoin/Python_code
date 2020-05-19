import sys

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline().rstrip())

memo = [-1 for i in range(n+1)]

if n == 0:
    memo[0] = 0
else:
    memo[0] = 0
    memo[1] = 1

def dp(n):
    if memo[n] != -1:
        return memo[n]

    a = dp(n-1)
    b = dp(n-2)
    ans = a+b
    memo[n] = ans
    return ans

print(dp(n))