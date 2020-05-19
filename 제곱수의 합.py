import sys

sys.stdin = open('input.txt','r')
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline().rstrip())

memo = [-1 for i in range(n+1)]
memo[1] = 1

for i in range(1,n):
    a = i * i
    if a > n:
        break
    memo[a] = 1

def dp(n):

    if memo[n] != -1:
        return memo[n]

    ans = 10000
    for i in range(1, int(n // 2) + 1):
        if memo[i] != -1:
            a = memo[i]
        else:
            a = dp(i)
        if memo[n-i] != -1:
            b = memo[n-i]
        else:
            b = dp(n-i)
        ans = min(ans, a+b)
    memo[n] = ans
    return memo[n]

if memo[n] != -1:
    print(memo[n])
else:
    for i in range(1,n+1):
        dp(i)
    print(memo[n])