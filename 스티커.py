import sys

sys.stdin = open('input.txt','r')

sys.setrecursionlimit(100001*2)

T = int(sys.stdin.readline().rstrip())

def dp(n):
    if memo[0][n] != -1 and memo[1][n] != -1:
        return max(memo[0][n], memo[1][n])

    if memo[0][n-1] == -1:
        dp(n-1)
    first = memo[0][n-1] + sticker[1][n-1]
    second = memo[1][n-1] + sticker[0][n-1]
    third = dp(n-2) + sticker[1][n-1]
    fourth = dp(n-2) + sticker[0][n-1]

    memo[0][n] = max(second, fourth)
    memo[1][n] = max(first, third)

    return max(memo[0][n], memo[1][n])


for t in range(T):
    n = int(sys.stdin.readline().rstrip())
    sticker = [[int(i) for i in sys.stdin.readline().rstrip().split()] for j in range(2)]
    memo = [[-1 for i in range(n+1)] for j in range(2)]
    a = sticker[0][0]
    b = sticker[1][0]

    memo[0][1] = a
    memo[1][1] = b

    if n > 1:
        c = sticker[0][1]
        d = sticker[1][1]

        memo[0][2] = b+c
        memo[1][2] = a+d

    print(dp(n))
