import sys

sys.stdin = open('input.txt','r')

n = int(sys.stdin.readline().rstrip())

dp = [0 for i in range(n+1)]

for i in range(1,n+1):
    if i == 1:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
