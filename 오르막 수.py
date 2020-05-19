import sys

sys.stdin = open('input.txt','r')

N = int(sys.stdin.readline().rstrip())

memo = [[0 for i in range(10)] for j in range(N)]

for i in range(10):
    memo[0][i] = 1
    if i == 0:
        for j in range(N):
            memo[j][i] = 1
    if N > 1:
        memo[1][i] = i+1

for i in range(N):
    for j in range(10):
        if memo[i][j] == 0:
            a = memo[i-1][j]
            b = memo[i][j-1]
            memo[i][j] = a+b

print(sum(memo[N-1])%10007)