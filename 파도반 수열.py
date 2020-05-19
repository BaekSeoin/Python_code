import sys

sys.stdin = open('input.txt','r')


T = int(sys.stdin.readline().rstrip())

memo = [0 for i in range(101)]
memo[1] =1
memo[2] =1
memo[3] =1
memo[4] =2
memo[5] =2


def dp(n):
    if memo[n] !=0:
        return memo[n]

    a = dp(n-1)
    b = dp(n-5)
    memo[n] = a + b
    return memo[n]

for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp(n))